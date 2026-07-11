# Builtins - sum(), min(), max()
# -----------------------------------------------------------------------------
# These builtins aggregate numeric sequences. They can also work with
# custom key functions and start values.
#
# Key concepts:
# 1. sum() — total of iterable
# 2. min() / max() — smallest / largest element
# 3. start parameter for sum
# 4. key parameter for min/max
# -----------------------------------------------------------------------------


# =============================================================================
# sum()
# =============================================================================


numbers = [1, 2, 3, 4, 5]
print(f"sum: {sum(numbers)}")
print(f"sum with start: {sum(numbers, start=100)}")


# =============================================================================
# min() and max()
# =============================================================================


print(f"min: {min(numbers)}")
print(f"max: {max(numbers)}")


# Multiple arguments
print(f"max(3, 7, 2): {max(3, 7, 2)}")
print(f"min(3, 7, 2): {min(3, 7, 2)}")


# =============================================================================
# Key Parameter
# =============================================================================


words = ["banana", "apple", "cherry", "date"]
print(f"shortest: {min(words, key=len)}")
print(f"longest: {max(words, key=len)}")


students = [("Alice", 90), ("Bob", 85), ("Charlie", 95)]
print(f"best: {max(students, key=lambda s: s[1])}")
print(f"worst: {min(students, key=lambda s: s[1])}")


# =============================================================================
# Practical Examples
# =============================================================================


# Running total
data = [10, 20, 30, 40]
total = 0
for val in data:
    total += val
    print(f"  Running sum: {total}")


# Find range
temps = [22, 25, 18, 30, 15, 28]
print(f"Temp range: {min(temps)} to {max(temps)}")
print(f"Swing: {max(temps) - min(temps)}")


# Sum of squared differences
def variance(data):
    """Calculate variance of a list."""
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)


values = [2, 4, 4, 4, 5, 5, 7, 9]
print(f"Variance: {variance(values):.2f}")


def main():
    print("=== sum, min, max ===")
    nums = [5, 2, 8, 1, 9, 3]
    print(f"Sum: {sum(nums)}")
    print(f"Min: {min(nums)}")
    print(f"Max: {max(nums)}")


if __name__ == "__main__":
    main()
