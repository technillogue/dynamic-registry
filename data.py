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
        "digest": "sha256:448a08f1d2f94e8db6db9286fd77a3a4f3712786583720a12f1648abb8cace25",
    },
    "layers": [
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 31403516,
            "digest": "sha256:9e3ea8720c6de96cc9ad544dddc695a3ab73f5581c5d954e0504cc4f80fb5e5c",
        },
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 25584344,
            "digest": "sha256:bf36b64666794f28ea5c3d4d75add149c04e849342e3d45ca31aac9cf4715dd1",
        },
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 626,
            "digest": "sha256:15a97cf85bb88997d139f86b2be23f99175d51d7e45a4c4b04ec0cbdbb56a63b",
        },
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 958,
            "digest": "sha256:9c2d6be5a61d1ad44be8e5e93a5800572cff95601147c45eaa9ecf0d4cb66f83",
        },
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 773,
            "digest": "sha256:6b7e4a5c7c7ad54c76bc4861f476f3b70978beede9e752015202dd223383602b",
        },
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 1403,
            "digest": "sha256:8db4caa19df89c606d39076b27fe163e1f37516f889ff5bfee1fce03056bb6b0",
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
        "AttachStdin": false,
        "AttachStdout": false,
        "AttachStderr": false,
        "ExposedPorts": {"80/tcp": {}},
        "Tty": false,
        "OpenStdin": false,
        "StdinOnce": false,
        "Env": [
            "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
            "NGINX_VERSION=1.23.4",
            "NJS_VERSION=0.7.11",
            "PKG_RELEASE=1~bullseye",
        ],
        "Cmd": ["nginx", "-g", "daemon off;"],
        "Image": "sha256:3a939c4944ef49bcf282f201919718dc414fd79c7761fe46ed6cdad1ac2d6564",
        "Volumes": null,
        "WorkingDir": "",
        "Entrypoint": ["/docker-entrypoint.sh"],
        "OnBuild": null,
        "Labels": {"maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"},
        "StopSignal": "SIGQUIT",
    },
    "container": "a4589847511fc5545db6600740abeb1c991a29ecf9a4b1e3d9b74ae565d373a5",
    "container_config": {
        "Hostname": "a4589847511f",
        "Domainname": "",
        "User": "",
        "AttachStdin": false,
        "AttachStdout": false,
        "AttachStderr": false,
        "ExposedPorts": {"80/tcp": {}},
        "Tty": false,
        "OpenStdin": false,
        "StdinOnce": false,
        "Env": [
            "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
            "NGINX_VERSION=1.23.4",
            "NJS_VERSION=0.7.11",
            "PKG_RELEASE=1~bullseye",
        ],
        "Cmd": ["/bin/sh", "-c", "#(nop) ", 'CMD ["nginx" "-g" "daemon off;"]'],
        "Image": "sha256:3a939c4944ef49bcf282f201919718dc414fd79c7761fe46ed6cdad1ac2d6564",
        "Volumes": null,
        "WorkingDir": "",
        "Entrypoint": ["/docker-entrypoint.sh"],
        "OnBuild": None,
        "Labels": {"maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"},
        "StopSignal": "SIGQUIT",
    },
    "created": "2023-05-03T19:51:06.214253945Z",
    "docker_version": "20.10.23",
    "history": [
        {
            "created": "2023-05-02T23:46:59.831699727Z",
            "created_by": "/bin/sh -c #(nop) ADD file:a2378c1b12e95db69e24b9d347441678c6f23239292cce3c822b1524992b6ec4 in / ",
        },
        {
            "created": "2023-05-02T23:47:00.1128963Z",
            "created_by": '/bin/sh -c #(nop)  CMD ["bash"]',
            "empty_layer": True,
        },
        {
            "created": "2023-05-03T19:50:47.862144405Z",
            "created_by": "/bin/sh -c #(nop)  LABEL maintainer=NGINX Docker Maintainers <docker-maint@nginx.com>",
            "empty_layer": True,
        },
        {
            "created": "2023-05-03T19:50:47.939315234Z",
            "created_by": "/bin/sh -c #(nop)  ENV NGINX_VERSION=1.23.4",
            "empty_layer": True,
        },
        {
            "created": "2023-05-03T19:50:48.020227271Z",
            "created_by": "/bin/sh -c #(nop)  ENV NJS_VERSION=0.7.11",
            "empty_layer": True,
        },
        {
            "created": "2023-05-03T19:50:48.097124251Z",
            "created_by": "/bin/sh -c #(nop)  ENV PKG_RELEASE=1~bullseye",
            "empty_layer": True,
        },
        {
            "created": "2023-05-03T19:51:05.443923646Z",
            "created_by": '/bin/sh -c set -x     && addgroup --system --gid 101 nginx     && adduser --system --disabled-login --ingroup nginx --no-create-home --home /nonexistent --gecos "nginx user" --shell /bin/false --uid 101 nginx     && apt-get update     && apt-get install --no-install-recommends --no-install-suggests -y gnupg1 ca-certificates     &&     NGINX_GPGKEY=573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62;     NGINX_GPGKEY_PATH=/usr/share/keyrings/nginx-archive-keyring.gpg;     export GNUPGHOME="$(mktemp -d)";     found=\'\';     for server in         hkp://keyserver.ubuntu.com:80         pgp.mit.edu     ; do         echo "Fetching GPG key $NGINX_GPGKEY from $server";         gpg1 --keyserver "$server" --keyserver-options timeout=10 --recv-keys "$NGINX_GPGKEY" && found=yes && break;     done;     test -z "$found" && echo >&2 "error: failed to fetch GPG key $NGINX_GPGKEY" && exit 1;     gpg1 --export "$NGINX_GPGKEY" > "$NGINX_GPGKEY_PATH" ;     rm -rf "$GNUPGHOME";     apt-get remove --purge --auto-remove -y gnupg1 && rm -rf /var/lib/apt/lists/*     && dpkgArch="$(dpkg --print-architecture)"     && nginxPackages="         nginx=${NGINX_VERSION}-${PKG_RELEASE}         nginx-module-xslt=${NGINX_VERSION}-${PKG_RELEASE}         nginx-module-geoip=${NGINX_VERSION}-${PKG_RELEASE}         nginx-module-image-filter=${NGINX_VERSION}-${PKG_RELEASE}         nginx-module-njs=${NGINX_VERSION}+${NJS_VERSION}-${PKG_RELEASE}     "     && case "$dpkgArch" in         amd64|arm64)             echo "deb [signed-by=$NGINX_GPGKEY_PATH] https://nginx.org/packages/mainline/debian/ bullseye nginx" >> /etc/apt/sources.list.d/nginx.list             && apt-get update             ;;         *)             echo "deb-src [signed-by=$NGINX_GPGKEY_PATH] https://nginx.org/packages/mainline/debian/ bullseye nginx" >> /etc/apt/sources.list.d/nginx.list                         && tempDir="$(mktemp -d)"             && chmod 777 "$tempDir"                         && savedAptMark="$(apt-mark showmanual)"                         && apt-get update             && apt-get build-dep -y $nginxPackages             && (                 cd "$tempDir"                 && DEB_BUILD_OPTIONS="nocheck parallel=$(nproc)"                     apt-get source --compile $nginxPackages             )                         && apt-mark showmanual | xargs apt-mark auto > /dev/null             && { [ -z "$savedAptMark" ] || apt-mark manual $savedAptMark; }                         && ls -lAFh "$tempDir"             && ( cd "$tempDir" && dpkg-scanpackages . > Packages )             && grep \'^Package: \' "$tempDir/Packages"             && echo "deb [ trusted=yes ] file://$tempDir ./" > /etc/apt/sources.list.d/temp.list             && apt-get -o Acquire::GzipIndexes=false update             ;;     esac         && apt-get install --no-install-recommends --no-install-suggests -y                         $nginxPackages                         gettext-base                         curl     && apt-get remove --purge --auto-remove -y && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/nginx.list         && if [ -n "$tempDir" ]; then         apt-get purge -y --auto-remove         && rm -rf "$tempDir" /etc/apt/sources.list.d/temp.list;     fi     && ln -sf /dev/stdout /var/log/nginx/access.log     && ln -sf /dev/stderr /var/log/nginx/error.log     && mkdir /docker-entrypoint.d',
        },
        {
            "created": "2023-05-03T19:51:05.651432117Z",
            "created_by": "/bin/sh -c #(nop) COPY file:7b307b62e82255f040c9812421a30090bf9abf3685f27b02d77fcca99f997911 in / ",
        },
        {
            "created": "2023-05-03T19:51:05.73780747Z",
            "created_by": "/bin/sh -c #(nop) COPY file:5c18272734349488bd0c94ec8d382c872c1a0a435cca13bd4671353d6021d2cb in /docker-entrypoint.d ",
        },
        {
            "created": "2023-05-03T19:51:05.821337624Z",
            "created_by": "/bin/sh -c #(nop) COPY file:abbcbf84dc17ee4454b6b2e3cf914be88e02cf84d344ec45a5b31235379d722a in /docker-entrypoint.d ",
        },
        {
            "created": "2023-05-03T19:51:05.906294486Z",
            "created_by": "/bin/sh -c #(nop) COPY file:e57eef017a414ca793499729d80a7b9075790c9a804f930f1417e56d506970cf in /docker-entrypoint.d ",
        },
        {
            "created": "2023-05-03T19:51:05.979700896Z",
            "created_by": '/bin/sh -c #(nop)  ENTRYPOINT ["/docker-entrypoint.sh"]',
            "empty_layer": True,
        },
        {
            "created": "2023-05-03T19:51:06.058893465Z",
            "created_by": "/bin/sh -c #(nop)  EXPOSE 80",
            "empty_layer": True,
        },
        {
            "created": "2023-05-03T19:51:06.138099974Z",
            "created_by": "/bin/sh -c #(nop)  STOPSIGNAL SIGQUIT",
            "empty_layer": True,
        },
        {
            "created": "2023-05-03T19:51:06.214253945Z",
            "created_by": '/bin/sh -c #(nop)  CMD ["nginx" "-g" "daemon off;"]',
            "empty_layer": True,
        },
    ],
    "os": "linux",
    "rootfs": {
        "type": "layers",
        "diff_ids": [
            "sha256:8553b91047dad45bedc292812586f1621e0a464a09a7a7c2ce6ac5f8ba2535d7",
            "sha256:a29cc9587af6488ae0cbb962ecbe023d347908cc62ca5d715af06e54ccaa9e36",
            "sha256:6bc8ae8fb3cf0909b3d9c2e74f6cabe16e6a2322c52cec76fbaecaef47006f1d",
            "sha256:5684be535bf11cb9ad1a57b51085f36d84ae8361eabc2b4c2ba9a83e8b084b20",
            "sha256:93ee76f39c974e4f819e632149c002d6f509aadc5995ec6523a96b337751c8ed",
            "sha256:1040838fe30e6f26d31bde96c514f47ee4bf727b3f1c3c7b045ea3891c1c2150",
        ],
    },
}
