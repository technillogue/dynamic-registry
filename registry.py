import hashlib
import json
import logging
import os
import re
import yarl
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


def sha256sum(f: str) -> str:
    return hashlib.sha256(open(f, "rb").read()).hexdigest()


def mktar():
    with tarfile.open("/tmp/reimu.tar.gz", "w:gz") as tar:
        info = tarfile.TarInfo(name="usr/share/nginx/html/reimu.webp")
        with open("/home/sylv/misc/registry-302/test/reimu.webp", "rb") as f:
            info.size = os.fstat(f.fileno()).st_size
            tar.addfile(info, f)
    return tar
if 1:
    f = "/tmp/reimu.tar.gz"
    layer_digest = f"sha256:{sha256sum(f)}"
    layer = {
        "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
        "size": os.stat(f).st_size,
        "digest": layer_digest,
    }
    data.manifest["layers"].append(layer)
    manifest = json.dumps(data.manifest)
    mf_digest = "sha256:" + hashlib.sha256(manifest.encode()).hexdigest()
    data.manifest_list["manifests"][0]= {
      "digest": mf_digest,
      "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
      "platform": {
        "architecture": "amd64",
        "os": "linux"
      },
      "size": len(manifest)
    }
    print(mf_digest)
    name = "dyn/reimu"
else:
    mf_digest = "sha256:3f01b0094e21f7d55b9eb7179d01c49fdf9c3e1e3419d315b81a9e0bae1b6a90"
    name = "library/nginx"


async def handle(req: web.Request) -> web.Response:
    print("\n=======new request=======")
    print(req)
    print(req.path)
    match = re.match("/v2/([\w/]+)/manifests/([\w/]+)", req.path)
    # https://registry-1.docker.io/v2/library/nginx/manifests/latest
    if match:
        print("matches: ", match.groups())

    if req.path == "/v2/dyn/reimu/manifests/latest":
        print(data.manifest_list)
        return web.json_response(data.manifest_list, content_type="application/vnd.docker.distribution.manifest.list.v2+json")
    if req.path == f"/v2/dyn/reimu/manifests/{mf_digest}":
        print(data.manifest)
        return web.json_response(data.manifest, content_type="application/vnd.docker.distribution.manifest.v2+json")
    # if req.path == f"/v2/dyn/reimu/blobs/{layer_digest}":
    #     return web.FileResponse(f)
    url = yarl.URL(f"https://registry-1.docker.io{req.url.relative()}")
    print(url)
    raise web.HTTPFound(url)


app = web.Application()
app.add_routes([web.route("*", "/{tail:.*}", handle)])
web.run_app(app)
