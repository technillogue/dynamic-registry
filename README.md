build images by adding a file on the fly by only serving the changed layer

try it:

`docker run --rm -it -p 8080:80 dynamic-registry.fly.dev/dynamic/marisa`


related material: 

- https://github.com/moby/moby/blob/master/distribution/pull_v2.go
- https://github.com/jpetazzo/registrish#how-it-works
- https://fly.io/blog/docker-without-docker/
- https://github.com/p8952/bocker
- https://nixery.dev/
