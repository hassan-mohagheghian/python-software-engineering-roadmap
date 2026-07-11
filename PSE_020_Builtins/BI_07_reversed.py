# Builtins - reversed()
# -----------------------------------------------------------------------------
# reversed() returns an iterator that accesses the given sequence in reverse.
# It does not modify the original and works with any sequence.
#
# Key concepts:
# 1. Basic reversed usage
# 2. Converting to list
# 3. reversed with strings
# 4. reversed vs [::-1]
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Usage
# =============================================================================


numbers = [1, 2, 3, 4, 5]
for num in reversed(numbers):
    print(num, end=" ")
print()


# =============================================================================
# Converting to List
# =============================================================================


reversed_list = list(reversed(numbers))
print(f"Reversed: {reversed_list}")
print(f"Original unchanged: {numbers}")


# =============================================================================
# With Strings
# =============================================================================


word = "python"
for char in reversed(word):
    print(char, end="")
print()


# =============================================================================
# reversed vs Slicing
# =============================================================================


# Using reversed (iterator, memory efficient)
rev_iter = reversed(numbers)

# Using slicing (creates new list)
rev_slice = numbers[::-1]

print(f"reversed: {list(rev_iter)}")
print(f"slice: {rev_slice}")


# =============================================================================
# Practical: Palindrome Check
# =============================================================================


def is_palindrome(text):
    """Check if text reads the same forwards and backwards."""
    clean = text.lower().replace(" ", "")
    return clean == "".join(reversed(clean))


print(f"'racecar': {is_palindrome('racecar')}")
print(f"'hello': {is_palindrome('hello')}")
print(f"'A man a plan a canal Panama': {is_palindrome('A man a plan a canal Panama')}")


# =============================================================================
# With enumerate
# =============================================================================


for i, val in enumerate(reversed([10, 20, 30])):
    print(f"  {i}: {val}")


def main():
    print("=== reversed() ===")
    data = [1, 2, 3, 4, 5]
    print(f"Reversed: {list(reversed(data))}")
    print(f"Is 'madam' palindrome: {is_palindrome('madam')}")


if __name__ == "__main__":
    main()
