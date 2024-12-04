FROM python:3.10 AS build

WORKDIR /build

COPY ../../../pyproject.toml pyproject.toml
COPY ../../../poetry.lock poetry.lock
COPY ingest_CTARoutesAlerts.py app.py

RUN mkdir logs alerts
RUN pip install poetry
RUN python3.10 -m poetry update

COPY ../../../dist dist

RUN pip install dist/*.tar.gz

ENTRYPOINT [ "python3.10", "app.py" ]
CMD ["--output", "alerts", "--logs", "logs"]
