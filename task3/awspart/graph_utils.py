# file: graph_utils.py

import os
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime

LOG_DIR = "./uploaded_logs"
OUTPUT_DIR = "./outputs"
def parse_connection_log(filepath):
    stats = defaultdict(lambda: defaultdict(list))
    with open(filepath, "r") as f:
        for line in f:
            try:
                if "|" not in line or "from" not in line or "to" not in line:
                    continue  

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
    final = defaultdict(dict)
    for dest, creators_data in stats.items():
        for creator, times in creators_data.items():
            times_list = sorted(times)
            count = len(times_list)
            avg_int = 0.0
            if count > 1:
                deltas = [(times_list[i] - times_list[i - 1]).total_seconds() for i in range(1, count)]
                avg_int = sum(deltas) / len(deltas)
            final[dest][creator] = {
                "count": count,
                "avg_interval": avg_int
            }
    return final

def analyze_and_generate_graphs():
    combined_stats = defaultdict(lambda: defaultdict(list))
    
    for filename in os.listdir(LOG_DIR):
        if not filename.endswith(".txt"):
            continue
        filepath = os.path.join(LOG_DIR, filename)
        stats = parse_connection_log(filepath)
        for dest, sources in stats.items():
            for src, times in sources.items():
                combined_stats[dest][src].extend(times)

    stats = compute_analysis(combined_stats)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for f in os.listdir(OUTPUT_DIR):
        if f.endswith(".png"):
            os.remove(os.path.join(OUTPUT_DIR, f))

    for dest, creators in stats.items():
        c_list, count_list, interval_list = [], [], []
        for creator, data in creators.items():
            c_list.append(creator)
            count_list.append(data["count"])
            interval_list.append(data["avg_interval"])

        
        plt.figure()
        plt.bar(c_list, count_list)
        plt.title(f"Files created on {dest} (Count)")
        plt.xlabel("Creator")
        plt.ylabel("File count")
        plt.savefig(os.path.join(OUTPUT_DIR, f"chart_count_{dest}.png"))
        plt.close()

        
        plt.figure()
        plt.bar(c_list, interval_list)
        plt.title(f"Average Interval on {dest} (sec)")
        plt.xlabel("Creator")
        plt.ylabel("Avg Interval (sec)")
        plt.savefig(os.path.join(OUTPUT_DIR, f"chart_interval_{dest}.png"))
        plt.close()
