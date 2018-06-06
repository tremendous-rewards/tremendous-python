.PHONY: lint
lint:
	flake8 tremendous


.PHONY: test
test: lint
	py.test --cov tremendous -s -rxs ./tests/


.PHONY: setup
setup:
	pip install -r requirements.txt
