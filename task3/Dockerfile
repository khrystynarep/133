# syntax=docker/dockerfile:1

FROM python:3.12-alpine AS builder
ENV PYTHONUNBUFFERED=1


RUN apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev \
    cargo \
    ca-certificates \
    tar

WORKDIR /app


COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


COPY log.py .


RUN pip install --no-cache-dir pyinstaller


RUN mkdir -p /app/tmp && chmod 1777 /app/tmp


RUN pyinstaller --onefile --strip --clean --runtime-tmpdir /app/tmp log.py


RUN ls -lh dist && du -sh dist/*


RUN mkdir -p /app/deps/lib /app/deps/etc/ssl/certs


RUN ldd dist/log | grep '=>' | awk '{print $3}' | sort -u | xargs -I '{}' cp -v '{}' /app/deps/lib/ || true


RUN cp -v /lib/libz.so.1 /app/deps/lib/ 2>/dev/null || \
    cp -v /usr/lib/libz.so.1 /app/deps/lib/ || true


RUN cp -v /lib/ld-musl-*.so.1 /app/deps/lib/ || true


RUN cp -v /etc/ssl/certs/ca-certificates.crt /app/deps/etc/ssl/certs/


FROM scratch


COPY --from=builder /app/deps/lib /lib


COPY --from=builder /app/deps/etc/ssl/certs /etc/ssl/certs


COPY --from=builder /app/dist/log /app/log


COPY --from=builder /app/tmp /tmp


ENV TMPDIR=/tmp
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
ENV SSH_KEY_PATH=/app/host_id_rsa
ENV LOCAL_LOGS_DIR=/app/logs

EXPOSE 6000

ENTRYPOINT ["/app/log"]
