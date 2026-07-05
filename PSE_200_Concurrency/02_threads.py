# Concurrency - Threads
# -----------------------------------------------------------------------------
# Threads run concurrently within a single process, sharing memory.
# Python's GIL limits true parallelism for CPU-bound work, but threads
# are great for I/O-bound tasks (network, file, database).
#
# Key concepts:
# 1. threading.Thread — create and start threads.
# 2. Lock — prevent race conditions on shared data.
# 3. Daemon threads — background threads that exit when main exits.
# 4. Practical uses — downloading, file I/O, API calls.
# -----------------------------------------------------------------------------


import threading
import time


# =============================================================================
# Basic Thread
# =============================================================================


def worker(name: str, delay: float):
    print(f"  [{name}] Starting")
    time.sleep(delay)
    print(f"  [{name}] Done")


def basic_thread_demo():
    t1 = threading.Thread(target=worker, args=("A", 1.0))
    t2 = threading.Thread(target=worker, args=("B", 0.5))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("  Both threads finished")


# =============================================================================
# Thread with Return Value (via list)
# =============================================================================


def fetch(url: str, results: list, index: int):
    time.sleep(0.5)  # simulate network
    results[index] = f"Response from {url}"


def fetch_demo():
    urls = ["api.example.com", "cdn.example.com", "db.example.com"]
    results = [None] * len(urls)
    threads = []

    for i, url in enumerate(urls):
        t = threading.Thread(target=fetch, args=(url, results, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"  Results: {results}")


# =============================================================================
# Lock — Thread Safety
# =============================================================================


counter = 0
lock = threading.Lock()


def increment_unsafe():
    global counter
    for _ in range(100_000):
        counter += 1  # race condition


def increment_safe():
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1  # safe


def lock_demo():
    global counter

    counter = 0
    threads = [threading.Thread(target=increment_unsafe) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"  Unsafe (race): {counter} (expected 500000)")

    counter = 0
    threads = [threading.Thread(target=increment_safe) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"  Safe (locked): {counter} (expected 500000)")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Basic Thread ===")
    basic_thread_demo()

    print("\n=== Fetch Demo ===")
    fetch_demo()

    print("\n=== Lock Demo ===")
    lock_demo()


if __name__ == "__main__":
    main()
