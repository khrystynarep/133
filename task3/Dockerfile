# syntax=docker/dockerfile:1


FROM python:3.12-alpine AS builder

ENV PYTHONUNBUFFERED=1


RUN apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev \
    cargo \
    upx

WORKDIR /app


COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


COPY log.py .


RUN pip install --no-cache-dir pyinstaller


RUN pyinstaller --onefile --strip --clean --upx-dir /usr/bin log.py


RUN ls -lh dist && du -sh dist/*


FROM alpine:latest


RUN apk add --no-cache \
    libstdc++ \
    ca-certificates \
    openssl

WORKDIR /app


COPY --from=builder /app/dist/log /app/log


RUN chmod +x /app/log


RUN mkdir -p /app/logs

ENV SSH_KEY_PATH=/app/host_id_rsa
ENV LOCAL_LOGS_DIR=/app/logs

EXPOSE 6000

ENTRYPOINT ["/app/log"]
