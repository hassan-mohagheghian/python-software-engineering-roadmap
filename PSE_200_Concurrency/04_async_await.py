# Concurrency - async / await
# -----------------------------------------------------------------------------
# asyncio lets you write concurrent code using coroutines. Unlike threads,
# coroutines are cooperative — they yield control explicitly, avoiding
# race conditions without locks.
#
# Key concepts:
# 1. async def — defines a coroutine.
# 2. await — pauses until a result is ready.
# 3. asyncio.gather — run multiple coroutines concurrently.
# 4. Practical uses — HTTP requests, web servers, database queries.
# -----------------------------------------------------------------------------


import asyncio
import time


# =============================================================================
# Basic Coroutine
# =============================================================================


async def say_hello(name: str, delay: float):
    print(f"  [{name}] Starting")
    await asyncio.sleep(delay)
    print(f"  [{name}] Done after {delay}s")
    return f"{name} result"


async def basic_demo():
    start = time.perf_counter()

    # Run sequentially
    await say_hello("A", 1.0)
    await say_hello("B", 0.5)

    seq_time = time.perf_counter() - start
    print(f"  Sequential: {seq_time:.1f}s")

    # Run concurrently
    start = time.perf_counter()
    results = await asyncio.gather(
        say_hello("C", 1.0),
        say_hello("D", 0.5),
    )

    par_time = time.perf_counter() - start
    print(f"  Concurrent: {par_time:.1f}s")
    print(f"  Results: {results}")


# =============================================================================
# Async Task with Exception Handling
# =============================================================================


async def risky_task(name: str):
    await asyncio.sleep(0.3)
    if name == "fail":
        raise ValueError(f"{name} failed!")
    return f"{name} succeeded"


async def task_demo():
    tasks = [risky_task("ok1"), risky_task("fail"), risky_task("ok2")]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for r in results:
        if isinstance(r, Exception):
            print(f"  Error: {r}")
        else:
            print(f"  Result: {r}")


# =============================================================================
# Producer-Consumer with Queue
# =============================================================================


async def producer(queue: asyncio.Queue, count: int):
    for i in range(count):
        await asyncio.sleep(0.1)
        item = f"item-{i}"
        await queue.put(item)
        print(f"  Produced: {item}")
    await queue.put(None)  # sentinel


async def consumer(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"  Consumed: {item}")


async def producer_consumer_demo():
    queue = asyncio.Queue()
    await asyncio.gather(
        producer(queue, 5),
        consumer(queue),
    )


# =============================================================================
# Usage
# =============================================================================


async def main():
    print("=== Basic Coroutine ===")
    await basic_demo()

    print("\n=== Exception Handling ===")
    await task_demo()

    print("\n=== Producer-Consumer ===")
    await producer_consumer_demo()


if __name__ == "__main__":
    asyncio.run(main())
