include ../../mk/env.mk

.PHONY: default
default:

.PHONY: build-master
build-master:
	docker pull debian:stable
	docker build -t tsadm/master .

.PHONY: build-masterdev
build-masterdev:
	docker build -f Dockerfile.dev -t tsadm/masterdev .

.PHONY: sulogin
sulogin:
	docker run -it --rm --user 0:0 $(DOCKER_IMG) /bin/bash
