# Python Basics - Unpacking
# -----------------------------------------------------------------------------
# Unpacking assigns elements from an iterable to variables in a single statement.
#
# Key concepts:
# 1. Basic unpacking — a, b, c = iterable
# 2. Star unpacking — a, *b, c = iterable (collect remaining)
# 3. Nested unpacking — unpacking within unpacking
# 4. Swapping — a, b = b, a
# 5. Function arguments — *args and **kwargs
# 6. Ignoring values — _ for throwaway variables
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Unpacking
# =============================================================================


# Unpack a tuple
point = (3, 4)
x, y = point
print(f"Point: x={x}, y={y}")

# Unpack a list
colors = ["red", "green", "blue"]
r, g, b = colors
print(f"Colors: {r}, {g}, {b}")

# Unpack a string
a, b, c = "Hi!"
print(f"String: a={a}, b={b}, c={c}")

# Unpack a range
first, second, third = range(3)
print(f"Range: {first}, {second}, {third}")


# =============================================================================
# Star Unpacking
# =============================================================================


# Collect remaining items into a list
first, *rest = [1, 2, 3, 4, 5]
print(f"\nfirst={first}, rest={rest}")

# Collect in the middle
first, *middle, last = [1, 2, 3, 4, 5]
print(f"first={first}, middle={middle}, last={last}")

# Collect at the end
first, second, *rest = [1, 2, 3, 4, 5]
print(f"first={first}, second={second}, rest={rest}")

# Collect at the start
*init, last = [1, 2, 3, 4, 5]
print(f"init={init}, last={last}")


# =============================================================================
# Nested Unpacking
# =============================================================================


# Unpack nested structures
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
(a, b, c), (d, e, f), (g, h, i) = matrix
print(f"\nNested: {a},{b},{c} | {d},{e},{f} | {g},{h},{i}")

# Partially nested
data = (1, (2, 3), 4)
a, (b, c), d = data
print(f"Partial: a={a}, b={b}, c={c}, d={d}")

# Deeply nested
(((x1, y1), (x2, y2)),) = (((1, 2), (3, 4)),)
print(f"Deep: ({x1},{y1}), ({x2},{y2})")


# =============================================================================
# Swapping Variables
# =============================================================================


# Simple swap
a, b = 1, 2
print(f"\nBefore swap: a={a}, b={b}")
a, b = b, a
print(f"After swap:  a={a}, b={b}")

# Rotate three variables
a, b, c = 1, 2, 3
print(f"\nBefore rotate: a={a}, b={b}, c={c}")
a, b, c = c, a, b
print(f"After rotate:  a={a}, b={b}, c={c}")


# =============================================================================
# Ignoring Values
# =============================================================================


# Use _ for values you don't need
record = ("Alice", 30, "NYC", "Engineer")
name, _, city, _ = record
print(f"\nName: {name}, City: {city}")

# *s_ to ignore multiple values
first, *_, last = range(10)
print(f"First: {first}, Last: {last}")

# _ in loops
for _ in range(3):
    print("  Repeated message")


# =============================================================================
# Unpacking in Function Calls
# =============================================================================


def print_info(name, age, city):
    print(f"  {name}, {age}, {city}")


# * for positional args from a list
args = ["Alice", 30, "NYC"]
print("\n--- *args unpacking ---")
print_info(*args)

# ** for keyword args from a dict
kwargs = {"name": "Bob", "age": 25, "city": "LA"}
print("\n--- **kwargs unpacking ---")
print_info(**kwargs)

# Combine
print("\n--- Combined ---")
print_info("Charlie", **{"age": 35, "city": "Chicago"})


# =============================================================================
# Unpacking in Data Structures
# =============================================================================


# Merge lists with unpacking
list1 = [1, 2]
list2 = [3, 4]
merged = [*list1, *list2, 5, 6]
print(f"\nMerged lists: {merged}")

# Merge dicts with unpacking
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(f"Merged dicts: {merged}")

# Override keys
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 99, "c": 3}
merged = {**dict1, **dict2}
print(f"With override: {merged}")


# =============================================================================
# Advanced Patterns
# =============================================================================


# Unpack and filter
data = [1, 2, 3, 4, 5, 6]
first, *evens, last = [x for x in data if x % 2 == 0]
print(f"\nEvens from filtered: first={first}, middle={evens}, last={last}")

# Unpack with walrus operator (Python 3.8+)
numbers = [1, 2, 3, 4, 5]
first, *rest = numbers
if (total := sum(rest)) > 10:
    print(f"\nTotal of rest ({rest}) = {total}")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Basic Unpacking ===")
    coords = (10, 20, 30)
    x, y, z = coords
    print(f"  x={x}, y={y}, z={z}")

    print("\n=== Star Unpacking ===")
    numbers = [1, 2, 3, 4, 5]
    first, *middle, last = numbers
    print(f"  first={first}, middle={middle}, last={last}")

    print("\n=== Swapping ===")
    a, b = "hello", "world"
    print(f"  Before: a={a}, b={b}")
    a, b = b, a
    print(f"  After:  a={a}, b={b}")

    print("\n=== Nested Unpacking ===")
    pairs = [(1, 2), (3, 4), (5, 6)]
    for x, y in pairs:
        print(f"  ({x}, {y})")

    print("\n=== Ignore Values ===")
    data = ("Alice", 30, "Engineer")
    name, _, role = data
    print(f"  Name: {name}, Role: {role}")

    print("\n=== Function Unpacking ===")

    def greet(name, greeting="Hello"):
        print(f"  {greeting}, {name}!")

    greet(*["World"])
    greet(**{"name": "Python", "greeting": "Hi"})

    print("\n=== Merge with Unpacking ===")
    print(f"  Lists: {[*[1, 2], *[3, 4]]}")
    print(f"  Dicts: { {**{'a': 1}, **{'b': 2}} }")


if __name__ == "__main__":
    main()
