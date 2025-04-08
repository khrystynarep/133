from flask import Flask, request, jsonify, render_template, redirect, url_for, send_from_directory
import os
import requests
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = './uploaded_logs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

API_KEY = "my_secret_key"

def parse_connection_log(filepath):
    entries = []
    with open(filepath, "r") as f:
        for line in f:
            try:
                timestamp_str, message = line.strip().split(" | ")
                dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                source = message.split("from")[1].split("to")[0].strip()
                dest = message.split("to")[1].strip()
                entries.append({
                    "time": dt.strftime("%Y-%m-%d %H:%M:%S"),
                    "source": source,
                    "dest": dest
                })
            except Exception as e:
                print(f"[WARN] Failed to parse line: {line.strip()} — {e}")
    return entries

@app.route('/')
def index():
    log_data = []
    for fname in os.listdir(UPLOAD_FOLDER):
        if fname.startswith("sftp") and fname.endswith("_connection_log.txt"):
            full_path = os.path.join(UPLOAD_FOLDER, fname)
            log_data.extend(parse_connection_log(full_path))

    charts = [f for f in os.listdir("outputs") if f.endswith(".png")]
    return render_template("index.html", charts=charts, log_data=log_data)

@app.route('/upload_log', methods=['POST'])
def upload_log():
    if request.headers.get("Authorization") != f"Bearer {API_KEY}":
        return jsonify({"error": "Unauthorized"}), 403

    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filename = secure_filename(file.filename)
    save_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(save_path)
    print(f"[INFO] File received: {filename}")
    return jsonify({"status": "ok", "message": f"File saved as {file.filename}"}), 200

@app.route('/refresh', methods=['POST'])
def refresh():
    try:
        print("[REFRESH] Calling local machine through SSH tunnel...")
        response = requests.post("http://localhost:6000/trigger_upload", timeout=15)
        print("[REFRESH] Response:", response.status_code, response.text)
    except Exception as e:
        print(f"[ERROR] Tunnel request failed: {e}")
    return redirect(url_for("index"))

@app.route("/outputs/<path:filename>")
def serve_outputs(filename):
    return send_from_directory("outputs", filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)