# Builtins - sorted()
# -----------------------------------------------------------------------------
# sorted() returns a new sorted list from any iterable. It does not modify
# the original. The key parameter lets you customize sort order.
#
# Key concepts:
# 1. Basic sorting
# 2. reverse=True for descending
# 3. key parameter for custom sort
# 4. Sorting complex objects
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Sorting
# =============================================================================


numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_nums = sorted(numbers)
print(f"Original: {numbers}")
print(f"Sorted: {sorted_nums}")


# =============================================================================
# Reverse
# =============================================================================


descending = sorted(numbers, reverse=True)
print(f"Descending: {descending}")


# =============================================================================
# Key Parameter
# =============================================================================


words = ["banana", "apple", "cherry", "date"]
by_length = sorted(words, key=len)
print(f"By length: {by_length}")

# Case-insensitive sort
names = ["charlie", "Alice", "bob"]
by_name = sorted(names, key=str.lower)
print(f"By name: {by_name}")


# =============================================================================
# Sorting Tuples/Dicts
# =============================================================================


students = [
    ("Alice", 90),
    ("Bob", 85),
    ("Charlie", 95),
    ("Diana", 92),
]

# Sort by grade (index 1)
by_grade = sorted(students, key=lambda s: s[1], reverse=True)
print(f"By grade: {by_grade}")


# Sort dicts
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]
by_age = sorted(users, key=lambda u: u["age"])
print(f"By age: {[u['name'] for u in by_age]}")


# =============================================================================
# Stable Sort
# =============================================================================


# Python's sort is stable — equal items keep their original order
data = [(1, "b"), (1, "a"), (2, "b"), (1, "c")]
result = sorted(data, key=lambda x: x[0])
print(f"Stable sort: {result}")


def main():
    print("=== sorted() ===")
    nums = [5, 2, 8, 1, 9, 3]
    print(f"Sorted: {sorted(nums)}")
    print(f"By abs: {sorted([-5, 2, -8, 1], key=abs)}")


if __name__ == "__main__":
    main()
