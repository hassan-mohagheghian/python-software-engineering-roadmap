# Builtins - map()
# -----------------------------------------------------------------------------
# map() applies a function to every item in an iterable, returning an iterator
# of results. It is a functional programming alternative to list comprehensions.
#
# Key concepts:
# 1. Basic map — apply function to single iterable
# 2. Multiple iterables — apply function to matching elements
# 3. Converting to list
# 4. map vs list comprehension
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Usage
# =============================================================================


numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled: {doubled}")


# =============================================================================
# With Built-in Functions
# =============================================================================


words = ["hello", "world", "python"]
upper_words = list(map(str.upper, words))
print(f"Upper: {upper_words}")

lengths = list(map(len, words))
print(f"Lengths: {lengths}")


# =============================================================================
# Multiple Iterables
# =============================================================================


a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(f"Sum: {sums}")


# =============================================================================
# map vs List Comprehension
# =============================================================================


# Using map
doubled_map = list(map(lambda x: x ** 2, numbers))

# Using list comprehension (usually preferred)
doubled_comp = [x ** 2 for x in numbers]

print(f"map: {doubled_map}")
print(f"comprehension: {doubled_comp}")


# =============================================================================
# Practical Examples
# =============================================================================


# Convert strings to integers
str_numbers = ["1", "2", "3", "4", "5"]
int_numbers = list(map(int, str_numbers))
print(f"Converted: {int_numbers}")


# Apply multiple transformations
def process_item(item):
    """Transform a string item."""
    return item.strip().lower()


raw = ["  Hello ", " WORLD ", " python "]
cleaned = list(map(process_item, raw))
print(f"Cleaned: {cleaned}")


def main():
    print("=== map() ===")
    numbers = [1, 4, 9, 16, 25]
    roots = list(map(lambda x: x ** 0.5, numbers))
    print(f"Roots: {[f'{r:.1f}' for r in roots]}")


if __name__ == "__main__":
    main()
