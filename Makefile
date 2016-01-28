default:

clean:
	find src/ -type d -name __pycache__ | xargs rm -rf

build-master:
	docker build -t tsadm/master build/master/

run-master:
	docker run -it --rm --user $(shell id -u):$(shell id -g) -v $(PWD)/src:/opt/tsadm/django -p 8000:8000 tsadm/master

.PHONY: default clean build-master run-master
