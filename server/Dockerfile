FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5001 5002 5003 5004

CMD ["python", "server.py"]