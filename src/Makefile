DOCKER_CMD ?=
DOCKER_IMG ?= tsadm/master
TEST_SUITE ?=
TSADM_LOG ?= off

clean:
	@find . -type d -name __pycache__ | xargs rm -rfv
	@find . -type f -iname '*.py[co]' | xargs rm -rfv
	@rm -rf .coverage htmlcov

run-master:
	docker run -it --rm --user $(shell id -u):$(shell id -g) \
		-v $(PWD):/opt/tsadm/webapp -p 8000:8000 \
		-e TSADM_LOG=$(TSADM_LOG) \
		$(DOCKER_IMG) $(DOCKER_CMD)

run-masterdev:
	make run-master DOCKER_IMG=tsadm/masterdev TSADM_LOG=debug

run-tests-py2:
	make run-master DOCKER_CMD='python2 manage.py test $(TEST_SUITE)' \
		DOCKER_IMG=tsadm/masterdev

run-tests-py3:
	make run-master DOCKER_CMD='python3 manage.py test $(TEST_SUITE)'

run-tests: run-tests-py2 run-tests-py3

tests-coverage:
	TSADM_LOG=off python3-coverage run --source='.' manage.py test
	python3-coverage report
	rm -rf htmlcov && python3-coverage html

django-runserver:
	python3 manage.py runserver 0.0.0.0:8000

develdb:
	python3 manage.py migrate
	python3 manage.py loaddata testdata

.PHONY: clean run-master run-masterdev run-tests-py2 run-tests-py3 run-tests tests-coverage django-runserver develdb
