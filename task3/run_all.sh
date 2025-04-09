#!/bin/bash

echo "[1] 🛠 Building image..."
docker build -t log-client .

echo "[2] 📦 Minimizing image with docker-slim..."
docker-slim build --http-probe=false --tag log-client-slim log-client

echo "[3] 🚀 Running container with mounted SSH key..."
docker run --rm --network host \
  -v $PWD/id_rsa:/tmp/id_rsa:ro \
  -e SSH_KEY_PATH=/tmp/id_rsa \
  -e AWS_SERVER_IP=100.73.158.1 \
  -e API_KEY=my_secret_key \
  log-client-slim
