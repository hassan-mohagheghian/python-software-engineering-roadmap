# Builtins - enumerate()
# -----------------------------------------------------------------------------
# enumerate() adds a counter to an iterable, returning (index, value) pairs.
# It eliminates the need for manual index tracking.
#
# Key concepts:
# 1. Basic enumerate with start=0 (default)
# 2. Custom start index
# 3. Unpacking index and value
# 4. When to use enumerate vs manual indexing
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Usage
# =============================================================================


fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")


# =============================================================================
# Custom Start Index
# =============================================================================


for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}. {fruit}")


# =============================================================================
# With range vs enumerate
# =============================================================================


# Without enumerate (manual index)
for i in range(len(fruits)):
    print(f"  [{i}] {fruits[i]}")

# With enumerate (cleaner)
for i, fruit in enumerate(fruits):
    print(f"  [{i}] {fruit}")


# =============================================================================
# Practical Examples
# =============================================================================


# Find index of an item
def find_index(items, target):
    """Return index of target, or -1 if not found."""
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1


print(f"Find 'cherry': {find_index(fruits, 'cherry')}")
print(f"Find 'grape': {find_index(fruits, 'grape')}")


# Numbered output
tasks = ["Write code", "Run tests", "Deploy"]
for num, task in enumerate(tasks, 1):
    print(f"  Task {num}: {task}")


def main():
    print("=== enumerate() ===")
    data = [10, 20, 30, 40]
    for i, val in enumerate(data, start=100):
        print(f"  Key {i}: {val}")


if __name__ == "__main__":
    main()
