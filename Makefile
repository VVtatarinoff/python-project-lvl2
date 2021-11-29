install:
	poetry install
gendiff:
	poetry run gendiff -h

gentest:
	poetry run gendiff file1.json file2.json

tests:
	poetry run pytest -v

coverage:
	poetry run pytest --cov=gendiff

build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
package-uninstall:
	python3 -m pip uninstall hexlet-code
lint:
	poetry run flake8 gendiff
.PHONY: install gendiff build publish package-install tests coverage gentest
