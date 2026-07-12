# Iterators & Generators - Iterable
# -----------------------------------------------------------------------------
# An iterable is any object that can be iterated over (list, str, dict, etc.).
# It implements __iter__() which returns an iterator.
#
# Key concepts:
# 1. Iterable vs iterator
# 2. __iter__() protocol
# 3. for loop mechanism
# 4. Checking iterability
# -----------------------------------------------------------------------------


# =============================================================================
# What is Iterable?
# =============================================================================


# Lists, strings, dicts, sets, tuples — all are iterables
my_list = [1, 2, 3]
my_string = "hello"
my_dict = {"a": 1, "b": 2}

for item in my_list:
    print(item, end=" ")
print()

for char in my_string:
    print(char, end=" ")
print()


# =============================================================================
# The __iter__ Method
# =============================================================================


# Every iterable has __iter__ that returns an iterator
print(f"list has __iter__: {hasattr(my_list, '__iter__')}")
print(f"int has __iter__: {hasattr(42, '__iter__')}")


# =============================================================================
# for Loop De-sugar
# =============================================================================


# for x in iterable: is equivalent to:
it = iter(my_list)  # calls __iter__
while True:
    try:
        x = next(it)  # calls __next__
        print(x, end=" ")
    except StopIteration:
        break
print()


# =============================================================================
# Custom Iterable
# =============================================================================


class CountRange:
    """A simple iterable that yields numbers."""

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        current = self.start
        while current < self.end:
            yield current
            current += 1


for num in CountRange(1, 6):
    print(num, end=" ")
print()


def main():
    print("=== Iterable ===")
    data = [10, 20, 30]
    it = iter(data)
    print(f"First: {next(it)}")
    print(f"Second: {next(it)}")


if __name__ == "__main__":
    main()
