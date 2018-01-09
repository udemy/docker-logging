FROM python:alpine

WORKDIR /app

COPY . /app

RUN pip install rfc5424-logging-handler

ENTRYPOINT ["python"]

CMD ["example-1/example_1.py"]

