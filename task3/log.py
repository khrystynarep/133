from flask import Flask, jsonify
import paramiko
import requests
import os
from datetime import datetime

app = Flask(__name__)
HOSTS = [
    {"name": "sftp1", "ip": "192.168.56.11"},
    {"name": "sftp2", "ip": "192.168.56.12"},
    {"name": "sftp3", "ip": "192.168.56.13"},
]

SSH_USER = "sftpuser"
SSH_KEY_PATH = "id_rsa"
REMOTE_LOG_FILE = "/home/sftpuser/connection_log.txt"
LOCAL_LOGS_DIR = "./logs"
AWS_SERVER_IP = "100.73.158.1"  # Replace with AWS server Tailscale IP
UPLOAD_URL = f"http://{AWS_SERVER_IP}:5000/upload_log"
API_KEY = "my_secret_key"

def fetch_log_file_from_vm(host_info):
    ip = host_info["ip"]
    name = host_info["name"]
    local_path = os.path.join(LOCAL_LOGS_DIR, f"{name}_connection_log.txt")
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, username=SSH_USER, key_filename=SSH_KEY_PATH)
        sftp = ssh.open_sftp()
        sftp.get(REMOTE_LOG_FILE, local_path)
        sftp.close()
        ssh.close()
        return local_path
    except Exception as e:
        print(f"[ERROR] Cannot fetch from {name}: {e}")
        return None

def upload_file_to_server(filepath):
    try:
        with open(filepath, "rb") as f:
            files = {"file": (os.path.basename(filepath), f)}
            headers = {"Authorization": f"Bearer {API_KEY}"}
            response = requests.post(UPLOAD_URL, files=files, headers=headers)
            print(f"[UPLOAD] {filepath}: {response.status_code} {response.text}")
    except Exception as e:
        print(f"[ERROR] Upload failed: {e}")

@app.route("/trigger_upload", methods=["POST"])
def trigger_upload():
    os.makedirs(LOCAL_LOGS_DIR, exist_ok=True)
    for host in HOSTS:
        log_path = fetch_log_file_from_vm(host)
        if log_path:
            upload_file_to_server(log_path)
    return jsonify({"status": "ok", "message": "Logs collected and sent"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)