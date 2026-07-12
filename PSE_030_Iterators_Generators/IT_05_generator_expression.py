# Iterators & Generators - Generator Expressions
# -----------------------------------------------------------------------------
# Generator expressions are concise syntax for creating generators,
# similar to list comprehensions but with parentheses instead of brackets.
#
# Key concepts:
# 1. Syntax: (expr for x in iterable)
# 2. Lazy evaluation
# 3. Memory efficiency
# 4. Passing to functions that accept iterables
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Syntax
# =============================================================================


# List comprehension — creates entire list in memory
squares_list = [x ** 2 for x in range(10)]

# Generator expression — produces values lazily
squares_gen = (x ** 2 for x in range(10))

print(f"List: {squares_list}")
print(f"Generator: {squares_gen}")  # shows generator object

# Consume generator
print(f"Gen values: {list(squares_gen)}")


# =============================================================================
# Lazy Evaluation
# =============================================================================


# This creates a generator — no computation yet
gen = (x * 2 for x in range(1000000))

# Computation happens one item at a time
print(f"First: {next(gen)}")
print(f"Second: {next(gen)}")


# =============================================================================
# Passing to Functions
# =============================================================================


# sum, min, max, any, all accept iterables
total = sum(x ** 2 for x in range(10))
print(f"Sum of squares: {total}")

maximum = max(len(word) for word in ["hi", "hello", "hey"])
print(f"Max length: {maximum}")

has_big = any(x > 50 for x in range(100))
print(f"Any > 50: {has_big}")


# =============================================================================
# Filtering
# =============================================================================


evens = (x for x in range(20) if x % 2 == 0)
print(f"Evens: {list(evens)}")


# =============================================================================
# Nested Generator Expressions
# =============================================================================


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = (x for row in matrix for x in row)
print(f"Flattened: {list(flattened)}")


def main():
    print("=== Generator Expressions ===")
    gen = (x ** 3 for x in range(1, 6))
    print(f"Cubes: {list(gen)}")
    print(f"Sum: {sum(x ** 2 for x in range(1, 11))}")


if __name__ == "__main__":
    main()
