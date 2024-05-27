# Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install flask

ENV SERVER_ID=Unknown

EXPOSE 5000

CMD ["python", "server.py"]
