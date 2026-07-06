# Python Basics - Comprehensions
# -----------------------------------------------------------------------------
# Comprehensions provide concise syntax to create new sequences from existing ones.
#
# Key concepts:
# 1. List comprehension — [expr for x in iterable if condition]
# 2. Dict comprehension — {key: val for x in iterable}
# 3. Set comprehension — {expr for x in iterable}
# 4. Generator expression — (expr for x in iterable)
# 5. Nested comprehensions — flattening/transforming 2D+ data
# 6. Conditional expressions — inline if/else in comprehensions
# -----------------------------------------------------------------------------


# =============================================================================
# List Comprehensions
# =============================================================================


# Basic
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# With condition (filter)
evens = [x for x in range(20) if x % 2 == 0]
print(f"Evens: {evens}")

# With transformation
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
print(f"Upper: {upper}")

# With if/else (ternary)
labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
print(f"Labels: {labels}")

# Nested loops
pairs = [(x, y) for x in range(3) for y in range(3)]
print(f"Pairs: {pairs}")


# =============================================================================
# Dict Comprehensions
# =============================================================================


# Basic
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"\nSquares dict: {squares_dict}")

# Invert a dict
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(f"Inverted: {inverted}")

# Filter
scores = {"Alice": 85, "Bob": 60, "Charlie": 92, "Diana": 78}
passed = {name: score for name, score in scores.items() if score >= 80}
print(f"Passed: {passed}")

# Transform values
doubled = {k: v * 2 for k, v in scores.items()}
print(f"Doubled: {doubled}")


# =============================================================================
# Set Comprehensions
# =============================================================================


# Basic
unique_lengths = {len(w) for w in ["hello", "world", "hi", "python"]}
print(f"\nUnique lengths: {unique_lengths}")

# From a list
nums = [1, 2, 2, 3, 3, 3, 4]
unique = {x for x in nums}
print(f"Unique from list: {unique}")

# Character frequency
word = "mississippi"
chars = {c for c in word}
print(f"Unique chars in '{word}': {chars}")


# =============================================================================
# Generator Expressions
# =============================================================================


# Parentheses around a comprehension create a generator expression.
# The values are produced lazily, making it memory efficient.
sum_of_squares = sum(x**2 for x in range(1000))
print(f"\nSum of squares (0-999): {sum_of_squares}")

# As a list (materializes)
squares_list = list(x**2 for x in range(10))
print(f"Squares list: {squares_list}")

# Find first match
first_big = next(x for x in range(100) if x > 50)
print(f"First > 50: {first_big}")

# Memory efficient for large data
total = sum(x for x in range(10_000_000) if x % 2 == 0)
print(f"Sum of even numbers to 10M: {total}")


# =============================================================================
# Nested Comprehensions
# =============================================================================


# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(f"\nFlattened: {flat}")

# Create a matrix
transpose = [[row[i] for row in matrix] for i in range(3)]
print(f"Transposed: {transpose}")

# Flatten with condition
data = [[1, 2, 0], [3, 0, 4], [0, 5, 6]]
non_zero = [x for row in data for x in row if x != 0]
print(f"Non-zero flattened: {non_zero}")

# Nested comprehension with dict
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "Diana", "grade": "C"},
]
a_students = [s["name"] for s in students if s["grade"] == "A"]
print(f"A students: {a_students}")


# =============================================================================
# Real-World Patterns
# =============================================================================


# Extract and transform
csv_data = "name,age,city\nAlice,30,NYC\nBob,25,LA"
rows = [line.split(",") for line in csv_data.split("\n")[1:]]
records = [{"name": r[0], "age": int(r[1]), "city": r[2]} for r in rows]
print(f"\nRecords: {records}")

# Group by key
words = ["apple", "banana", "cherry", "avocado", "blueberry"]
by_first = {}
for w in words:
    by_first.setdefault(w[0], []).append(w)
grouped = {k: v for k, v in sorted(by_first.items())}
print(f"Grouped by first letter: {grouped}")

# Flatten with chain
nested = [[1, 2], [3, 4], [5, 6]]
flat = [x for sub in nested for x in sub]
print(f"Flattened: {flat}")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== List Comprehension ===")
    nums = list(range(10))
    print(f"  Original: {nums}")
    print(f"  Squares:  {[x**2 for x in nums]}")
    print(f"  Evens:    {[x for x in nums if x % 2 == 0]}")

    print("\n=== Dict Comprehension ===")
    names = ["alice", "bob", "charlie"]
    print(f"  Lengths:  { {n: len(n) for n in names} }")

    print("\n=== Set Comprehension ===")
    data = [1, 2, 2, 3, 3, 3]
    print(f"  Unique:   { {x for x in data} }")

    print("\n=== Generator ===")
    total = sum(x**2 for x in range(10))
    print(f"  Sum of squares: {total}")

    print("\n=== Nested ===")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"  Flat:     {[x for row in matrix for x in row]}")
    print(f"  Transpose:{[[row[i] for row in matrix] for i in range(3)]}")

    print("\n=== Conditional Expression ===")
    nums = range(6)
    print(f"  Labels:   {['even' if x % 2 == 0 else 'odd' for x in nums]}")


if __name__ == "__main__":
    main()
