
FROM python:3.10-slim


RUN apt-get update && apt-get install -y --no-install-recommends \
    libfreetype6-dev libpng-dev gcc ssh-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY log.py /app/log.py

RUN mkdir /app/outputs

VOLUME ["/app/outputs"]
VOLUME ["/app/logs"]
VOLUME ["/app"]

CMD ["python", "/app/log.py"]
