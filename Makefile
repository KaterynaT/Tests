export NOSE_INIT_MODULE=tests.nose_init
export PYTHONPATH=.
export TZ=UTC

build:
	$(NOOP)

test:
	python setup.py test

coverage:
	coverage run --concurrency=gevent --source=progs setup.py test

lint:
	flake8 progs --ignore=E123,E126,E128,E265,E501

clean:
	python setup.py clean
	find . -name '*.py[co]' -delete
	rm -rf build/ dist/ *.egg progs.egg-info

.PHONY:	test lint clean coverage


