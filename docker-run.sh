#!/bin/bash 
set -o xtrace
image="${1:-docker/whalesay}"
tag="${2:-latest}"

registry_url='https://registry-1.docker.io'
#registry_url='localhost:8080'
auth_url='https://auth.docker.io'
svc_url='registry.docker.io'
store="/tmp"

function auth_token { 
  curl -fsSL "${auth_url}/token?service=${svc_url}&scope=repository:${image}:pull" | jq --raw-output .token
}

function manifest { 
  image="$2"
  digest="${3:-latest}"

  curl -fvSL \
    -H "Authorization: Bearer $1" \
    -H 'Accept: application/vnd.docker.distribution.manifest.list.v2+json' \
    -H 'Accept: application/vnd.docker.distribution.manifest.v1+json' \
    -H 'Accept: application/vnd.docker.distribution.manifest.v2+json' \
      "${registry_url}/v2/${image}/manifests/${digest}"
}

verbose=true

function blob {
  image="$2"
  digest="$3"
  file="$4"
  if $verbose; then
      curl -fvSL -o "$file" \
          -H "Authorization: Bearer $1" \
            "${registry_url}/v2/${image}/blobs/${digest}"
      verbose=false
  else
      curl -fsSL -o "$file" \
          -H "Authorization: Bearer $1" \
            "${registry_url}/v2/${image}/blobs/${digest}"
  fi
}

function linux_version { 
  echo "$1" | jq --raw-output '.manifests[] | select(.platform.architecture=="amd64") | select(.platform.os=="linux") | .digest'
}

function layers { 
  echo "$1" | jq --raw-output '.layers[]?.digest // .fsLayers[].blobSum'
}

function config {
  echo "$1" | jq --raw-output '.config.digest' 
}

function entrypoint {
   jq -r '.config.Entrypoint | join(" ")' config.json
}


echo "getting token"
token=$(auth_token "$image")
#echo "getting amd64?"
tag_mf=$(manifest "$token" "$image" "$tag")
echo "$tag_mf" > /tmp/tag_manifest.json
if [ -z "$tag_mf" ]; then
    echo "couldn't get manifest"
    exit $?
fi;
amd64=$(linux_version "$tag_mf")
if [ -z "$amd64" ]; then
    echo "manifest available without platform tag, not fetching specific image id"
    mf="$tag_mf"
else
  echo "getting manifest"
  mf=$(manifest "$token" "$image" "$amd64")
  echo "$mf" > /tmp/manifest.json
fi;
echo "getting config"
blob "$token" "$image" $(config "$mf") config.json
cmd=$(entrypoint)
echo "pulling"
mkdir -p $store
for L in $(layers "$mf"); do
  if [ ! -f "$store/$L.tgz" ]; then
    blob "$token" "$image" "$L" "$store/$L.tgz" &
  fi;
done;
wait
echo "extracting layers"
for L in $(layers "$mf"); do
  tar -xf "$store/$L.tgz" -C .
done;
#rm -rf ./usr/lib/locale
#ln -s /usr/lib/locale ./usr/lib/
echo "running chroot"
chroot -S . $cmd ${@:3}
