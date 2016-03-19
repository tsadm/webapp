include ../mk/env.mk

.PHONY: clean
clean:
	@find . -type d -name __pycache__ | xargs rm -rfv
	@find . -type f -iname '*.py[co]' | xargs rm -rfv
	@rm -rf .coverage htmlcov

.PHONY: tests
tests:
	@python3 manage.py test $(TEST_SUITE)

.PHONY: tests-coverage
tests-coverage:
	TSADM_LOG=off python3-coverage run --source='.' manage.py test
	python3-coverage report
	rm -rf htmlcov && python3-coverage html

.PHONY: django-runserver
django-runserver:
	python3 manage.py runserver 0.0.0.0:8000

.PHONY: develdb
develdb:
	python3 manage.py migrate
	python3 manage.py loaddata testdata
