# Python Basics - Loops
# -----------------------------------------------------------------------------
# Loops allow you to execute a block of code repeatedly.
#
# Key concepts:
# 1. for loop — iterate over sequences (lists, strings, ranges, dicts).
# 2. while loop — repeat while a condition is true.
# 3. range() — generate sequences of numbers.
# 4. break / continue / else — control loop flow.
# 5. Nested loops — loops inside loops.
# 6. Itertools — advanced iteration patterns.
# -----------------------------------------------------------------------------


# =============================================================================
# For Loop Basics
# =============================================================================


# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterate over a string
for char in "Python":
    print(char, end=" ")
print()

# Iterate with index using enumerate()
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Iterate over a dictionary
person = {"name": "Alice", "age": 30, "city": "NYC"}
for key, value in person.items():
    print(f"{key} = {value}")


# =============================================================================
# Range Function
# =============================================================================


# range(stop)
print("\nrange(5):", list(range(5)))

# range(start, stop)
print("range(2, 6):", list(range(2, 6)))

# range(start, stop, step)
print("range(0, 10, 2):", list(range(0, 10, 2)))
print("range(10, 0, -1):", list(range(10, 0, -1)))


# =============================================================================
# While Loop
# =============================================================================


# Basic while loop
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
print()

# While with user input (simulated)
def get_valid_input():
    attempts = 0
    while attempts < 3:
        # Simulating valid input after 2 attempts
        value = 10 if attempts >= 2 else -1
        if value > 0:
            return value
        print(f"Invalid input, attempt {attempts + 1}")
        attempts += 1
    return None

result = get_valid_input()
print(f"Got valid input: {result}")


# =============================================================================
# Break and Continue
# =============================================================================


# break — exit the loop early
print("\n--- break example ---")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

# continue — skip to next iteration
print("\n--- continue example ---")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()


# =============================================================================
# For-Else and While-Else
# =============================================================================


# The else block runs only if the loop completed without break
def find_item(items: list, target):
    for item in items:
        if item == target:
            print(f"Found {target}")
            break
    else:
        print(f"{target} not found")

find_item([1, 2, 3, 4, 5], 3)
find_item([1, 2, 3, 4, 5], 9)


# =============================================================================
# Nested Loops
# =============================================================================


# Multiplication table
print("\n--- Multiplication Table (1-5) ---")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:4}", end="")
    print()

# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = []
for row in matrix:
    for val in row:
        flat.append(val)
print(f"\nFlattened: {flat}")


# =============================================================================
# Loop with Zip
# =============================================================================


names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
grades = ["B", "A", "C"]

print("\n--- Zip Example ---")
for name, score, grade in zip(names, scores, grades):
    print(f"{name}: {score} ({grade})")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== For Loop with Range ===")
    for i in range(1, 6):
        print(f"  {i} squared = {i ** 2}")

    print("\n=== While Loop ===")
    n, factorial = 5, 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    print(f"  {n}! = {factorial}")

    print("\n=== Break Example ===")
    for i in range(100):
        if i ** 2 > 50:
            print(f"  First i where i^2 > 50: {i}")
            break

    print("\n=== Continue Example ===")
    total = 0
    for i in range(1, 11):
        if i % 3 == 0:
            continue
        total += i
    print(f"  Sum of 1-10 excluding multiples of 3: {total}")

    print("\n=== Nested Loop ===")
    for i in range(3):
        for j in range(3):
            print(f"({i},{j})", end=" ")
        print()

    print("\n=== Enumerate ===")
    colors = ["red", "green", "blue"]
    for idx, color in enumerate(colors, start=1):
        print(f"  {idx}. {color}")


if __name__ == "__main__":
    main()
