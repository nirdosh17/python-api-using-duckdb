FROM python:3.10.8-slim

RUN apt-get update && apt-get upgrade -y

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY server.py /app/server.py

COPY test.db /app/test.db

EXPOSE 8080

CMD ["python", "server.py"]
