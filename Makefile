GIT_TAG := $(shell git --no-pager tag | tail -n 1)

build:
	poetry -C cta2json version $(GIT_TAG)
	poetry -C cta2json version --short > cta2json/_version
	poetry -C cta2json build
	pip install cta2json/dist/*.tar.gz

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
