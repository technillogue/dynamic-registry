# digest, size
manifest_list = {
    "manifests": [
        {
            "digest": "sha256:3f01b0094e21f7d55b9eb7179d01c49fdf9c3e1e3419d315b81a9e0bae1b6a90",
            "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
            "platform": {"architecture": "amd64", "os": "linux"},
            "size": 1570,
        }
    ],
    "mediaType": "application/vnd.docker.distribution.manifest.list.v2+json",
    "schemaVersion": 2,
}

manifest = {
    "schemaVersion": 2,
    "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
    "config": {
        "mediaType": "application/vnd.docker.container.image.v1+json",
        "size": 7916,
        "digest": "sha256:f9c14fe76d502861ba0939bc3189e642c02e257f06f4c0214b1f8ca329326cda",
    },
    "layers": [
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 31403586,
            "digest": "sha256:f03b40093957615593f2ed142961afb6b540507e0b47e3f7626ba5e02efbbbf1",
        },
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 25772325,
            "digest": "sha256:eed12bbd64949353649476b59d486ab4c5b84fc5ed2b2dc96384b0b892b6bf7e",
        },
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 626,
            "digest": "sha256:fa7eb8c8eee8792b8db1c0043092b817376f096e3cc8feeea623c6e00211dad1",
        },
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 955,
            "digest": "sha256:7ff3b2b12318a41d4b238b643d7fcf1fe6da400ca3e02aa61766348f90455354",
        },
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 1208,
            "digest": "sha256:0f67c7de5f2c7e0dc408ce685285419c1295f24b7a01d554517c7a72374d4aeb",
        },
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 1403,
            "digest": "sha256:831f51541d386c6d0d86f6799fcfabb48e91e9e5aea63c726240dd699179f495",
        },
    ],
}

true, false, null = True, False, None

config = {
    "architecture": "amd64",
    "config": {
        "Hostname": "",
        "Domainname": "",
        "User": "",
        "AttachStdin": False,
        "AttachStdout": False,
        "AttachStderr": False,
        "ExposedPorts": {"80/tcp": {}},
        "Tty": False,
        "OpenStdin": False,
        "StdinOnce": False,
        "Env": [
            "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
            "NGINX_VERSION=1.25.0",
            "NJS_VERSION=0.7.12",
            "PKG_RELEASE=1~bullseye",
        ],
        "Cmd": ["nginx", "-g", "daemon off;"],
        "Image": "sha256:a14a5803cbf095a0268663fe3235681c2f7fd5d0b59c242d99e7b1ebb59284f3",
        "Volumes": None,
        "WorkingDir": "",
        "Entrypoint": ["/docker-entrypoint.sh"],
        "OnBuild": None,
        "Labels": {"maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"},
        "StopSignal": "SIGQUIT",
    },
    "container": "23b0fce2f40be83daa129eacbf79b8a57c6524a7898bf3aba06e10c15b433d0d",
    "container_config": {
        "Hostname": "23b0fce2f40b",
        "Domainname": "",
        "User": "",
        "AttachStdin": False,
        "AttachStdout": False,
        "AttachStderr": False,
        "ExposedPorts": {"80/tcp": {}},
        "Tty": False,
        "OpenStdin": False,
        "StdinOnce": False,
        "Env": [
            "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
            "NGINX_VERSION=1.25.0",
            "NJS_VERSION=0.7.12",
            "PKG_RELEASE=1~bullseye",
        ],
        "Cmd": ["/bin/sh", "-c", "#(nop) ", 'CMD ["nginx" "-g" "daemon off;"]'],
        "Image": "sha256:a14a5803cbf095a0268663fe3235681c2f7fd5d0b59c242d99e7b1ebb59284f3",
        "Volumes": None,
        "WorkingDir": "",
        "Entrypoint": ["/docker-entrypoint.sh"],
        "OnBuild": None,
        "Labels": {"maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"},
        "StopSignal": "SIGQUIT",
    },
    "created": "2023-05-24T22:43:48.18207587Z",
    "docker_version": "20.10.23",
    "history": [
        {
            "created": "2023-05-23T01:20:14.056617575Z",
            "created_by": "/bin/sh -c #(nop) ADD file:88252a7f118b4d6f55dd5baf49dbcaa053c9d6172c652963c1151fa76f625e44 in / ",
        },
        {
            "created": "2023-05-23T01:20:14.397263351Z",
            "created_by": '/bin/sh -c #(nop)  CMD ["bash"]',
            "empty_layer": True,
        },
        {
            "created": "2023-05-23T08:51:20.535844201Z",
            "created_by": "/bin/sh -c #(nop)  LABEL maintainer=NGINX Docker Maintainers <docker-maint@nginx.com>",
            "empty_layer": True,
        },
        {
            "created": "2023-05-24T22:43:27.066031836Z",
            "created_by": "/bin/sh -c #(nop)  ENV NGINX_VERSION=1.25.0",
            "empty_layer": True,
        },
        {
            "created": "2023-05-24T22:43:27.145245895Z",
            "created_by": "/bin/sh -c #(nop)  ENV NJS_VERSION=0.7.12",
            "empty_layer": True,
        },
        {
            "created": "2023-05-24T22:43:27.223746092Z",
            "created_by": "/bin/sh -c #(nop)  ENV PKG_RELEASE=1~bullseye",
            "empty_layer": True,
        },
        {
            "created": "2023-05-24T22:43:47.385226096Z",
            "created_by": '/bin/sh -c set -x     && addgroup --system --gid 101 nginx     && adduser --system --disabled-login --ingroup nginx --no-create-home --home /nonexistent --gecos "nginx user" --shell /bin/false --uid 101 nginx     && apt-get update     && apt-get install --no-install-recommends --no-install-suggests -y gnupg1 ca-certificates     &&     NGINX_GPGKEY=573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62;     NGINX_GPGKEY_PATH=/usr/share/keyrings/nginx-archive-keyring.gpg;     export GNUPGHOME="$(mktemp -d)";     found=\'\';     for server in         hkp://keyserver.ubuntu.com:80         pgp.mit.edu     ; do         echo "Fetching GPG key $NGINX_GPGKEY from $server";         gpg1 --keyserver "$server" --keyserver-options timeout=10 --recv-keys "$NGINX_GPGKEY" && found=yes && break;     done;     test -z "$found" && echo >&2 "error: failed to fetch GPG key $NGINX_GPGKEY" && exit 1;     gpg1 --export "$NGINX_GPGKEY" > "$NGINX_GPGKEY_PATH" ;     rm -rf "$GNUPGHOME";     apt-get remove --purge --auto-remove -y gnupg1 && rm -rf /var/lib/apt/lists/*     && dpkgArch="$(dpkg --print-architecture)"     && nginxPackages="         nginx=${NGINX_VERSION}-${PKG_RELEASE}         nginx-module-xslt=${NGINX_VERSION}-${PKG_RELEASE}         nginx-module-geoip=${NGINX_VERSION}-${PKG_RELEASE}         nginx-module-image-filter=${NGINX_VERSION}-${PKG_RELEASE}         nginx-module-njs=${NGINX_VERSION}+${NJS_VERSION}-${PKG_RELEASE}     "     && case "$dpkgArch" in         amd64|arm64)             echo "deb [signed-by=$NGINX_GPGKEY_PATH] https://nginx.org/packages/mainline/debian/ bullseye nginx" >> /etc/apt/sources.list.d/nginx.list             && apt-get update             ;;         *)             echo "deb-src [signed-by=$NGINX_GPGKEY_PATH] https://nginx.org/packages/mainline/debian/ bullseye nginx" >> /etc/apt/sources.list.d/nginx.list                         && tempDir="$(mktemp -d)"             && chmod 777 "$tempDir"                         && savedAptMark="$(apt-mark showmanual)"                         && apt-get update             && apt-get build-dep -y $nginxPackages             && (                 cd "$tempDir"                 && DEB_BUILD_OPTIONS="nocheck parallel=$(nproc)"                     apt-get source --compile $nginxPackages             )                         && apt-mark showmanual | xargs apt-mark auto > /dev/null             && { [ -z "$savedAptMark" ] || apt-mark manual $savedAptMark; }                         && ls -lAFh "$tempDir"             && ( cd "$tempDir" && dpkg-scanpackages . > Packages )             && grep \'^Package: \' "$tempDir/Packages"             && echo "deb [ trusted=yes ] file://$tempDir ./" > /etc/apt/sources.list.d/temp.list             && apt-get -o Acquire::GzipIndexes=false update             ;;     esac         && apt-get install --no-install-recommends --no-install-suggests -y                         $nginxPackages                         gettext-base                         curl     && apt-get remove --purge --auto-remove -y && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/nginx.list         && if [ -n "$tempDir" ]; then         apt-get purge -y --auto-remove         && rm -rf "$tempDir" /etc/apt/sources.list.d/temp.list;     fi     && ln -sf /dev/stdout /var/log/nginx/access.log     && ln -sf /dev/stderr /var/log/nginx/error.log     && mkdir /docker-entrypoint.d',
        },
        {
            "created": "2023-05-24T22:43:47.610250909Z",
            "created_by": "/bin/sh -c #(nop) COPY file:7b307b62e82255f040c9812421a30090bf9abf3685f27b02d77fcca99f997911 in / ",
        },
        {
            "created": "2023-05-24T22:43:47.694925097Z",
            "created_by": "/bin/sh -c #(nop) COPY file:5c18272734349488bd0c94ec8d382c872c1a0a435cca13bd4671353d6021d2cb in /docker-entrypoint.d ",
        },
        {
            "created": "2023-05-24T22:43:47.781873513Z",
            "created_by": "/bin/sh -c #(nop) COPY file:36429cfeeb299f9913b84ea136b004be12fbe4bb4f975a977a3608044e8bfa91 in /docker-entrypoint.d ",
        },
        {
            "created": "2023-05-24T22:43:47.867772264Z",
            "created_by": "/bin/sh -c #(nop) COPY file:e57eef017a414ca793499729d80a7b9075790c9a804f930f1417e56d506970cf in /docker-entrypoint.d ",
        },
        {
            "created": "2023-05-24T22:43:47.943753697Z",
            "created_by": '/bin/sh -c #(nop)  ENTRYPOINT ["/docker-entrypoint.sh"]',
            "empty_layer": True,
        },
        {
            "created": "2023-05-24T22:43:48.024969965Z",
            "created_by": "/bin/sh -c #(nop)  EXPOSE 80",
            "empty_layer": True,
        },
        {
            "created": "2023-05-24T22:43:48.10402457Z",
            "created_by": "/bin/sh -c #(nop)  STOPSIGNAL SIGQUIT",
            "empty_layer": True,
        },
        {
            "created": "2023-05-24T22:43:48.18207587Z",
            "created_by": '/bin/sh -c #(nop)  CMD ["nginx" "-g" "daemon off;"]',
            "empty_layer": True,
        },
    ],
    "os": "linux",
    "rootfs": {
        "type": "layers",
        "diff_ids": [
            "sha256:8cbe4b54fa88d8fc0198ea0cc3a5432aea41573e6a0ee26eca8c79f9fbfa40e3",
            "sha256:4b8862fe7056d8a3c2c0910eb38ebb8fc08785eaa1f9f53b2043bf7ca8adbafb",
            "sha256:e60266289ce4a890aaf52b93228090998e28220aef04f128704141864992dd15",
            "sha256:7daac92f43be84ad9675f94875c1a00357b975d6c58b11d17104e0a0e04da370",
            "sha256:5e099cf3f3c83c449b8c062f944ac025c9bf2dd7ec255837c53430021f5a1517",
            "sha256:4fd83434130318dede62defafcc5853d03dae8636eccfa1b9dcd385d92e3ff19",
        ],
    },
}
