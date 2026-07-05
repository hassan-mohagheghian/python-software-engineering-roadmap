# Concurrency & Parallelism - Synchronous vs Asynchronous I/O
# -----------------------------------------------------------------------------
# Concurrency is about *dealing* with lots of things at once.
# Parallelism is about *doing* lots of things at once.
#
# This example compares traditional Synchronous execution with Asynchronous I/O.
#
# Synchronous (Blocking):
# - Tasks are executed one after another in a sequence.
# - If a task is waiting for I/O (e.g., database query, API call, file read),
#   the entire execution is blocked, and the CPU sits idle doing nothing.
#
# Asynchronous (Non-blocking):
# - Tasks can yield control back to an "Event Loop" when they are waiting for I/O.
# - While one task is waiting, the Event Loop executes another task.
# - This allows a single thread to handle multiple tasks concurrently.
#
# Key Concepts in Python Asyncio:
# - Event Loop: The coordinator that manages and distributes execution of tasks.
# - Coroutines: Functions defined with `async def` that can suspend execution.
# - Await: The keyword `await` pauses a coroutine, yielding control back to the loop.
# - asyncio.gather: Runs multiple awaitable tasks concurrently and collects results.
# -----------------------------------------------------------------------------

import asyncio
import time


# =============================================================================
# 1. Synchronous Simulation (Sequential)
# =============================================================================

def fetch_data_sync(url: str, delay: float) -> str:
    """
    Simulates a synchronous network request.
    This function blocks the thread during time.sleep().
    """
    print(f"[Sync] Start fetching {url}...")
    time.sleep(delay)  # Blocking wait
    print(f"[Sync] Finished fetching {url}")
    return f"Data from {url}"


def run_synchronously(urls: list[str], delay: float):
    """
    Executes multiple fetches one by one.
    """
    print("\n--- Starting Synchronous Execution ---")
    start_time = time.perf_counter()
    
    results = []
    for url in urls:
        result = fetch_data_sync(url, delay)
        results.append(result)
        
    duration = time.perf_counter() - start_time
    print(f"Synchronous total duration: {duration:.2f} seconds")
    return results, duration


# =============================================================================
# 2. Asynchronous Simulation (Concurrent)
# =============================================================================

async def fetch_data_async(url: str, delay: float) -> str:
    """
    Simulates an asynchronous network request.
    This function yields control back to the event loop during asyncio.sleep().
    """
    print(f"[Async] Start fetching {url}...")
    await asyncio.sleep(delay)  # Non-blocking wait (yields control)
    print(f"[Async] Finished fetching {url}")
    return f"Data from {url}"


async def run_asynchronously(urls: list[str], delay: float):
    """
    Executes multiple fetches concurrently using asyncio.gather.
    """
    print("\n--- Starting Asynchronous Execution ---")
    start_time = time.perf_counter()
    
    # Create coroutine tasks for each URL
    tasks = [fetch_data_async(url, delay) for url in urls]
    
    # Run all tasks concurrently and gather results
    results = await asyncio.gather(*tasks)
    
    duration = time.perf_counter() - start_time
    print(f"Asynchronous total duration: {duration:.2f} seconds")
    return results, duration


# =============================================================================
# Main Execution
# =============================================================================

def main():
    urls = [
        "https://api.example.com/users",
        "https://api.example.com/products",
        "https://api.example.com/orders",
    ]
    delay = 1.0  # Simulated latency for each request in seconds
    
    # 1. Run Synchronously
    sync_results, sync_duration = run_synchronously(urls, delay)
    
    # 2. Run Asynchronously
    # We use asyncio.run to create the event loop and run our async entry point
    async_results, async_duration = asyncio.run(run_asynchronously(urls, delay))
    
    # 3. Summary Comparison
    print("\n================== Results Summary ==================")
    print(f"Synchronous Results: {sync_results}")
    print(f"Asynchronous Results: {async_results}")
    print(f"Sync took:   {sync_duration:.4f} seconds (Sequential delay sum)")
    print(f"Async took:  {async_duration:.4f} seconds (Overlapped concurrency)")
    
    speedup = sync_duration / async_duration
    print(f"Async is ~{speedup:.1f}x faster for this load!")
    print("=====================================================")


if __name__ == "__main__":
    main()
