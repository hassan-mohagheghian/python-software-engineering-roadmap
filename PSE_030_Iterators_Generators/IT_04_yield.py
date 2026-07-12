# Iterators & Generators - yield
# -----------------------------------------------------------------------------
# yield pauses the function and returns a value. The function's state is
# preserved, and execution resumes from where it left off on the next call.
#
# Key concepts:
# 1. yield as return + pause
# 2. yield from — delegate to sub-generator
# 3. send() — send values into generator
# 4. Generator pipeline
# -----------------------------------------------------------------------------


# =============================================================================
# yield Basics
# =============================================================================


def simple_gen():
    print("  First yield")
    yield 1
    print("  Second yield")
    yield 2
    print("  Third yield")
    yield 3


gen = simple_gen()
print(next(gen))  # prints "First yield", returns 1
print(next(gen))  # prints "Second yield", returns 2
print(next(gen))  # prints "Third yield", returns 3


# =============================================================================
# yield from — Delegation
# =============================================================================


def flatten(nested):
    """Flatten a nested list using yield from."""
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


data = [1, [2, 3], [4, [5, 6]], 7]
print(f"Flattened: {list(flatten(data))}")


# =============================================================================
# send() — Two-Way Communication
# =============================================================================


def accumulator():
    """Accumulate values sent to it."""
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value


acc = accumulator()
next(acc)  # prime the generator
print(f"After +5: {acc.send(5)}")
print(f"After +3: {acc.send(3)}")
print(f"After +7: {acc.send(7)}")


# =============================================================================
# Generator Pipeline
# =============================================================================


def numbers():
    """Generate numbers 1-10."""
    for i in range(1, 11):
        yield i


def squares(nums):
    """Square each number."""
    for n in nums:
        yield n**2


def evens(nums):
    """Keep only even squares."""
    for n in nums:
        if n % 2 == 0:
            yield n


pipeline = evens(squares(numbers()))
print(f"Even squares: {list(pipeline)}")


def main():
    print("=== yield ===")
    gen = simple_gen()
    print(f"Values: {[x for x in gen]}")
    data = [[1, 2], [3, [4, 5]], 6]
    print(f"Flattened: {list(flatten(data))}")


if __name__ == "__main__":
    main()
