import multiprocessing
import time

# Define a CPU-bound task
def cpu_bound_task(n):
    return sum(i*i for i in range(n))

if __name__ == "__main__":
    N = 10_000_000  # Large range for heavy computation

    # Sequential execution for comparison
    start_time = time.time()
    for _ in range(4):
        cpu_bound_task(N)
    sequential_time = time.time() - start_time
    print(f"Sequential execution time: {sequential_time:.2f} seconds")

    # Parallel execution using multiprocessing
    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(cpu_bound_task, [N, N, N, N])
    parallel_time = time.time() - start_time
    print(f"Parallel execution time: {parallel_time:.2f} seconds")
