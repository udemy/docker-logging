FROM python:alpine

WORKDIR /app

COPY . /app

ENTRYPOINT ["python"]

CMD ["example-1/example_1.py"]

