DOCKER_IMG ?= tsadm/master
DOCKER_CMD ?=
TEST_SUITE ?=
TSADM_LOG ?= off
DOCKER_UID ?= $(shell id -u)
DOCKER_GID ?= $(shell id -g)
DOCKER_USER ?= $(DOCKER_UID):$(DOCKER_GID)
DOCKER_UMASK ?= $(shell umask)
