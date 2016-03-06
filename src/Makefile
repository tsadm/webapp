clean:
	@find . -type d -name __pycache__ | xargs rm -rfv
	@find . -type f -iname '*.py[co]' | xargs rm -rfv
	@rm -rf .coverage htmlcov

run-master:
	docker run -it --rm --user $(shell id -u):$(shell id -g) -v $(PWD):/opt/tsadm/webapp -p 8000:8000 tsadm/master $(DOCKER_CMD)

run-masterdev:
	docker run -it --rm --user $(shell id -u):$(shell id -g) -v $(PWD):/opt/tsadm/webapp -p 8000:8000 tsadm/masterdev $(DOCKER_CMD)

run-tests-py2:
	docker run -it --rm --user $(shell id -u):$(shell id -g) -v $(PWD):/opt/tsadm/webapp tsadm/masterdev python2 manage.py test $(TEST_SUITE)

run-tests-py3:
	docker run -it --rm --user $(shell id -u):$(shell id -g) -v $(PWD):/opt/tsadm/webapp tsadm/masterdev python3 manage.py test $(TEST_SUITE)

run-tests: run-tests-py2 run-tests-py3

tests-coverage:
	python3-coverage run --source='.' manage.py test
	python3-coverage report
	rm -rf htmlcov && python3-coverage html

django-runserver:
	python3 manage.py runserver 0.0.0.0:8000

.PHONY: clean run-master run-masterdev run-tests-py2 run-tests-py3 run-tests tests-coverage django-runserver
