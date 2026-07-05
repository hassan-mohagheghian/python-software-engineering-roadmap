# Concurrency - Multiprocessing
# -----------------------------------------------------------------------------
# Multiprocessing runs code in separate processes, each with its own
# memory space and Python interpreter. This bypasses the GIL and gives
# true parallelism for CPU-bound work.
#
# Key concepts:
# 1. Process — independent memory, no GIL contention.
# 2. Pool — map work across multiple processes.
# 3. Shared memory — Queue and Value for inter-process communication.
# 4. Trade-off — heavier than threads, but parallel for CPU work.
# -----------------------------------------------------------------------------


import multiprocessing
import time


# =============================================================================
# Basic Process
# =============================================================================


def cpu_work(n: int) -> int:
    """Simulate CPU-heavy work."""
    total = 0
    for i in range(n):
        total += i * i
    return total


def basic_process_demo():
    start = time.perf_counter()

    p1 = multiprocessing.Process(target=cpu_work, args=(10_000_000,))
    p2 = multiprocessing.Process(target=cpu_work, args=(10_000_000,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    elapsed = time.perf_counter() - start
    print(f"  Two processes finished in {elapsed:.2f}s")


# =============================================================================
# Pool — Map Work Across Cores
# =============================================================================


def square(n):
    return n * n


def pool_demo():
    numbers = list(range(10))

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, numbers)

    print(f"  Squares: {results}")


# =============================================================================
# Sequential vs Parallel Comparison
# =============================================================================


def compare():
    n = 5_000_000

    # Sequential
    start = time.perf_counter()
    for _ in range(4):
        cpu_work(n)
    seq_time = time.perf_counter() - start

    # Parallel
    start = time.perf_counter()
    with multiprocessing.Pool(4) as pool:
        pool.map(cpu_work, [n] * 4)
    par_time = time.perf_counter() - start

    print(f"  Sequential: {seq_time:.2f}s")
    print(f"  Parallel:   {par_time:.2f}s")
    print(f"  Speedup:    {seq_time / par_time:.1f}x")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Basic Process ===")
    basic_process_demo()

    print("\n=== Pool ===")
    pool_demo()

    print("\n=== Sequential vs Parallel ===")
    compare()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
