# Python Basics - Lists
# -----------------------------------------------------------------------------
# Lists are ordered, mutable collections of items.
#
# Key concepts:
# 1. Creation — literal, list(), list comprehension.
# 2. Indexing and Slicing — accessing elements.
# 3. Methods — append, insert, remove, pop, sort, etc.
# 4. Iteration — for loops, enumerate, zip.
# 5. Copying — shallow vs deep copy.
# 6. Nested lists — 2D arrays, matrices.
# -----------------------------------------------------------------------------

import copy

# =============================================================================
# List Creation
# =============================================================================


# Literal
fruits = ["apple", "banana", "cherry"]

# Constructor
numbers = list(range(1, 6))

# List comprehension
squares = [x**2 for x in range(1, 6)]

# Repeat
zeros = [0] * 5

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")
print(f"Zeros: {zeros}")


# =============================================================================
# Indexing and Slicing
# =============================================================================


colors = ["red", "green", "blue", "yellow", "purple"]

print(f"\nFirst: {colors[0]}")
print(f"Last: {colors[-1]}")
print(f"Slice [1:3]: {colors[1:3]}")
print(f"Slice [::2]: {colors[::2]}")
print(f"Reversed: {colors[::-1]}")


# =============================================================================
# List Methods
# =============================================================================


nums = [3, 1, 4, 1, 5]

# Add elements
nums.append(9)
print(f"\nAfter append(9): {nums}")

nums.insert(0, 0)
print(f"After insert(0, 0): {nums}")

nums.extend([2, 6])
print(f"After extend([2, 6]): {nums}")

# Remove elements
nums.remove(1)  # removes first occurrence
print(f"After remove(1): {nums}")

popped = nums.pop()  # removes and returns last
print(f"After pop(): {nums}, popped: {popped}")

popped = nums.pop(0)  # removes and returns at index
print(f"After pop(0): {nums}, popped: {popped}")

# Search
print(f"\nIndex of 4: {nums.index(4)}")
print(f"Count of 1: {nums.count(1)}")
print(f"Contains 5: {5 in nums}")

# Sort
nums.sort()
print(f"\nSorted: {nums}")

nums.sort(reverse=True)
print(f"Sorted desc: {nums}")

# Reverse
nums.reverse()
print(f"Reversed: {nums}")


# =============================================================================
# List Comprehensions
# =============================================================================


# Basic
squares = [x**2 for x in range(10)]
print(f"\nSquares: {squares}")

# With condition
evens = [x for x in range(20) if x % 2 == 0]
print(f"Evens: {evens}")

# With transformation
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
print(f"Upper: {upper}")

# Nested
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"Matrix: {matrix}")

# Flatten
flat = [x for row in matrix for x in row]
print(f"Flattened: {flat}")


# =============================================================================
# Copying Lists
# =============================================================================


original = [1, 2, [3, 4]]

# Shallow copy — nested objects are shared
shallow = original.copy()
shallow[2][0] = 99
print(f"\nOriginal after shallow copy modify: {original}")

# Deep copy — fully independent

original = [1, 2, [3, 4]]
deep = copy.deepcopy(original)
deep[2][0] = 99
print(f"Original after deep copy modify: {original}")


# =============================================================================
# Nested Lists
# =============================================================================


# 2D list
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("\nGrid:")
for row in grid:
    print(f"  {row}")

# Access element
print(f"Grid[1][2]: {grid[1][2]}")

# Transpose
transposed = [[row[i] for row in grid] for i in range(3)]
print(f"Transposed: {transposed}")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== List Creation ===")
    a = [1, 2, 3, 4, 5]
    b = list("hello")
    c = [x**2 for x in range(6)]
    print(f"  a = {a}")
    print(f"  b = {b}")
    print(f"  c = {c}")

    print("\n=== List Operations ===")
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"  Original: {nums}")
    print(f"  Sorted: {sorted(nums)}")
    print(f"  Sum: {sum(nums)}")
    print(f"  Min: {min(nums)}, Max: {max(nums)}")
    print(f"  Length: {len(nums)}")

    print("\n=== List Comprehension ===")
    evens = [x for x in range(20) if x % 2 == 0]
    print(f"  Even numbers: {evens}")

    words = ["apple", "Banana", "cherry"]
    lowered = [w.lower() for w in words]
    print(f"  Lowered: {lowered}")

    print("\n=== Iteration ===")
    fruits = ["apple", "banana", "cherry"]
    for i, fruit in enumerate(fruits, 1):
        print(f"  {i}. {fruit}")

    print("\n=== Slicing ===")
    data = list(range(10))
    print(f"  Data: {data}")
    print(f"  First 3: {data[:3]}")
    print(f"  Last 3: {data[-3:]}")
    print(f"  Every 2nd: {data[::2]}")
    print(f"  Reversed: {data[::-1]}")


if __name__ == "__main__":
    main()
