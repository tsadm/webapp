TSADM_LOG ?= OFF

clean:
	@find . -type d -name __pycache__ | xargs rm -rfv
	@find . -type f -iname '*.py[co]' | xargs rm -rfv

run-master:
	docker run -it --rm -e TSADM_LOG=$(TSADM_LOG) --user $(shell id -u):$(shell id -g) -v $(PWD):/opt/tsadm/webapp -p 8000:8000 tsadm/master $(DOCKER_CMD)

run-masterdev:
	docker run -it --rm -e TSADM_LOG=$(TSADM_LOG) --user $(shell id -u):$(shell id -g) -v $(PWD):/opt/tsadm/webapp -p 8000:8000 tsadm/masterdev $(DOCKER_CMD)

run-tests-py2:
	docker run -it --rm -e TSADM_LOG=$(TSADM_LOG) --user $(shell id -u):$(shell id -g) -v $(PWD):/opt/tsadm/webapp tsadm/masterdev python2 manage.py test $(TEST_SUITE)

run-tests-py3:
	docker run -it --rm -e TSADM_LOG=$(TSADM_LOG) --user $(shell id -u):$(shell id -g) -v $(PWD):/opt/tsadm/webapp tsadm/masterdev python3 manage.py test $(TEST_SUITE)

run-tests: run-tests-py2 run-tests-py3

.PHONY: clean run-master run-masterdev run-tests-py2 run-tests-py3 run-tests
