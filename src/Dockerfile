FROM python:3.10

COPY . /root/app/

WORKDIR /root/app

RUN pip install poetry pyinstaller
RUN make build GIT_TAG=0.0.0
RUN make test
RUN make package

RUN cp dist/ingest_CTAAlerts .

RUN chmod +x run.bash
RUN chmod +x ingest_CTAAlerts

ENTRYPOINT [ "/bin/bash", "./run.bash" ]
