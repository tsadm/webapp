default:

clean:
	@cd src/ && make clean

docker-build-master:
	docker build -t tsadm/master build/master/

dia-png-export:
	@cd docs/dia && make png-export

travis-test:
	@cd src/ && make run-master-tests TSADM_LOG=OFF DOCKER_TEST_CMD="python /opt/tsadm/webapp/manage.py test"

.PHONY: default clean docker-build-master dia-png-export travis-test
