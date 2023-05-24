import hashlib
import json
import logging
import os
import re
import tarfile
import yarl
import aiohttp
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
{
    "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
    "size": 28867,
    "digest": "sha256:e2b4981857892d233ef79621f7ca0cd004733c26c2c47906fce2edc44a76a80b",
}
# (fsLayers, etc)
# also need to update digest: "For manifests, this is the manifest body without the signature content, also known as the JWS payload."
# serve it at /v2/technillogue/nginx-reimu/manifests/<digest>
#
# .config.digest is the entrypoint and stuff and may not be necessary
#
# then serve the tarball at v2/technillogue/nginx-reimu/blobs/sha256:e2b4981857892d233ef79621f7ca0cd004733c26c2c47906fce2edc44a76a80b
# ```


def sha256_uncompressed(tar_filename):
    sha256 = hashlib.sha256()

    with tarfile.open(tar_filename, 'r:gz') as f:
        for member in f.getmembers():
            if member.isfile():
                file = f.extractfile(member)
                if file:
                    sha256.update(file.read())

    return sha256.hexdigest()
def sha256sum(f: str) -> str:
    return hashlib.sha256(open(f, "rb").read()).hexdigest()


def mktar():
    with tarfile.open("/tmp/reimu.tar", "w") as tar:
    # with tarfile.open("/tmp/reimu.tar.gz", "w:gz") as tar:
        info = tarfile.TarInfo(name="usr/share/nginx/html/reimu.webp")
        with open("/home/sylv/misc/registry-302/test/reimu.webp", "rb") as f:
            info.size = os.fstat(f.fileno()).st_size
            tar.addfile(info, f)
    return tar


mktar()

if 1:
    # f = "/tmp/reimu.tar.gz"
    f = "/tmp/reimu.tar"
    layer_digest = f"sha256:{sha256sum(f)}"
    layer = {
        # "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
        "mediaType": "application/vnd.docker.image.rootfs.diff.tar",
        "size": os.stat(f).st_size,
        "digest": layer_digest,
    }
    print("layer digest:", layer_digest)

    # data.config["rootfs"]["diff_ids"].append("sha256:" + sha256_uncompressed(f))
    data.config["rootfs"]["diff_ids"].append(layer_digest)
    now = "2023-05-23T20:13:28.137843Z" # datetime.datetime.now().isoformat()
    data.config["history"].append({"created":now, "created_by": "dynamic", "comment": "dynamic"})
    cfg = json.dumps(data.config)
    cfg_digest = "sha256:" + hashlib.sha256(cfg.encode()).hexdigest()
    print("cfg digest:", cfg_digest)

    data.manifest["layers"].append(layer)
    data.manifest["config"]["digest"] = cfg_digest
    data.manifest["config"]["size"] = len(cfg)
    manifest = json.dumps(data.manifest)  # , separators=(',', ':'))
    mf_digest = "sha256:" + hashlib.sha256(manifest.encode()).hexdigest()


    assert len(data.manifest["layers"]) == len(list(filter(lambda x:not x.get("empty_layer"), data.config["history"])))

    data.manifest_list["manifests"][0] = {
        "digest": mf_digest,
        "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
        "platform": {"architecture": "amd64", "os": "linux"},
        "size": len(manifest),
    }
    print("manifest digest:", mf_digest)
    name = "dyn/reimu2"
else:
    mf_digest = (
        "sha256:3f01b0094e21f7d55b9eb7179d01c49fdf9c3e1e3419d315b81a9e0bae1b6a90"
    )
    name = "library/nginx"


async def handle(req: web.Request) -> web.Response:
    if "sess" not in req.app:
        req.app["sess"] = aiohttp.ClientSession()
    cs = req.app["sess"]
    print("\n=======new request=======")
    print(req)
    print(req.path)
    # match = re.match("/v2/([\w/]+)/manifests/([\w/]+)", req.path)
    # # https://registry-1.docker.io/v2/library/nginx/manifests/latest
    # if match:
    #     print("matches: ", match.groups())

    if req.path == f"/v2/{name}/manifests/latest":
        print(data.manifest_list, end="\n\n")
        return web.json_response(
            data.manifest_list,
            content_type="application/vnd.docker.distribution.manifest.list.v2+json",
        )
    if req.path == f"/v2/{name}/manifests/{mf_digest}":
        print(data.manifest, end="\n\n")
        return web.json_response(
            data.manifest,
            content_type="application/vnd.docker.distribution.manifest.v2+json",
        )
    if req.path == f"/v2/{name}/blobs/{cfg_digest}":
        print(data.config)
        return web.json_response(data.config, content_type="application/vnd.docker.container.image.v1+json")
    if req.path == f"/v2/{name}/blobs/{layer_digest}":
        print("sending blob")
        return web.FileResponse(f, headers={"Content-Type": "application/octet-stream"})
    # async with cs.get(f"https://registry-1.docker.io{req.url.relative()}", headers=req.headers) as resp:
    #     print("proxy for ", req.url.relative())

    #     body = await resp.text()
    #     if body[0] in "{[":
    #         print(body)
    #     print()
    #     return web.Response(body=body, status=resp.status, headers=resp.headers)

    url = yarl.URL(f"https://registry-1.docker.io{req.url.relative()}")
    print(url, end="\n\n")
    raise web.HTTPFound(url)


app = web.Application()
app.add_routes([web.route("*", "/{tail:.*}", handle)])
web.run_app(app, port=9090)
