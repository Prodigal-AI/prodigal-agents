.PHONY: install fmt lint test

install:
	poetry install

fmt:
	poetry run black src

lint:
	poetry run flake8 src

test:
	poetry run pytest
