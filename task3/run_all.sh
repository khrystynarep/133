#!/bin/bash

set -e  
cd "$(dirname "$0")"   

echo "📁 [1] Entered task3 directory: $(pwd)"

echo "🔐 [2] Generating SSH key..."
ssh-keygen -t rsa -b 2048 -f id_rsa -N "" -q
chmod 600 id_rsa
chmod 644 id_rsa.pub

echo "🚀 [3] Starting Vagrant machines..."
vagrant up

echo "🐳 [4] Building Docker image..."
docker build -t log-client .

echo "📦 [5] Minimizing image with docker-slim..."
docker-slim build --http-probe=false --tag log-client-slim log-client

echo "▶️ [6] Running slimmed container..."
docker run --rm --network host \
  -v "$PWD/id_rsa:/tmp/id_rsa:ro" \
  -e SSH_KEY_PATH=/tmp/id_rsa \
  -e AWS_SERVER_IP=100.73.158.1 \
  -e API_KEY=my_secret_key \
  log-client-slim
