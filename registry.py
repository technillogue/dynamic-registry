import datetime
import io
import gzip
import hashlib
import json
import logging
import os
import tarfile
import typing as t
from copy import deepcopy
from dataclasses import dataclass
import aiohttp
from aiohttp import web

import data

logging.getLogger().setLevel("DEBUG")
conf = """http {
    server {
        listen 80;

        location / {
            root /usr/share/nginx/html;
            try_files /index.html =404;
        }
    }
}"""


def mktar(image_path: str, layer_path: str) -> None:
    basename = os.path.basename(image_path)
    basepath = "usr/share/nginx/html"
    with tarfile.open(layer_path, "w:gz") as tar:
        index_info = tarfile.TarInfo(f"{basepath}/index.html")
        index = f'<!DOCTYPE html><img src="{basename}">'.encode()
        index_info.size = len(index)
        tar.addfile(index_info, io.BytesIO(index))
        conf_info = tarfile.TarInfo(f"/etc/nginx.conf")
        conf_info.size = len(conf)
        tar.addfile(conf_info, io.BytesIO(conf.encode()))
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
    manifest_list_str = json.dumps(manifest_list)

    return Image(
        f"dynamic/{name}",
        # f"technillogue/{name}",
        cfg=config_str,
        cfg_digest=config_digest,
        manifest=manifest_str,
        manifest_digest=manifest_digest,
        manifest_list=manifest_list_str,
        layer_fname=layer_fname,
        layer_digest=layer_digest,
    )


marisa = make_image("images/marisa.png")
reimu = make_image("images/reimu.webp")
images = {marisa.name: marisa, reimu.name: reimu}
base_image = "library/nginx"
base_tag = "1.25.0-bullseye"
base_layer_digests = [layer["digest"] for layer in data.manifest["layers"]]

# auth_url='https://auth.docker.io'
# svc_url='registry.docker.io'
# curl -fsSL "${auth_url}/token?service=${svc_url}&scope=repository:${image}:pull" | jq --raw-output .token
# curl -fsSL -o "$file" \
#     -H "Authorization: Bearer $1" \
#       "${registry_url}/v2/${image}/blobs/${digest}"


async def get_token(cs: aiohttp.ClientSession) -> str:
    auth_url = f"https://auth.docker.io/token?service=registry.docker.io&scope=repository:{base_image}:pull"
    resp = await cs.get(auth_url)
    #print("token resp", resp)
    return (await resp.json())["token"]


def redirect(req: web.Request) -> web.Response:
    path = req.url.relative()
    url = f"https://registry-1.docker.io{path}".replace("latest", base_tag)
    # for name in images:
    #     url = url.replace(name, base_image)
    print(url)
    raise web.HTTPTemporaryRedirect(url)


def get_image(req: web.Request) -> Image:
    image = images.get(req.match_info["name"])
    if not image:
        redirect(req)
        raise Exception("unreachable")
    return image


async def manifest_route(req: web.Request) -> web.Response:
    print(req)
    image = get_image(req)
    if req.match_info["digest"] == image.manifest_digest:
        print(image.manifest, end="\n\n")
        return web.Response(
            text=image.manifest,
            content_type="application/vnd.docker.distribution.manifest.v2+json",
        )
    # just going to pretend latest is the only tag
    if req.method == "HEAD":
        print("sending Docker-Content-Digest", image.manifest_digest, end="\n\n")
        return web.Response(
            headers={
                "Docker-Content-Digest": image.manifest_digest,
                "Content-Length": str(len(image.manifest)),
            }
        )
    # it seems like if HEAD doesn't return Docker-Content-Digest, it's expected to return the manifest
    # docker hashes whatever it is and uses that as the digest
    # if it tries to hash the manifest list and use that as a digest instead of the manifest digest, that won't work

    # however, the actual docker registry returns the manifest list at this endpoint
    print(image.manifest_list)
    return web.Response(
        text=image.manifest_list,
        content_type="application/vnd.docker.distribution.manifest.list.v2+json",
    )


tracing = False


async def blob_route(req: web.Request) -> web.StreamResponse:
    print(req)
    digest = req.match_info["digest"]
    image = get_image(req)
    if digest == image.cfg_digest:
        print(image.cfg, end="\n\n")
        return web.Response(
            text=image.cfg,
            content_type="application/vnd.docker.container.image.v1+json",
        )
    if digest == image.layer_digest:
        print("sending layer blob\n")
        return web.FileResponse(
            image.layer_fname, headers={"Content-Type": "application/octet-stream"}
        )
    if digest not in base_layer_digests:
        # uncertain about this
        raise web.HTTPNotFound()
    cs: aiohttp.ClientSession = req.app["cs"]
    token = await get_token(cs)
    resp = await cs.get(
        f"https://registry-1.docker.io/v2/{base_image}/blobs/{digest}",
        headers={"Authorization": f"Bearer {token}"},
        allow_redirects=False,
    )
    print(resp)
    # if "Location" not in resp.headers:
    #     global tracing
    #     if not tracing:
    #         tracing = True
    #         import pdb
    #         pdb.set_trace()
    # hopefully this is the cloudflare
    print("passing through redirect to", resp.headers["Location"])
    raise web.HTTPTemporaryRedirect(
        resp.headers["Location"], headers=dict(resp.headers)
    )
    # return redirect(req)


async def default_redirect(req: web.Request) -> web.Response:
    return redirect(req)


async def client_session(app: web.Application) -> "t.AsyncIterator[None]":
    app["cs"] = cs = aiohttp.ClientSession()
    # app["token"] = await get_token(cs)
    yield
    await cs.close()


app = web.Application()
app.cleanup_ctx.append(client_session)
app.add_routes(
    [
        web.route("*", "/v2/{name:.+}/manifests/{digest}", manifest_route),
        web.route("*", "/v2/{name:.+}/blobs/{digest}", blob_route),
        web.route("*", "/{tail:.*}", default_redirect),
    ]
)
web.run_app(app, port=9090)
