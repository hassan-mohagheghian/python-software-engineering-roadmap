# Builtins - filter()
# -----------------------------------------------------------------------------
# filter() extracts elements from an iterable for which a function returns True.
# It returns an iterator of matching elements.
#
# Key concepts:
# 1. Basic filter — keep elements where function returns True
# 2. filter(None, ...) — remove falsy values
# 3. filter vs list comprehension
# 4. Practical filtering patterns
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Usage
# =============================================================================


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")


# =============================================================================
# filter(None, ...) — Remove Falsy Values
# =============================================================================


mixed = [0, 1, "", "hello", None, [], [1], False, True, 42]
truthy = list(filter(None, mixed))
print(f"Truthy: {truthy}")


# =============================================================================
# filter vs List Comprehension
# =============================================================================


# Using filter
evens_filter = list(filter(lambda x: x % 2 == 0, numbers))

# Using list comprehension (usually preferred)
evens_comp = [x for x in numbers if x % 2 == 0]

print(f"filter: {evens_filter}")
print(f"comprehension: {evens_comp}")


# =============================================================================
# With Named Functions
# =============================================================================


def is_positive(n):
    return n > 0


def is_long_word(word):
    return len(word) > 4


temperatures = [-5, 12, 0, 22, -3, 35, 18]
positive = list(filter(is_positive, temperatures))
print(f"Positive temps: {positive}")

words = ["hi", "hello", "hey", "python", "go", "javascript"]
long_words = list(filter(is_long_word, words))
print(f"Long words: {long_words}")


# =============================================================================
# Practical: Filter and Transform
# =============================================================================


# Chain filter and map
numbers = range(1, 21)
result = list(map(lambda x: x ** 2, filter(lambda x: x % 3 == 0, numbers)))
print(f"Squares of multiples of 3: {result}")


def main():
    print("=== filter() ===")
    data = [1, -2, 3, -4, 5, -6]
    pos = list(filter(lambda x: x > 0, data))
    print(f"Positive: {pos}")
    non_empty = list(filter(None, ["", "a", "", "b", ""]))
    print(f"Non-empty: {non_empty}")


if __name__ == "__main__":
    main()
