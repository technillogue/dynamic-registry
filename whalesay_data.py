base_image = "technillogue/whalesay"
base_tag = "latest"

true, false, null = True, False, None

manifest_list = {
    "manifests": [{}],
    "mediaType": "application/vnd.docker.distribution.manifest.list.v2+json",
    "schemaVersion": 2,
}

manifest = {
    "schemaVersion": 2,
    "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
    "config": {
        "mediaType": "application/vnd.docker.container.image.v1+json",
        "size": 4660,
        "digest": "sha256:cbea99e2c0150e7279b86c46ba67a2853934442f15b00323ebd4f31eeaddffb5",
    },
    "layers": [
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 65771329,
            "digest": "sha256:e190868d63f8f8b85b026e53b5724c3c2a4548e1d642953442559cfa5f79b2c9",
        },
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 71482,
            "digest": "sha256:909cd34c6fd77d398af1d93e9d4f7f76104903f237be3d4db7b345a19631f291",
        },
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 682,
            "digest": "sha256:0b9bfabab7c119abe303f22a146ff78be4ab0abdc798b0a0e97e94e80238a7e8",
        },
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 32,
            "digest": "sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4",
        },
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 37711437,
            "digest": "sha256:00bf65475aba8f1077fa9629f088a5f531d645faeccb6acd7a8626c7d896a4c4",
        },
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 61679,
            "digest": "sha256:c57b6bcc83e3e88fb3748ea3f0cb13d77c4e2ffa7b9a8ded3d636f17d2d83759",
        },
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 32,
            "digest": "sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4",
        },
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 18323,
            "digest": "sha256:8978f6879e2f86eb7a063e70f7d89feecde9950c40fc68f1f53d00b3c8ce9b52",
        },
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 11615,
            "digest": "sha256:8eed3712d2cfd8c37b19d324452ba9cdb445933c04c9175c4e945b0d7241f1e3",
        },
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 32,
            "digest": "sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4",
        },
        {
            "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "size": 128,
            "digest": "sha256:64ef2e0e29af552096ab9fab54b4c875344e80d299c6dacc1449d6eb74ad290a",
        },
    ],
}

base_digests = [layer["digest"] for layer in manifest["layers"]]

config = {
    "architecture": "amd64",
    "config": {
        "Hostname": "9ec8c01a6a48",
        "Domainname": "",
        "User": "",
        "AttachStdin": false,
        "AttachStdout": false,
        "AttachStderr": false,
        "Tty": false,
        "OpenStdin": false,
        "StdinOnce": false,
        "Env": [
            "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
        ],
        "Cmd": null,
        "Image": "sha256:e30c98a760e7c7dd6705a116b368134c3a429f4a7c02e59dd25686f750fe35f6",
        "Volumes": null,
        "WorkingDir": "/cowsay",
        "Entrypoint": ["/bin/bash", "/entrypoint"],
        "OnBuild": [],
        "Labels": {},
    },
    "container": "f90a29a2bfdcc4a38353580d14a2a1a822e83cf61a0f80045f6892d653d017ce",
    "container_config": {
        "Hostname": "9ec8c01a6a48",
        "Domainname": "",
        "User": "",
        "AttachStdin": false,
        "AttachStdout": false,
        "AttachStderr": false,
        "Tty": false,
        "OpenStdin": false,
        "StdinOnce": false,
        "Env": [
            "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
        ],
        "Cmd": ["/bin/sh", "-c", "#(nop) ", 'ENTRYPOINT ["/bin/bash" "/entrypoint"]'],
        "Image": "sha256:e30c98a760e7c7dd6705a116b368134c3a429f4a7c02e59dd25686f750fe35f6",
        "Volumes": null,
        "WorkingDir": "/cowsay",
        "Entrypoint": ["/bin/bash", "/entrypoint"],
        "OnBuild": [],
        "Labels": {},
    },
    "created": "2023-06-06T05:50:19.971626847Z",
    "docker_version": "20.10.5",
    "history": [
        {
            "created": "2015-04-30T21:50:10.226787491Z",
            "created_by": "/bin/sh -c #(nop) ADD file:f4d7b4b3402b5c53f266bb7fdd7e728493d9a17f9ef20c8cb1b4759b6e66b70f in /",
        },
        {
            "created": "2015-04-30T21:50:12.489225538Z",
            "created_by": "/bin/sh -c echo '#!/bin/sh' > /usr/sbin/policy-rc.d \t&& echo 'exit 101' >> /usr/sbin/policy-rc.d \t&& chmod +x /usr/sbin/policy-rc.d \t\t&& dpkg-divert --local --rename --add /sbin/initctl \t&& cp -a /usr/sbin/policy-rc.d /sbin/initctl \t&& sed -i 's/^exit.*/exit 0/' /sbin/initctl \t\t&& echo 'force-unsafe-io' > /etc/dpkg/dpkg.cfg.d/docker-apt-speedup \t\t&& echo 'DPkg::Post-Invoke { \"rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true\"; };' > /etc/apt/apt.conf.d/docker-clean \t&& echo 'APT::Update::Post-Invoke { \"rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true\"; };' >> /etc/apt/apt.conf.d/docker-clean \t&& echo 'Dir::Cache::pkgcache \"\"; Dir::Cache::srcpkgcache \"\";' >> /etc/apt/apt.conf.d/docker-clean \t\t&& echo 'Acquire::Languages \"none\";' > /etc/apt/apt.conf.d/docker-no-languages \t\t&& echo 'Acquire::GzipIndexes \"true\"; Acquire::CompressionTypes::Order:: \"gz\";' > /etc/apt/apt.conf.d/docker-gzip-indexes",
        },
        {
            "created": "2015-04-30T21:50:13.086359826Z",
            "created_by": "/bin/sh -c sed -i 's/^#\\s*\\(deb.*universe\\)$/\\1/g' /etc/apt/sources.list",
        },
        {
            "created": "2015-04-30T21:50:13.355542328Z",
            "created_by": '/bin/sh -c #(nop) CMD ["/bin/bash"]',
        },
        {
            "created": "2015-05-25T22:04:19.123469373Z",
            "created_by": "/bin/sh -c apt-get -y update && apt-get install -y git",
        },
        {
            "created": "2015-05-25T22:04:21.275907059Z",
            "created_by": "/bin/sh -c git clone https://github.com/moxiegirl/cowsay.git",
        },
        {
            "created": "2015-05-25T22:04:21.504637653Z",
            "created_by": "/bin/sh -c #(nop) WORKDIR /cowsay",
        },
        {
            "created": "2015-05-25T22:04:22.22309468Z",
            "created_by": "/bin/sh -c git reset --hard origin/master",
        },
        {
            "created": "2015-05-25T22:04:23.085038061Z",
            "created_by": "/bin/sh -c sh install.sh",
        },
        {
            "created": "2015-05-25T22:04:23.303454458Z",
            "created_by": "/bin/sh -c #(nop) ENV PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
        },
        {
            "created": "2023-06-06T05:50:19.783047375Z",
            "created_by": '/bin/sh -c echo "cat /msg.txt | cowsay" > /entrypoint',
        },
        {
            "created": "2023-06-06T05:50:19.971626847Z",
            "created_by": '/bin/sh -c #(nop)  ENTRYPOINT ["/bin/bash" "/entrypoint"]',
            "empty_layer": true,
        },
    ],
    "os": "linux",
    "rootfs": {
        "type": "layers",
        "diff_ids": [
            "sha256:1154ba695078d29ea6c4e1adb55c463959cd77509adf09710e2315827d66271a",
            "sha256:528c8710fd95f61d40b8bb8a549fa8dfa737d9b9c7c7b2ae55f745c972dddacd",
            "sha256:37ee47034d9b78f10f0c5ce3a25e6b6e58997fcadaf5f896c603a10c5f35fb31",
            "sha256:5f70bf18a086007016e948b04aed3b82103a36bea41755b6cddfaf10ace3c6ef",
            "sha256:b26122d57afa5c4a2dc8db3f986410805bc8792af3a4fa73cfde5eed0a8e5b6d",
            "sha256:091abc5148e4d32cecb5522067509d7ffc1e8ac272ff75d2775138639a6c50ca",
            "sha256:5f70bf18a086007016e948b04aed3b82103a36bea41755b6cddfaf10ace3c6ef",
            "sha256:d511ed9e12e17ab4bfc3e80ed7ce86d4aac82769b42f42b753a338ed9b8a566d",
            "sha256:d061ee1340ecc8d03ca25e6ca7f7502275f558764c1ab46bd1f37854c74c5b3f",
            "sha256:5f70bf18a086007016e948b04aed3b82103a36bea41755b6cddfaf10ace3c6ef",
            "sha256:626259b892c4571baae3c4ff9d74f93e79861ab3a6dbf32ccdaf80dfd293d4b4",
        ],
    },
}
