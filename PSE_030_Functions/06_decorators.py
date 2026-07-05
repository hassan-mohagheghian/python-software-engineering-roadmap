# Functions - Decorators
# -----------------------------------------------------------------------------
# A decorator wraps a function to modify its behavior without changing the
# original code. Decorators use the @ syntax and are common in frameworks
# for logging, timing, access control, and caching.
#
# At its core, a decorator is a function that takes a function and returns
# a new function — it's a higher-order function applied with @ syntax.
# -----------------------------------------------------------------------------


# =============================================================================
# Simple Decorator — Logging
# =============================================================================


def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"  Calling {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"  {func.__name__} returned {result}")
        return result
    return wrapper


@log_calls
def multiply(a: int, b: int) -> int:
    return a * b


# =============================================================================
# Decorator — Timing
# =============================================================================


import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__} took {elapsed:.6f}s")
        return result
    return wrapper


@timer
def slow_sum(n: int) -> int:
    total = 0
    for i in range(n):
        total += i
    return total


# =============================================================================
# Stacking Decorators
# =============================================================================


def add_prefix(prefix: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{prefix}{result}"
        return wrapper
    return decorator


@add_prefix(">> ")
@log_calls
def get_name(first: str, last: str) -> str:
    return f"{first} {last}"


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== @log_calls ===")
    multiply(3, 4)

    print("\n=== @timer ===")
    slow_sum(1_000_000)

    print("\n=== Stacked Decorators ===")
    result = get_name("Jane", "Doe")
    print(f"  Result: {result}")


if __name__ == "__main__":
    main()
