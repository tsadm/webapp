include ../mk/env.mk

.PHONY: default
default:

.PHONY: run-master
run-master:
	@test -d $(PWD)/../../webapp
	@test -d $(PWD)/../../ansible
	@docker run -it --rm --user $(DOCKER_USER) \
		-v $(PWD)/../../webapp:/opt/tsadm/webapp \
		-v $(PWD)/../../ansible:/opt/tsadm/ansible \
		-p 8000:8000 \
		-e TSADM_LOG=$(TSADM_LOG) \
		-e DOCKER_UID=$(DOCKER_UID) \
		-e DOCKER_GID=$(DOCKER_GID) \
		-e DOCKER_UMASK=$(DOCKER_UMASK) \
		$(DOCKER_IMG) $(DOCKER_CMD)

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

.PHONY: devlogin
devlogin:
	@make -s run-master DOCKER_IMG=tsadm/masterdev TSADM_LOG=debug \
		DOCKER_USER=0:0 \
		DOCKER_CMD=/root/devlogin.sh

.PHONY: sulogin
sulogin:
	@docker run -it --rm --user 0:0 $(DOCKER_IMG) /bin/bash
