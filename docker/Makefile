include ../mk/env.mk

.PHONY: default
default:

.PHONY: run-master
run-master:
	@test -d $(PWD)/../src
	@test -d $(PWD)/../../ansible
	@docker run -it --rm --user $(shell id -u):$(shell id -g) \
		-v $(PWD)/../src:/opt/tsadm/webapp \
		-v $(PWD)/../../ansible:/opt/tsadm/ansible \
		-p 8000:8000 \
		-e TSADM_LOG=$(TSADM_LOG) \
		$(DOCKER_IMG) $(DOCKER_CMD)

.PHONY: run-masterdev
run-masterdev:
	make run-master DOCKER_IMG=tsadm/masterdev TSADM_LOG=debug

.PHONY: run-tests-py2
run-tests-py2:
	make run-master DOCKER_CMD='python2 manage.py test $(TEST_SUITE)' \
		DOCKER_IMG=tsadm/masterdev

.PHONY: run-tests-py3
run-tests-py3:
	make run-master DOCKER_CMD='python3 manage.py test $(TEST_SUITE)'

.PHONY: run-tests
run-tests: run-tests-py2 run-tests-py3

.PHONY: build-master
build-master:
	docker pull debian:stable
	docker build -t tsadm/master master

.PHONY: build-masterdev
build-masterdev:
	docker build -f master/Dockerfile.dev -t tsadm/masterdev master

.PHONY: sulogin
sulogin:
	docker run -it --rm --user 0:0 $(DOCKER_IMG) /bin/bash
