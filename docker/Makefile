include ../mk/env.mk

.PHONY: default
default:

.PHONY: run-master
run-master:
	@test -d $(PWD)/../../webapp
	@test -d $(PWD)/../../ansible
	@docker run -it --rm --user $(shell id -u):$(shell id -g) \
		-v $(PWD)/../../webapp:/opt/tsadm/webapp \
		-v $(PWD)/../../ansible:/opt/tsadm/ansible \
		-p 8000:8000 \
		-e TSADM_LOG=$(TSADM_LOG) \
		$(DOCKER_IMG) $(DOCKER_CMD)

.PHONY: run-masterdev
run-masterdev:
	@make -s run-master DOCKER_IMG=tsadm/masterdev TSADM_LOG=debug \
		DOCKER_CMD=/bin/bash

.PHONY: run-tests
run-tests:
	@make -s run-master DOCKER_IMG=tsadm/masterdev TSADM_LOG=off \
		DOCKER_CMD='make -C src tests'

.PHONY: build-master
build-master:
	@docker pull debian:stable
	@docker build -t tsadm/master master

.PHONY: build-masterdev
build-masterdev:
	@docker build -f master/Dockerfile.dev -t tsadm/masterdev master

.PHONY: sulogin
sulogin:
	@docker run -it --rm --user 0:0 $(DOCKER_IMG) /bin/bash
