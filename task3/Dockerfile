############################
# 1. Builder
############################
FROM python:3.12-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libffi-dev libssl-dev cargo && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt

COPY id_rsa id_rsa.pub ./
RUN chmod 600 id_rsa

COPY log.py .

############################
# 2. Runtime (distroless)
############################
FROM gcr.io/distroless/python3-debian12

COPY --from=builder /usr/local /usr/local
WORKDIR /app

COPY --from=builder /app/log.py .
COPY --from=builder /app/id_rsa /root/.ssh/id_rsa
COPY --from=builder /app/id_rsa.pub /root/.ssh/id_rsa.pub

ENTRYPOINT ["python", "/app/log.py"]
EXPOSE 6000
