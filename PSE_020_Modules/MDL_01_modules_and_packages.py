# Python Basics - Modules and Imports
# -----------------------------------------------------------------------------
# Modules are files containing Python code that can be imported and reused.
#
# Key concepts:
# 1. Importing — import, from...import, as aliases.
# 2. Standard library — common built-in modules.
# 3. Creating modules — your own .py files as modules.
# 4. Packages — directories with __init__.py.
# 5. __name__ == "__main__" — script vs module execution.
# 6. pip — installing third-party packages.
# -----------------------------------------------------------------------------


# =============================================================================
# Import Styles
# =============================================================================


# Import entire module
import math

print(f"Pi: {math.pi}")
print(f"sqrt(16): {math.sqrt(16)}")

# Import specific items
from random import choice, randint  # noqa: E402

print(f"Random int 1-10: {randint(1, 10)}")
print(f"Random choice: {choice(['a', 'b', 'c'])}")

# Import with alias
import datetime as dt  # noqa: E402

now = dt.datetime.now()
print(f"Now: {now.strftime('%Y-%m-%d %H:%M')}")

# Import all (not recommended — pollutes namespace)
# from math import *


# =============================================================================
# Common Standard Library Modules
# =============================================================================


# os — operating system interface
import os  # noqa: E402

print(f"\nCurrent dir: {os.getcwd()}")
print(f"Platform: {os.name}")

# sys — system-specific parameters
import sys  # noqa: E402

print(f"Python version: {sys.version_info.major}.{sys.version_info.minor}")
print(f"Platform: {sys.platform}")

# collections — specialized containers
from collections import Counter, defaultdict, deque  # noqa: E402

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = Counter(words)
print(f"\nCounter: {counter}")
print(f"Most common: {counter.most_common(2)}")

dd = defaultdict(list)
for k, v in [("a", 1), ("b", 2), ("a", 3)]:
    dd[k].append(v)
print(f"Defaultdict: {dict(dd)}")

dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(f"Deque: {dq}")

# itertools — iteration utilities
from itertools import chain, combinations, product  # noqa: E402

print(f"\nChain: {list(chain([1, 2], [3, 4]))}")
print(f"Product: {list(product([1, 2], ['a', 'b']))}")
print(f"Combinations: {list(combinations([1, 2, 3], 2))}")

# functools — higher-order functions
from functools import lru_cache, reduce  # noqa: E402

nums = [1, 2, 3, 4, 5]
product_result = reduce(lambda a, b: a * b, nums)
print(f"\nReduce product: {product_result}")


@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(f"Fib(30): {fib(30)}")


# =============================================================================
# Reloading Modules
# =============================================================================


import importlib  # noqa: E402, F401

# importlib.reload(module) — reload a modified module during development


# =============================================================================
# Module Search Path
# =============================================================================


print("\nModule search path (first 3):")
for p in sys.path[:3]:
    print(f"  {p}")


# =============================================================================
# Creating Your Own Module
# =============================================================================


# Any .py file is a module. Example:
#
# my_utils.py:
#   def greet(name):
#       return f"Hello, {name}!"
#
#   PI = 3.14159
#
# main.py:
#   from my_utils import greet, PI
#   print(greet("Alice"))


# =============================================================================
# __name__ == "__main__"
# =============================================================================


# This pattern allows a file to be both importable and runnable as a script.
#
# def my_function():
#     ...
#
# if __name__ == "__main__":
#     # Only runs when executed directly, not when imported
#     my_function()


def demonstrate():
    """This runs only when the file is executed directly."""
    print("\nThis file is being run as a script")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Math Module ===")
    print(f"  ceil(4.3): {math.ceil(4.3)}")
    print(f"  floor(4.7): {math.floor(4.7)}")
    print(f"  factorial(5): {math.factorial(5)}")
    print(f"  gcd(12, 8): {math.gcd(12, 8)}")

    print("\n=== Random Module ===")
    import random

    random.seed(42)
    print(f"  randint(1, 100): {random.randint(1, 100)}")
    print(f"  random(): {random.random():.4f}")
    print(f"  choice: {random.choice(['red', 'green', 'blue'])}")
    print(f"  shuffle: {random.sample(range(5), 5)}")

    print("\n=== DateTime Module ===")
    today = dt.date.today()
    print(f"  Today: {today}")
    print(f"  Weekday: {today.strftime('%A')}")
    print(f"  ISO format: {today.isoformat()}")

    print("\n=== Collections ===")
    c = Counter("mississippi")
    print(f"  Counter: {c}")
    print(f"  Most common: {c.most_common(3)}")

    print("\n=== Itertools ===")
    print(f"  product: {list(product('AB', '12'))}")
    print(f"  combinations: {list(combinations('ABC', 2))}")

    print("\n=== Functools ===")
    nums = [1, 2, 3, 4, 5]
    print(f"  reduce sum: {reduce(lambda a, b: a + b, nums)}")


if __name__ == "__main__":
    main()
    demonstrate()
