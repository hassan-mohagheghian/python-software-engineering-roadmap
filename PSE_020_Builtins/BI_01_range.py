# Builtins - range()
# -----------------------------------------------------------------------------
# range() generates a sequence of numbers. It is commonly used for
# looping a specific number of times in for loops.
#
# Key concepts:
# 1. range(stop) — 0 to stop-1
# 2. range(start, stop) — start to stop-1
# 3. range(start, stop, step) — custom step
# 4. Converting to list for inspection
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Range
# =============================================================================


for i in range(5):
    print(i, end=" ")
print()


# =============================================================================
# Start and Stop
# =============================================================================


for i in range(2, 8):
    print(i, end=" ")
print()


# =============================================================================
# With Step
# =============================================================================


# Even numbers
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# Countdown
for i in range(10, 0, -1):
    print(i, end=" ")
print()


# =============================================================================
# Converting to List
# =============================================================================


print(f"range(5): {list(range(5))}")
print(f"range(1, 6): {list(range(1, 6))}")
print(f"range(0, 10, 3): {list(range(0, 10, 3))}")


# =============================================================================
# Common Patterns
# =============================================================================


# Repeat N times
for _ in range(3):
    print("Hello", end=" ")
print()

# Index-based loop
items = ["a", "b", "c"]
for i in range(len(items)):
    print(f"  [{i}] {items[i]}")


def main():
    print("=== range() ===")
    print(f"range(5) length: {len(range(5))}")
    print(f"In 100: {50 in range(100)}")
    print(f"In range: {15 in range(10, 20)}")


if __name__ == "__main__":
    main()
