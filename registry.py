import datetime
import io
import gzip
import hashlib
import json
import logging
import os
import tarfile
from copy import deepcopy
from dataclasses import dataclass

from aiohttp import web

import data

logging.getLogger().setLevel("DEBUG")


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
    cfg: str
    cfg_digest: str
    manifest: str
    manifest_digest: str
    manifest_list: str
    layer_fname: str
    layer_digest: str
    # layer_diff_id: str
    tag: str = "latest"


def make_image(image_path: str) -> Image:
    name = os.path.basename(image_path).split(".")[0]
    layer_fname = f"/tmp/{name}.tgz"
    mktar(image_path, layer_fname)

    layer_diff_id = diff_id(layer_fname)
    config = deepcopy(data.config)
    config["rootfs"]["diff_ids"].append(layer_diff_id)  # type: ignore
    history = {
        "created": datetime.datetime.now().isoformat() + "Z",
        "created_by": "dynamic",
        "comment": "dynamic",
    }
    config["history"].append(history)  # type: ignore
    config_str = json.dumps(config)
    config_digest = sha256sum(config_str.encode())
    print("image id:", config_digest)

    layer_digest = file_digest(layer_fname)
    print("layer digest:", layer_digest)
    layer = {
        "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
        "size": os.stat(layer_fname).st_size,
        "digest": layer_digest,
    }
    manifest = deepcopy(data.manifest)
    manifest["layers"].append(layer)  # type: ignore
    manifest["config"]["digest"] = config_digest  # type: ignore
    manifest["config"]["size"] = len(config_str)  # type: ignore
    manifest_str = json.dumps(manifest)
    manifest_digest = sha256sum(manifest_str.encode())
    print("manifest digest:", manifest_digest)

    manifest_list = deepcopy(data.manifest_list)
    manifest_list["manifests"][0] = {  # type: ignore
        "digest": manifest_digest,
        "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
        "platform": {"architecture": "amd64", "os": "linux"},
        "size": len(manifest_str),
    }
    manifest_list_str = json.dumps(manifest_list_str)

    return Image(
        f"dynamic/{name}",
        cfg=config_str,
        cfg_digest=config_digest,
        manifest=manifest_str,
        manifest_digest=manifest_digest,
        manifest_list=manifest_list_str,
        layer_fname=layer_fname,
        layer_digest=layer_digest,
    )


marisa = make_image("test/marisa.png")
reimu = make_image("test/reimu.webp")
images = {marisa.name: marisa, reimu.name: reimu}
base_image = "library/nginx"
base_tag = "1.25.0-bullseye"


async def handle(req: web.Request) -> web.StreamResponse:
    print("\n=======new request=======")
    print(req)

    for name, image in images.items():
        if req.path == f"/v2/{name}/manifests/latest":
            if req.method == "HEAD":
                return web.Response(
                    headers={
                        "Docker-Content-Digest": image.manifest_digest,
                        "Content-Length": str(len(image.manifest)),
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
            return web.Response(
                text=image.manifest_list,
                content_type="application/vnd.docker.distribution.manifest.list.v2+json",
            )
            # oh
        if req.path == f"/v2/{name}/manifests/{image.manifest_digest}":
            print(image.manifest, end="\n\n")
            return web.Response(
                image.manifest,
                content_type="application/vnd.docker.distribution.manifest.v2+json",
            )
        if req.path == f"/v2/{name}/blobs/{image.cfg_digest}":
            print(image.cfg)
            return web.Response(
                image.cfg, content_type="application/vnd.docker.container.image.v1+json"
            )
        if req.path == f"/v2/{name}/blobs/{image.layer_digest}":
            print("sending blob")
            return web.FileResponse(
                image.layer_fname, headers={"Content-Type": "application/octet-stream"}
            )

    url = f"https://registry-1.docker.io{req.url.relative()}".replace(
        "latest", base_tag
    )
    for name in images:
        url.replace(name, base_image)
    print(url, end="\n\n")
    raise web.HTTPFound(url)


app = web.Application()
app.add_routes([web.route("*", "/{tail:.*}", handle)])
web.run_app(app, port=9090)
