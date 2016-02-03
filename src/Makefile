TSADM_LOG ?= WARNING
DOCKER_TEST_CMD ?= /opt/tsadm/webapp/manage.py test

clean:
	@find . -type d -name __pycache__ | xargs rm -rfv

run-master:
	docker run -it --rm -e TSADM_LOG=$(TSADM_LOG) --user $(shell id -u):$(shell id -g) -v $(PWD):/opt/tsadm/webapp -p 8000:8000 tsadm/master $(DOCKER_CMD)

run-master-tests:
	docker run -it --rm -e TSADM_LOG=$(TSADM_LOG) --user $(shell id -u):$(shell id -g) -v $(PWD):/opt/tsadm/webapp tsadm/master $(DOCKER_TEST_CMD) $(TEST_SUITE)

.PHONY: clean run-master run-master-tests
