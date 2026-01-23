FROM python:3.12-slim

# system deps (docker cli)
RUN apt-get update && apt-get install -y \
    docker.io \
    python3-venv \
    awscli \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python3", "app.py"]
