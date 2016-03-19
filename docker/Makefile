include ../mk/env.mk

.PHONY: default
default:

.PHONY: run-master
run-master:
	@test -d $(PWD)/../../webapp
	@test -d $(PWD)/../../ansible
	@docker run -it --rm \
		--name $(DOCKER_MASTER_NAME) \
		--hostname $(DOCKER_MASTER_NAME) \
		-v $(PWD)/../../webapp:/opt/tsadm/webapp \
		-v $(PWD)/../../ansible:/opt/tsadm/ansible \
		$(DOCKER_ARGS) \
		-e TSADM_LOG=$(TSADM_LOG) \
		-e DOCKER_UID=$(DOCKER_UID) \
		-e DOCKER_GID=$(DOCKER_GID) \
		-e DOCKER_UMASK=$(DOCKER_UMASK) \
		$(DOCKER_IMG) $(DOCKER_CMD)

.PHONY: run-tests
run-tests:
	@make -s run-master DOCKER_IMG=$(DOCKER_IMG) TSADM_LOG=off \
		DOCKER_ARGS='-w /opt/tsadm/webapp/src' \
		DOCKER_CMD='python3 manage.py test'

.PHONY: build-master
build-master:
	@docker pull debian:stable
	@docker build -t $(DOCKER_IMG) master

.PHONY: build-masterdev
build-masterdev:
	@docker build -t $(DOCKER_DEVIMG) masterdev 

.PHONY: devlogin
devlogin:
	@make -s run-master DOCKER_IMG=$(DOCKER_DEVIMG) TSADM_LOG=debug \
		DOCKER_ARGS='-p 8000:8000' \
		DOCKER_CMD=/root/devlogin.sh
