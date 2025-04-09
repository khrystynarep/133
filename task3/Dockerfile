
FROM python:3.12-alpine as builder


RUN apk add --no-cache build-base libffi-dev openssl-dev


WORKDIR /install
COPY requirements.txt .


RUN pip install --no-cache-dir --prefix=/install flask requests paramiko


FROM python:3.12-alpine


COPY --from=builder /install /usr/local


WORKDIR /app
COPY log.py .
COPY id_rsa ./id_rsa


RUN chmod 600 id_rsa && mkdir -p logs


RUN python -m compileall . && find . -name '*.py' -delete


EXPOSE 6000

CMD ["python", "__pycache__/log.cpython-312.pyc"]
