.PHONY: lint
lint:
	flake8 tremendous --ignore=E302,E501,W391


.PHONY: test
test: lint
	py.test --cov tremendous -s -rxs ./tests/


.PHONY: setup
setup:
	pip install -r requirements.txt
