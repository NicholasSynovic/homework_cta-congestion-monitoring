GIT_TAG := $(shell git --no-pager tag | tail -n 1)

build:
	poetry version $(GIT_TAG)
	poetry version --short > cta/_version
	poetry build
	pip install dist/*.tar.gz

create-dev:
	pre-commit install
	rm -rf env
	python3.10 -m venv env
	( \
		. env/bin/activate; \
		pip install -r requirements.txt; \
		poetry install; \
		deactivate; \
	)

package:
	pyinstaller --clean \
		--onefile \
		--add-data ./src/_version:. \
		--workpath ./pyinstaller \
		--name src \
		--hidden-import src \
		src/main.py
