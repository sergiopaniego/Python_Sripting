import psutil
import concurrent.futures
import multiprocessing
import time

# System monitoring tasks
def monitor_cpu():
    return f"CPU Usage: {psutil.cpu_percent(interval=1)}%"

def monitor_memory():
    memory = psutil.virtual_memory()
    return f"Memory Usage: {memory.percent}%"

def monitor_disk():
    disk = psutil.disk_usage('/')
    return f"Disk Usage: {disk.percent}%"

def log_to_file(data, filename):
    with open(filename, 'a') as f:
        f.write(data + '\n')

# CPU-bound task
def cpu_bound_task(n):
    return sum(i*i for i in range(n))

# Parallel system monitoring and CPU-bound tasks
def monitor_and_compute():
    N = 10_000_000  # Large range for heavy computation
    
    # Start system monitoring in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for _ in range(10):  # Monitor for 10 iterations
            futures = [
                executor.submit(monitor_cpu),
                executor.submit(monitor_memory),
                executor.submit(monitor_disk)
            ]
            results = [future.result() for future in concurrent.futures.as_completed(futures)]
            log_to_file("\n".join(results), 'system_monitor_during_computation.log')
            print("\n".join(results))  # Optional: Print to console
            time.sleep(2)

    # Run CPU-bound tasks in parallel
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(cpu_bound_task, [N, N, N, N])

if __name__ == "__main__":
    monitor_and_compute()
