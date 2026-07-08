# Functions - Lambda
# -----------------------------------------------------------------------------
# Lambdas are small anonymous functions defined with the lambda keyword.
# They are limited to a single expression and are often used for short,
# one-off operations.
#
# Key concepts:
# 1. lambda syntax: lambda args: expression
# 2. Common with map, filter, sorted
# 3. When to use lambda vs def
# -----------------------------------------------------------------------------


# =============================================================================
# Lambda Basics
# =============================================================================


square = lambda x: x**2  # noqa: E731
add = lambda a, b: a + b  # noqa: E731

print(f"square(5) = {square(5)}")
print(f"add(3, 4) = {add(3, 4)}")


# =============================================================================
# Lambda with map
# =============================================================================


numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled: {doubled}")


# =============================================================================
# Lambda with filter
# =============================================================================


evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")


# =============================================================================
# Lambda with sorted
# =============================================================================


students = [("Alice", 90), ("Bob", 85), ("Charlie", 95)]
by_grade = sorted(students, key=lambda s: s[1], reverse=True)
print(f"By grade: {by_grade}")

words = ["banana", "apple", "cherry"]
by_length = sorted(words, key=lambda w: len(w))
print(f"By length: {by_length}")


# =============================================================================
# Lambda in data structures
# =============================================================================


operations = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
}

print(f"add: {operations['add'](10, 5)}")
print(f"mul: {operations['mul'](10, 5)}")


# =============================================================================
# Lambda Capture — The Classic Gotcha
# =============================================================================


# Lambdas capture variables BY REFERENCE, not by value.
# This means the lambda follows the variable, not the value at creation time.


# --- Broken: all lambdas share the same 'i' ---

functions_broken = [lambda: i for i in range(5)]
print(f"Broken:   {[f() for f in functions_broken]}")  # [4, 4, 4, 4, 4]


# --- Fixed: bind 'i' at definition time using a default argument ---

functions_fixed = [lambda i=i: i for i in range(5)]
print(f"Fixed:    {[f() for f in functions_fixed]}")  # [0, 1, 2, 3, 4]


# --- Rule of thumb ---
# If a lambda captures a loop variable and executes LATER (not immediately),
# bind it with a default arg (x=x) at definition time.
# If the lambda executes immediately in the same iteration, capturing by
# reference is fine.


def main():
    print("=== Lambda ===")
    print(f"Square: {square(7)}")
    print(f"Doubled: {list(map(lambda x: x * 3, [1, 2, 3]))}")
    print(f"Filtered: {list(filter(lambda x: x > 2, [1, 2, 3, 4, 5]))}")


if __name__ == "__main__":
    main()
