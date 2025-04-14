from flask import Flask, jsonify
import paramiko
import requests
import os
from datetime import datetime
import sys

app = Flask(__name__)

HOSTS = [
    {"name": "sftp1", "ip": "192.168.56.11"},
    {"name": "sftp2", "ip": "192.168.56.12"},
    {"name": "sftp3", "ip": "192.168.56.13"},
]

SSH_USER = "sftpuser"
SSH_KEY_PATH = os.getenv("SSH_KEY_PATH", "/root/.ssh/id_rsa")

REMOTE_LOG_FILE = "/home/sftpuser/connection_log.txt"
LOCAL_LOGS_DIR = "./logs"
AWS_SERVER_IP = os.getenv("AWS_SERVER_IP", "100.73.158.1")
UPLOAD_URL = f"http://{AWS_SERVER_IP}:5000/upload_log"
API_KEY = os.getenv("API_KEY", "my_secret_key")

def fetch_log_file_from_vm(host_info):
    ip = host_info["ip"]
    name = host_info["name"]
    local_path = os.path.join(LOCAL_LOGS_DIR, f"{name}_connection_log.txt")

    if not os.path.exists(SSH_KEY_PATH):
        print(f"[ERROR] SSH key file not found at {SSH_KEY_PATH}")
        sys.stdout.flush()
        return None

    try:
        with open(SSH_KEY_PATH, 'r') as key_file:
            key_data = key_file.read()
            print(f"[DEBUG] SSH KEY content:\n{key_data}")
            sys.stdout.flush()

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print(f"[INFO] Trying to connect to {name} ({ip}) using key {SSH_KEY_PATH}")
        sys.stdout.flush()
        
        ssh.connect(hostname=ip, username=SSH_USER, key_filename=SSH_KEY_PATH, timeout=10)
        sftp = ssh.open_sftp()
        sftp.get(REMOTE_LOG_FILE, local_path)
        sftp.close()
        ssh.close()
        print(f"[INFO] Successfully fetched log from {name}")
        sys.stdout.flush()
        return local_path

    except Exception as e:
        print(f"[ERROR] Cannot fetch from {name} ({ip}): {e}")
        sys.stdout.flush()
        return None

def upload_file_to_server(filepath):
    try:
        with open(filepath, "rb") as f:
            files = {"file": (os.path.basename(filepath), f)}
            headers = {"Authorization": f"Bearer {API_KEY}"}
            response = requests.post(UPLOAD_URL, files=files, headers=headers, timeout=30)
            print(f"[UPLOAD] {filepath}: {response.status_code} {response.text}")
            return response.status_code == 200
    except Exception as e:
        print(f"[ERROR] Upload failed: {e}")
        return False

@app.route("/trigger_upload", methods=["POST"])
def trigger_upload():
    os.makedirs(LOCAL_LOGS_DIR, exist_ok=True)

    uploaded = []
    failed = []

    for host in HOSTS:
        name = host["name"]
        log_path = fetch_log_file_from_vm(host)
        if log_path:
            success = upload_file_to_server(log_path)
            if success:
                uploaded.append(name)
            else:
                failed.append({"host": name, "reason": "upload failed"})
        else:
            failed.append({"host": name, "reason": "log not fetched"})

    return jsonify({
        "status": "ok",
        "uploaded": uploaded,
        "failed": failed
    })

@app.route("/")
def index():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)