install:
	poetry install
gendiff:
	poetry run gendiff -h

gentest1:
	poetry run gendiff gendiff/tests/fixtures/test01.json gendiff/tests/fixtures/test02.json

gentest2:
	poetry run gendiff gendiff/tests/fixtures/test11.json gendiff/tests/fixtures/test12.json

gentest3:
	poetry run gendiff gendiff/tests/fixtures/test21.yml gendiff/tests/fixtures/test22.yaml

tests:
	poetry run coverage run -m pytest -vv

coverage:
	poetry run coverage report

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
.PHONY: install gendiff build publish package-install tests coverage gentest1 gentest2 gentest3
