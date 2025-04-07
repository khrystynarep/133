#!/usr/bin/env python3

import os
import paramiko
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime

HOSTS = [
    {"name": "sftp1", "ip": "192.168.56.11"},
    {"name": "sftp2", "ip": "192.168.56.12"},
    {"name": "sftp3", "ip": "192.168.56.13"},
]

SSH_USER = "sftpuser"
SSH_KEY_PATH = "id_rsa"
REMOTE_LOG_FILE = "/home/sftpuser/connection_log.txt"
LOCAL_LOGS_DIR = "./logs"
GRAPH_DIR = "./outputs"

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
        return local_path
    except Exception as e:
        print(f"[ERROR] Cannot fetch log from {ip}: {e}")
        return None

def parse_connection_log(filepath):
    stats = defaultdict(lambda: defaultdict(list))
    with open(filepath, "r") as f:
        for line in f:
            try:
                timestamp_str, message = line.strip().split(" | ")
                dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                parts = message.split("from")[1].strip().split(" to ")
                source = parts[0]
                destination = parts[1]
                stats[destination][source].append(dt)
            except Exception as e:
                print(f"[WARN] Failed to parse line: {line.strip()} — {e}")
    return stats

def compute_analysis(stats):
    for dest, creators_data in stats.items():
        for creator, times in creators_data.items():
            times_list = sorted(times)
            count_files = len(times_list)
            if count_files <= 1:
                avg_int = 0.0
            else:
                deltas = [(times_list[i] - times_list[i - 1]).total_seconds() for i in range(1, count_files)]
                avg_int = sum(deltas) / len(deltas)
            stats[dest][creator] = {
                "count": count_files,
                "avg_interval": avg_int
            }
    return stats

def print_text_report_and_build_charts(stats):
    print("\\n===== Результат аналізу (destination vs. creator) =====")
    print("Dest Machine | Creator Machine | Count | Avg Interval (sec)")
    graph_counts = {}
    graph_intervals = {}
    for dest, creators_data in stats.items():
        c_list, count_list, interval_list = [], [], []
        for creator, data in creators_data.items():
            count = data["count"]
            avg = data["avg_interval"]
            print(f"{dest:<13} | {creator:<15} | {count:<5} | {avg:.2f}")
            c_list.append(creator)
            count_list.append(count)
            interval_list.append(avg)
        if c_list:
            graph_counts[dest] = (c_list, count_list)
            graph_intervals[dest] = (c_list, interval_list)
    os.makedirs(GRAPH_DIR, exist_ok=True)
    for dest, (creators, counts) in graph_counts.items():
        plt.figure()
        plt.bar(creators, counts)
        plt.title(f"Files created on {dest} (Count)")
        plt.xlabel("Creator machine")
        plt.ylabel("Number of files created")
        plt.savefig(os.path.join(GRAPH_DIR, f"chart_count_{dest}.png"))
        plt.close()
    for dest, (creators, intervals) in graph_intervals.items():
        plt.figure()
        plt.bar(creators, intervals)
        plt.title(f"Average interval on {dest} (sec)")
        plt.xlabel("Creator machine")
        plt.ylabel("Avg interval (seconds)")
        plt.savefig(os.path.join(GRAPH_DIR, f"chart_interval_{dest}.png"))
        plt.close()
    print("\\n[INFO] Графіки збережено у ./outputs\\n")

def main():
    os.makedirs(LOCAL_LOGS_DIR, exist_ok=True)
    all_stats = defaultdict(lambda: defaultdict(list))
    for host in HOSTS:
        log_path = fetch_log_file_from_vm(host)
        if log_path:
            stats = parse_connection_log(log_path)
            for dest, creators in stats.items():
                for creator, times in creators.items():
                    all_stats[dest][creator].extend(times)
    stats = compute_analysis(all_stats)
    print_text_report_and_build_charts(stats)

if __name__ == "__main__":
    main()