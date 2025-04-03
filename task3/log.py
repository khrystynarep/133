#!/usr/bin/env python3


import os
import re
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
REMOTE_DIR = "/home/sftpuser"    
LOCAL_LOGS_DIR = "./logs"      
GRAPH_DIR= "./outputs"  


FILENAME_PATTERN = re.compile(
    r'^(?P<destination>\S+)_created_by_(?P<creator>\S+)_at_(?P<datetime>\d{8}_\d{6})\.txt$'
)

def fetch_created_files_from_vm(host_info):
    """
    Підключається по SSH/SFTP до VM (host_info["ip"]),
    шукає всі файли, які починаються з 'created_by_',
    і копіює їх локально. Повертає список локальних шляхів.
    """
    copied_files = []
    ip = host_info["ip"]
    name = host_info["name"]

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            hostname=ip,
            username=SSH_USER,
            key_filename=SSH_KEY_PATH,
            look_for_keys=False,
        )
        
        sftp = ssh.open_sftp()
        remote_files = sftp.listdir(REMOTE_DIR)

        
        created_files = [f for f in remote_files if f.startswith('created_by_')]

        for remote_file in created_files:
            remote_path = os.path.join(REMOTE_DIR, remote_file)
            local_filename = f"{name}_{remote_file}"
            local_path = os.path.join(LOCAL_LOGS_DIR, local_filename)
            
            sftp.get(remote_path, local_path)
            copied_files.append(local_path)
        
        sftp.close()
        ssh.close()
    except Exception as e:
        print(f"[ERROR] Не вдалося отримати файли з {ip}. Причина: {e}")

    return copied_files

def parse_files_and_collect_times(file_paths):
    """
    Збирає дані по кожному файлу:
      - machine_dest (sftp1)
      - machine_creator (sftp2)
      - datetime (2025-04-03 16:05:01)  -- конвертуємо з '20250403_160501'

    Зберігає у структурі:
      stats[destination][creator]["times"] = [datetime1, datetime2, ...]
    Повертає такий словник.
    """
   
    stats = defaultdict(lambda: defaultdict(lambda: {"times": []}))

    for path in file_paths:
        filename = os.path.basename(path)
        match = FILENAME_PATTERN.match(filename)
        if match:
            dest = match.group("destination")
            creator = match.group("creator")
            dt_str = match.group("datetime") 
           
            date_part = dt_str.split('_')[0]  
            time_part = dt_str.split('_')[1] 

            
            dt = datetime.strptime(date_part + time_part, "%Y%m%d%H%M%S")

            
            stats[dest][creator]["times"].append(dt)

    return stats

def compute_analysis(stats):
    """
    На вхід отримує структуру:
      stats[destination][creator]["times"] = [dt1, dt2, dt3, ...]
    Розраховуємо:
      - Кількість (count) = len(times)
      - Середній інтервал між послідовними часами (avg_interval) у секундах

    Вихід:
      stats[destination][creator] = {
        "count": N,
        "avg_interval": X.XX
      }
    """
    for dest, creators_data in stats.items():
        for creator, info in creators_data.items():
            times_list = sorted(info["times"])
            count_files = len(times_list)
            if count_files <= 1:
                
                avg_int = 0.0
            else:
                
                deltas = []
                for i in range(1, count_files):
                    delta_sec = (times_list[i] - times_list[i - 1]).total_seconds()
                    deltas.append(delta_sec)
                avg_int = sum(deltas) / len(deltas)
            
            stats[dest][creator]["count"] = count_files
            stats[dest][creator]["avg_interval"] = avg_int

   
    return stats

def print_text_report_and_build_charts(stats):
    """
    1. Виводимо у консоль:
         - Machine(destination) | Machine(creator) | Count | Avg Interval (sec)
    2. Будуємо 2 види графіків для кожного destination:
       - (A) Bar-chart: скільки файлів (count) створили різні creators
       - (B) Bar-chart: який середній інтервал (avg_interval) між файлами
    """
    print("\n===== Результат аналізу (destination vs. creator) =====")
    print("Dest Machine | Creator Machine | Count | Avg Interval (sec)")

    
    graph_counts = {}
    graph_intervals = {}

    for dest, creators_data in stats.items():
        c_list = []
        count_list = []
        interval_list = []

        for creator, info in creators_data.items():
            c = info.get("count", 0)
            avg = info.get("avg_interval", 0.0)
            print(f"{dest:<13} | {creator:<15} | {c:<5} | {avg:.2f}")
            c_list.append(creator)
            count_list.append(c)
            interval_list.append(avg)

        if c_list:
            graph_counts[dest] = (c_list, count_list)
            graph_intervals[dest] = (c_list, interval_list)

   
    # Save charts to logs directory
    for dest, (creators, counts) in graph_counts.items():
        plt.figure()
        plt.bar(creators, counts)
        plt.title(f"Files created on {dest} (Count)")
        plt.xlabel("Creator machine")
        plt.ylabel("Number of files created")

        output_path = os.path.join(GRAPH_DIR, f"chart_count_{dest}.png")
        try:
            plt.savefig(output_path)
            print(f"[OK] Saved chart: {output_path}")
        except Exception as e:
            print(f"[ERROR] Could not save chart_count for {dest}: {e}")
        plt.close()

    for dest, (creators, intervals) in graph_intervals.items():
        plt.figure()
        plt.bar(creators, intervals)
        plt.title(f"Average interval on {dest} (sec)")
        plt.xlabel("Creator machine")
        plt.ylabel("Avg interval (seconds)")

        output_path = os.path.join(GRAPH_DIR, f"chart_interval_{dest}.png")
        try:
            plt.savefig(output_path)
            print(f"[OK] Saved chart: {output_path}")
        except Exception as e:
            print(f"[ERROR] Could not save chart_interval for {dest}: {e}")
        plt.close()


def main():
    os.makedirs(LOCAL_LOGS_DIR, exist_ok=True)
    all_local_files = []
    for host_info in HOSTS:
        new_files = fetch_created_files_from_vm(host_info)
        all_local_files.extend(new_files)

    print("=== Парсимо файли та збираємо часи ===")
    stats = parse_files_and_collect_times(all_local_files)

    print("=== Обчислюємо статистику (count, avg_interval) ===")
    stats = compute_analysis(stats)

    print_text_report_and_build_charts(stats)

if __name__ == "__main__":
    main()
