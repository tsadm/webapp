DOCKER_IMG ?= tsadm/master
DOCKER_CMD ?= /bin/bash

default:

build-master:
	docker pull debian:stable
	docker build -t tsadm/master .

build-masterdev:
	docker build -f Dockerfile.dev -t tsadm/masterdev .

sulogin:
	docker run -it --rm --user 0:0 $(DOCKER_IMG) $(DOCKER_CMD)

.PHONY: default build-master build-masterdev
