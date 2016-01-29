default:

clean:
	@cd src/ && make clean

build-master:
	docker build -t tsadm/master build/master/

run-master:
	docker run -it --rm --user $(shell id -u):$(shell id -g) -v $(PWD)/src:/opt/tsadm/django -p 8000:8000 tsadm/master $(DOCKER_CMD)

dia-png-export:
	@cd docs/dia && make png-export

.PHONY: default clean build-master run-master dia-png-export
