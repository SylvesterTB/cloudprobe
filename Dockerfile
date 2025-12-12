FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt



COPY . /app

COPY config ./config
RUN mkdir -p /app/logs

CMD ["python", "-m", "cloudprobe.cli", "--config", "config/sample-test.json"]
