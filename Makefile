install:
	poetry install
gendiff:
	poetry run gendiff -h

gentest1:
	poetry run gendiff tests/fixtures/test01.json tests/fixtures/test02.json

gentest2:
	poetry run gendiff tests/fixtures/test11.json tests/fixtures/test12.json

gentest3:
	poetry run gendiff tests/fixtures/test21.yml tests/fixtures/test22.yaml

gentest4:
	poetry run gendiff tests/fixtures/test31.yml tests/fixtures/test32.yaml

gentest5:
	poetry run gendiff tests/fixtures/test01.json tests/fixtures/test02.json -f plain

gentest6:
	poetry run gendiff tests/fixtures/test11.json tests/fixtures/test12.json -f plain

gentest7:
	poetry run gendiff tests/fixtures/test21.yml tests/fixtures/test22.yaml -f plain

gentest8:
	poetry run gendiff tests/fixtures/test31.yml tests/fixtures/test32.yaml -f plain

gentest9:
	poetry run gendiff tests/fixtures/test11.json tests/fixtures/test32.yaml -f plain

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
