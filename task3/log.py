import os
import subprocess
import threading
import time
from flask import Flask, jsonify
import paramiko
import requests
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime


AWS_HOST = "34.207.124.149"
AWS_USER = "ubuntu"
SSH_KEY_PATH = "id_rsa"
TUNNEL_PORT = 6000
LOCAL_FLASK_PORT = 6000
API_KEY = "my_secret_key"
UPLOAD_URL = f"http://{AWS_HOST}:5000/upload_log"
SSH_KEY_PATH = "tesk3keys.pem"


HOSTS = [
    {"name": "sftp1", "ip": "192.168.56.11"},
    {"name": "sftp2", "ip": "192.168.56.12"},
    {"name": "sftp3", "ip": "192.168.56.13"},
]

SSH_USER = "sftpuser"
REMOTE_LOG_FILE = "/home/sftpuser/connection_log.txt"
LOCAL_LOGS_DIR = "./logs"


app = Flask(__name__)

@app.route("/trigger_upload", methods=["POST"])
def trigger_upload():
    try:
        print("[INFO] Triggered remotely by server. Fetching logs...")
        collect_and_upload_logs()
        return jsonify({"status": "ok", "message": "Logs sent"}), 200
    except Exception as e:
        print(f"[ERROR] {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


def fetch_log_file_from_vm(host_info):
    ip = host_info["ip"]
    name = host_info["name"]
    local_path = os.path.join(LOCAL_LOGS_DIR, f"{name}_connection_log.txt")
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, username=SSH_USER, key_filename=SSH_KEY_PATH, look_for_keys=False)
        sftp = ssh.open_sftp()
        sftp.get(REMOTE_LOG_FILE, local_path)
        sftp.close()
        ssh.close()
        print(f"[OK] Downloaded log from {name}")
        return local_path
    except Exception as e:
        print(f"[ERROR] Cannot fetch log from {ip}: {e}")
        return None


def send_log_to_server(filepath):
    try:
        with open(filepath, "rb") as f:
            files = {"file": (os.path.basename(filepath), f)}
            headers = {"Authorization": f"Bearer {API_KEY}"}
            response = requests.post(UPLOAD_URL, headers=headers, files=files)
            print(f"[UPLOAD] {filepath} -> {response.status_code}: {response.text}")
    except Exception as e:
        print(f"[ERROR] Upload failed for {filepath}: {e}")

# === Головна функція збору та відправки ===
def collect_and_upload_logs():
    os.makedirs(LOCAL_LOGS_DIR, exist_ok=True)
    for host in HOSTS:
        log_path = fetch_log_file_from_vm(host)
        if log_path:
            send_log_to_server(log_path)


def setup_reverse_ssh_tunnel():
    print("[INFO] Setting up reverse SSH tunnel to server...")
    ssh_cmd = [
        "ssh",
        "-i", SSH_KEY_PATH,
        "-o", "StrictHostKeyChecking=no",
        "-N",
        "-R", f"{TUNNEL_PORT}:localhost:{LOCAL_FLASK_PORT}",
        f"{AWS_USER}@{AWS_HOST}"
    ]
    try:
        subprocess.Popen(ssh_cmd)
        print(f"[OK] Tunnel established: AWS:{TUNNEL_PORT} => Local:{LOCAL_FLASK_PORT}")
    except Exception as e:
        print(f"[ERROR] Tunnel failed: {e}")


def start_flask_thread():
    thread = threading.Thread(target=lambda: app.run(host="0.0.0.0", port=LOCAL_FLASK_PORT))
    thread.daemon = True
    thread.start()


if __name__ == "__main__":
    print("[BOOT] Starting local log server with auto-tunnel...")
    setup_reverse_ssh_tunnel()
    start_flask_thread()
    print("[READY] You can now trigger upload from the server via /refresh endpoint.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[EXIT] Exiting log.py gracefully.")

