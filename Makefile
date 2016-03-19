default:

clean:
	@cd src/ && make clean
	@cd docs/ && make clean

docker-build-master:
	@cd build/master && make build-master

docker-build-masterdev:
	@cd build/master && make build-masterdev

.PHONY: default clean docker-build-master docker-build-masterdev dia-png-export
