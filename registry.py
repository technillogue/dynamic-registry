import datetime
import io
import gzip
import hashlib
import json
import logging
import os
import tarfile
from dataclasses import dataclass

from aiohttp import web

import data

logging.getLogger().setLevel("DEBUG")

# ```md
# r2-public-worker.drysys.workers.dev
# place at usr/share/nginx/html/reimu.webp and tarball
# sha256sum
# update some stuff, at least
# /v2/technillogue/nginx-reimu/manifests/latest
# actually that lists digests for the manifests; we need to create a fake one first
# .layers = .layers +
# {
#     "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
#     "size": 28867,
#     "digest": "sha256:e2b4981857892d233ef79621f7ca0cd004733c26c2c47906fce2edc44a76a80b",
# }
# (fsLayers, etc)
# also need to update digest: "For manifests, this is the manifest body without the signature content, also known as the JWS payload."
# serve it at /v2/technillogue/nginx-reimu/manifests/<digest>
#
# .config.digest is the entrypoint and stuff and may not be necessary
#
# then serve the tarball at v2/technillogue/nginx-reimu/blobs/sha256:e2b4981857892d233ef79621f7ca0cd004733c26c2c47906fce2edc44a76a80b
# ```


def mktar(image_path: str, layer_path: str) -> None:
    basename = os.path.basename(image_path)
    basepath = "usr/share/nginx/html"
    with tarfile.open(layer_path, "w:gz") as tar:
        info = tarfile.TarInfo(f"{basepath}/index.html")
        index = f'<!DOCTYPE html><img src="{basename}">'.encode()
        info.size = len(index)
        tar.addfile(info, io.BytesIO(index))
        tar.add(image_path, arcname=f"{basepath}/{basename}")


def sha256sum(_data: bytes) -> str:
    return "sha256:" + hashlib.sha256(_data).hexdigest()


def diff_id(fname: str) -> str:
    with gzip.open(fname, "rb") as f_in:
        return sha256sum(f_in.read())


def file_digest(fname: str) -> str:
    return sha256sum(open(fname, "rb").read())


@dataclass
class Image:
    name: str
    cfg: dict
    cfg_digest: str
    manifest: dict
    manifest_digest: str
    manifest_list: dict
    layer_fname: str
    layer_digest: str
    # layer_diff_id: str
    tag: str = "latest"


def make_image(image_path: str) -> Image:
    name = os.path.basename(image_path).split(".")[0]
    layer_fname = f"/tmp/{name}.tgz"
    mktar(image_path, layer_fname)

    layer_diff_id = diff_id(layer_fname)
    config = dict(data.config)
    config["rootfs"]["diff_ids"].append(layer_diff_id)
    history = {
        "created": datetime.datetime.now().isoformat() + "Z",
        "created_by": "dynamic",
        "comment": "dynamic"
    }
    config["history"].append(history)
    config_digest = sha256sum(json.dumps(config).encode())

    layer_digest = file_digest(layer_fname)
    layer = {
        "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
        "size": os.stat(layer_fname).st_size,
        "digest": layer_digest,
    }
    manifest = dict(data.manifest)
    manifest["layers"].append(layer)
    manifest["config"]["digest"] = config_digest
    manifest["config"]["size"] = len(json.dumps(config))
    manifest_digest = sha256sum(json.dumps(manifest).encode())

    manifest_list = dict(data.manifest_list)
    manifest_list["manifests"][0] = {
        "digest": manifest_digest,
        "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
        "platform": {"architecture": "amd64", "os": "linux"},
        "size": len(json.dumps(manifest)),
    }

    return Image(
        f"dynamic/{name}",
        cfg=config,
        cfg_digest=config_digest,
        manifest=manifest,
        manifest_digest=manifest_digest,
        manifest_list=manifest_list,
        layer_fname=layer_fname,
        layer_digest=layer_digest,
    )


marisa = make_image("test/marisa.png")
images = {marisa.name: marisa}

# if 1:
#     f = "/tmp/reimu.tar.gz"
#     layer_digest = "sha256:" + file_digest(f)
#     layer = {
#         "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
#         "size": os.stat(f).st_size,
#         "digest": layer_digest,
#     }
#     print("layer digest:", layer_digest)

#     layer_diff_id = diff_id(f)
#     print("layer diff_id:", layer_diff_id)
#     data.config["rootfs"]["diff_ids"].append(layer_diff_id)
#     now = "2023-05-23T20:13:28.137843Z"  # datetime.datetime.now().isoformat()
#     data.config["history"].append(
#         {"created": now, "created_by": "dynamic", "comment": "dynamic"}
#     )
#     cfg = json.dumps(data.config)
#     cfg_digest = "sha256:" + hashlib.sha256(cfg.encode()).hexdigest()
#     print("cfg digest:", cfg_digest)

#     data.manifest["layers"].append(layer)
#     data.manifest["config"]["digest"] = cfg_digest
#     data.manifest["config"]["size"] = len(cfg)
#     manifest = json.dumps(data.manifest)  # , separators=(',', ':'))
#     mf_digest = "sha256:" + hashlib.sha256(manifest.encode()).hexdigest()

#     assert len(data.manifest["layers"]) == len(
#         list(filter(lambda x: not x.get("empty_layer"), data.config["history"]))
#     )

#     data.manifest_list["manifests"][0] = {
#         "digest": mf_digest,
#         "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
#         "platform": {"architecture": "amd64", "os": "linux"},
#         "size": len(manifest),
#     }
#     print("manifest digest:", mf_digest)
#     print(
#         "manfist list digest:",
#         sha256sum(json.dumps(data.manifest_list).encode()),
#         "(shouldn't show up)",
#     )
#     name = "dyn/reimu2"
# else:
#     mf_digest = (
#         "sha256:3f01b0094e21f7d55b9eb7179d01c49fdf9c3e1e3419d315b81a9e0bae1b6a90"
#     )
#     name = "library/nginx"


async def handle(req: web.Request) -> web.Response:
    print("\n=======new request=======")
    print(req)
    print(req.path)

    for name, image in images.items():
        if req.path == f"/v2/{name}/manifests/latest":
            if req.method == "HEAD":
                return web.Response(
                    headers={
                        "Docker-Content-Digest": image.manifest_digest,
                        "Content-Length": str(len(json.dumps(image.manifest))),
                    }
                )
            # it seems like if HEAD doesn't return Docker-Content-Digest, it's expected to return the manifest
            # docker hashes whatever it is and uses that as the digest
            # if it tries to hash the manifest list and use that as a digest instead of the manifest digest, that won't work
            #
            # however, the actual docker registry returns the manifest list at this endpoint
            #
            # maybe we should check Accept: to determine what's expected

            print(image.manifest_list, end="\n\n")
            return web.json_response(
                image.manifest_list,
                content_type="application/vnd.docker.distribution.manifest.list.v2+json",
            )
            # oh
        if req.path == f"/v2/{name}/manifests/{image.manifest_digest}":
            print(image.manifest, end="\n\n")
            return web.json_response(
                image.manifest,
                content_type="application/vnd.docker.distribution.manifest.v2+json",
            )
        if req.path == f"/v2/{name}/blobs/{image.cfg_digest}":
            print(image.cfg)
            return web.json_response(
                image.cfg, content_type="application/vnd.docker.container.image.v1+json"
            )
        if req.path == f"/v2/{name}/blobs/{image.layer_digest}":
            print("sending blob")
            return web.FileResponse(
                image.layer_fname, headers={"Content-Type": "application/octet-stream"}
            )

    url = f"https://registry-1.docker.io{req.url.relative()}"
    print(url, end="\n\n")
    raise web.HTTPFound(url)


app = web.Application()
app.add_routes([web.route("*", "/{tail:.*}", handle)])
web.run_app(app, port=9090)
