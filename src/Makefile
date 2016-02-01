clean:
	@find . -type d -name __pycache__ | xargs rm -rfv

run-master:
	docker run -it --rm --user $(shell id -u):$(shell id -g) -v $(PWD):/opt/tsadm/django -p 8000:8000 tsadm/master $(DOCKER_CMD)

.PHONY: clean run-master
