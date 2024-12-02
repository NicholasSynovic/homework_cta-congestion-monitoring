GIT_TAG ?= $(shell git --no-pager tag | tail -n 1)

build:
	rm -rf dist
	echo $(GIT_TAG) > cta/_version
	poetry version $(GIT_TAG)
	poetry build
	pip install dist/*.tar.gz

deploy:
	docker volume create ccm_data
	docker build -t ccm_image_ingest .
	docker run -d \
	--name ccm_container_ingest \
	--restart always \
	-v ccm_data:/root/app \
	ccm_image_ingest

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
