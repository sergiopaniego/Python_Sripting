import psutil
import concurrent.futures
import time

# Define monitoring tasks
def monitor_cpu():
    return f"CPU Usage: {psutil.cpu_percent(interval=1)}%"

def monitor_memory():
    memory = psutil.virtual_memory()
    return f"Memory Usage: {memory.percent}%"

def monitor_disk():
    disk = psutil.disk_usage('/')
    return f"Disk Usage: {disk.percent}%"

def log_to_file(data):
    with open('system_monitor.log', 'a') as f:
        f.write(data + '\n')

# Parallelize monitoring tasks
def monitor_system():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for _ in range(10):  # Monitor for 10 iterations
            futures = [
                executor.submit(monitor_cpu),
                executor.submit(monitor_memory),
                executor.submit(monitor_disk)
            ]
            results = [future.result() for future in concurrent.futures.as_completed(futures)]
            log_to_file("\n".join(results))
            print("\n".join(results))  # Optional: Print to console
            time.sleep(2)

monitor_system()
