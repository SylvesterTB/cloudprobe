FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY cloudprobe /app/cloudprobe
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY config ./config

RUN apt-get update && apt-get install -y awscli
RUN mkdir -p /app/output

ENTRYPOINT ["/entrypoint.sh"]
