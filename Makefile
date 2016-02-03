default:

clean:
	@cd src/ && make clean

docker-build-master:
	docker build -t tsadm/master build/master/

dia-png-export:
	@cd docs/dia && make png-export

.PHONY: default clean docker-build-master dia-png-export
