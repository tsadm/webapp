clean:
	@find . -type d -name __pycache__ | xargs rm -rfv

run-master:
	docker run -it --rm --user $(shell id -u):$(shell id -g) -v $(PWD):/opt/tsadm/django -p 8000:8000 tsadm/master $(DOCKER_CMD)

run-master-tests:
	docker run -it --rm --user $(shell id -u):$(shell id -g) -v $(PWD):/opt/tsadm/django tsadm/master python3 manage.py test

.PHONY: clean run-master run-master-tests
