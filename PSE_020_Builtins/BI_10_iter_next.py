# Builtins - iter() and next()
# -----------------------------------------------------------------------------
# iter() and next() provide direct access to the iterator protocol.
# iter() converts an iterable to an iterator; next() retrieves items one by one.
#
# Key concepts:
# 1. iter() — create iterator from iterable
# 2. next() — get next item
# 3. Default value for next
# 4. StopIteration exception
# 5. Custom iterators
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Usage
# =============================================================================


numbers = [1, 2, 3]
it = iter(numbers)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # StopIteration


# =============================================================================
# Default Value
# =============================================================================


it = iter([1, 2, 3])
print(next(it, "default"))  # 1
print(next(it, "default"))  # 2
print(next(it, "default"))  # 3
print(next(it, "default"))  # "default" (exhausted)


# =============================================================================
# Manual Iteration
# =============================================================================


def manual_loop(iterable):
    """Iterate without for loop."""
    it = iter(iterable)
    while True:
        try:
            item = next(it)
            print(item, end=" ")
        except StopIteration:
            break
    print()


manual_loop([10, 20, 30])


# =============================================================================
# Custom Iterator
# =============================================================================


class Countdown:
    """Countdown from n to 1."""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


for num in Countdown(5):
    print(num, end=" ")
print()


# =============================================================================
# Practical: peek at first element
# =============================================================================


def peek_first(iterable):
    """Return first element and the rest."""
    it = iter(iterable)
    first = next(it)
    return first, list(it)


first, rest = peek_first([10, 20, 30, 40])
print(f"First: {first}, Rest: {rest}")


def main():
    print("=== iter() and next() ===")
    nums = [5, 10, 15]
    it = iter(nums)
    print(f"First: {next(it)}")
    print(f"Second: {next(it)}")
    print(f"Remaining: {list(it)}")


if __name__ == "__main__":
    main()
