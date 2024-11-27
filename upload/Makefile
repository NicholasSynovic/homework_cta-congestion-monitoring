GIT_TAG ?= $(shell git --no-pager tag | tail -n 1)

build:
	rm -rf dist
	echo $(GIT_TAG) > cta/_version
	poetry version $(GIT_TAG)
	poetry build
	pip install dist/*.tar.gz

package:
	pyinstaller --clean \
		--onefile \
		--add-data ./cta/_version:. \
		--workpath ./pyinstaller \
		--name cta \
		--hidden-import cta \
		cta/main.py

test:
	pytest tests/test_*.py
