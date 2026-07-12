# Iterators & Generators - Iterator
# -----------------------------------------------------------------------------
# An iterator implements __iter__() and __next__(). It produces items
# one at a time and remembers its state between calls.
#
# Key concepts:
# 1. __iter__() returns self
# 2. __next__() returns next value or raises StopIteration
# 3. Stateful iteration
# 4. Consumed after exhaustion
# -----------------------------------------------------------------------------


# =============================================================================
# Creating an Iterator
# =============================================================================


class Counter:
    """Iterator that counts from start to end."""

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


counter = Counter(1, 5)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3


# =============================================================================
# Iterator is Consumed
# =============================================================================


counter = Counter(1, 4)
items = list(counter)
print(f"Items: {items}")
print(f"Again: {list(counter)}")  # empty — consumed


# =============================================================================
# Fibonacci Iterator
# =============================================================================


class Fibonacci:
    """Infinite Fibonacci sequence iterator."""

    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value


fib = Fibonacci()
first_10 = [next(fib) for _ in range(10)]
print(f"Fibonacci: {first_10}")


# =============================================================================
# Practical: File Line Iterator
# =============================================================================


class LineReader:
    """Read lines from a file one at a time."""

    def __init__(self, filepath):
        self.filepath = filepath
        self._file = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._file is None:
            self._file = open(self.filepath)
        line = self._file.readline()
        if not line:
            self._file.close()
            raise StopIteration
        return line.rstrip("\n")


def main():
    print("=== Iterator ===")
    c = Counter(5, 10)
    print(f"Counter: {list(c)}")
    fib = Fibonacci()
    print(f"First 8: {[next(fib) for _ in range(8)]}")


if __name__ == "__main__":
    main()
