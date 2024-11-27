GIT_TAG ?= $(shell git --no-pager tag | tail -n 1)

build:
	rm -rf dist
	echo $(GIT_TAG) > cta/_version
	poetry version $(GIT_TAG)
	poetry build
	pip install dist/*.tar.gz

deploy:
	echo

package:
	pyinstaller --clean \
		--onefile \
		--add-data ./cta/_version:. \
		--workpath ./pyinstaller \
		--name ingest_CTAAlerts \
		--hidden-import cta \
		ingest_CTAAlerts.py

	pyinstaller --clean \
		--onefile \
		--add-data ./cta/_version:. \
		--workpath ./pyinstaller \
		--name ingest_CTALStops \
		--hidden-import cta \
		ingest_CTALStops.py
test:
	pytest tests/test_*.py
