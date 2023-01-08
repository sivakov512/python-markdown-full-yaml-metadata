install:
	poetry install

install-no-dev:
	poetry install --no-dev

lint:
	poetry run flake8
	poetry run mypy ./
	poetry run black --check ./

test:
	poetry run pytest

test-with-coverage:
	poetry run pytest --cov=full_yaml_metadata

upload-coverage:
	poetry run coveralls
