# Iterators & Generators - Generator
# -----------------------------------------------------------------------------
# A generator is a function that uses yield to produce values lazily.
# It automatically implements the iterator protocol and maintains state.
#
# Key concepts:
# 1. yield keyword
# 2. Lazy evaluation (produces values on demand)
# 3. Generator state preservation
# 4. Memory efficiency
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Generator
# =============================================================================


from collections.abc import Generator


def countdown(n: int) -> Generator[int, None, None]:
    """Count down from n to 1."""
    while n > 0:
        yield n
        n -= 1


for num in countdown(5):
    print(num, end=" ")
print()


# =============================================================================
# Generator vs List
# =============================================================================


# List comprehension — stores all in memory
squares_list = [x**2 for x in range(1000000)]


# Generator — produces one at a time
def squares_gen():
    for x in range(1000000):
        yield x**2


# Generator uses constant memory
gen = squares_gen()
print(f"First 5: {[next(gen) for _ in range(5)]}")


# =============================================================================
# Generator with State
# =============================================================================


def fibonacci():
    """Infinite Fibonacci generator."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
first_10 = [next(fib) for _ in range(10)]
print(f"Fibonacci: {first_10}")


# =============================================================================
# Practical: Read Large Files
# =============================================================================


def read_large_file(filepath):
    """Read a file line by line (memory efficient)."""
    with open(filepath) as f:
        for line in f:
            yield line.strip()


def main():
    print("=== Generator ===")
    gen = countdown(5)
    for num in gen:
        print(num, end=" ")
    print()
    fib = fibonacci()
    print(f"First 8: {[next(fib) for _ in range(8)]}")


if __name__ == "__main__":
    main()
