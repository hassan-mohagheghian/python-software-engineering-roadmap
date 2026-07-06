# Python Basics - Slicing
# -----------------------------------------------------------------------------
# Slicing provides a concise way to access subsequences from sequences.
#
# Key concepts:
# 1. Syntax — sequence[start:stop:step]
# 2. Defaults — start=0, stop=len, step=1
# 3. Negative indices — count from the end
# 4. Slice assignment — modify parts of mutable sequences
# 5. Works on — strings, lists, tuples, ranges, bytes
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Slicing
# =============================================================================


text = "Python"
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"String: {text}")
print(f"List:   {nums}")

# Full slice (copy)
print(f"\ntext[:]:   {text[:]}")
print(f"nums[:]:   {nums[:]}")

# First N elements
print(f"\ntext[:3]:  {nums[:3]}")
print(f"nums[:4]:  {nums[:4]}")

# Last N elements
print(f"\ntext[-3:]: {text[-3:]}")
print(f"nums[-3:]: {nums[-3:]}")

# Middle slice
print(f"\ntext[1:4]: {text[1:4]}")
print(f"nums[2:6]: {nums[2:6]}")


# =============================================================================
# Step Parameter
# =============================================================================


print("\n--- Step ---")
print(f"nums[::2]:  {nums[::2]}")  # every 2nd
print(f"nums[::3]:  {nums[::3]}")  # every 3rd
print(f"nums[1::2]: {nums[1::2]}")  # every 2nd, starting at index 1

# Reverse with step=-1
print(f"\ntext[::-1]:  {text[::-1]}")  # full reverse
print(f"nums[::-1]:  {nums[::-1]}")

# Reverse a slice
print(f"nums[7:2:-1]: {nums[7:2:-1]}")  # from index 7 down to 3


# =============================================================================
# Negative Indices
# =============================================================================


print("\n--- Negative Indices ---")
print(f"text[-1]:   {text[-1]}")  # last char
print(f"text[-2]:   {text[-2]}")  # second to last
print(f"text[:-2]:  {text[:-2]}")  # all but last 2
print(f"text[-3:]:  {text[-3:]}")  # last 3

print(f"\nnums[-3:]:  {nums[-3:]}")  # last 3
print(f"nums[:-3]:  {nums[:-3]}")  # all but last 3
print(f"nums[-4:-1]: {nums[-4:-1]}")  # from 4th-to-last to 2nd-to-last


# =============================================================================
# Slice Objects
# =============================================================================


# Create a slice object
s = slice(1, 5, 2)
print(f"\nslice(1, 5, 2): {nums[s]}")

# Slice object with variables
start, stop, step = 2, 8, 3
print(f"slice({start}, {stop}, {step}): {nums[start:stop:step]}")


# =============================================================================
# Slice Assignment (Mutable Sequences Only)
# =============================================================================


# Lists support slice assignment
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"\nOriginal: {nums}")
nums[2:5] = [20, 30, 40]
print(f"After nums[2:5] = [20,30,40]: {nums}")

# Replace with different length
nums = [0, 1, 2, 3, 4, 5]
print(f"\nOriginal: {nums}")
nums[1:4] = [10]
print(f"After nums[1:4] = [10]: {nums}")

# Delete with slice
nums = [0, 1, 2, 3, 4, 5]
print(f"\nOriginal: {nums}")
nums[1:4] = []
print(f"After nums[1:4] = []: {nums}")

# Insert with slice
nums = [0, 1, 2, 3, 4, 5]
print(f"\nOriginal: {nums}")
nums[2:2] = [20, 30]
print(f"After nums[2:2] = [20,30]: {nums}")

# Strings are immutable — slice assignment doesn't work
try:
    text = "hello"
    text[1:3] = "XY"  # pyright: ignore[reportIndexIssue]
except TypeError as e:
    print(f"\nString slice assignment: {e}")


# =============================================================================
# Common Slicing Patterns
# =============================================================================


# First element
first = nums[:1]
print(f"\nFirst: {first}")

# Last element
last = nums[-1:]
print(f"Last: {last}")

# Every Nth element
every_third = nums[::3]
print(f"Every 3rd: {every_third}")

# Middle half
data = list(range(20))
mid = data[len(data) // 4 : 3 * len(data) // 4]
print(f"Middle half of range(20): {mid}")


# Chunk a list
def chunks(lst, size):
    return [lst[i : i + size] for i in range(0, len(lst), size)]


print(f"Chunks of 3: {chunks(list(range(10)), 3)}")


# =============================================================================
# Slicing with Other Types
# =============================================================================


# Ranges
r = range(20)
print(f"\nrange(20)[5:10]: {list(r[5:10])}")
print(f"range(20)[::5]:  {list(r[::5])}")

# Bytes
b = b"Hello, World!"
print(f"\nbytes[:5]: {b[:5]}")
print(f"bytes[::-1]: {b[::-1]}")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Basic Slicing ===")
    data = list(range(10))
    print(f"  data:        {data}")
    print(f"  data[:3]:    {data[:3]}")
    print(f"  data[3:]:    {data[3:]}")
    print(f"  data[2:7]:   {data[2:7]}")
    print(f"  data[-3:]:   {data[-3:]}")

    print("\n=== Step ===")
    print(f"  data[::2]:   {data[::2]}")
    print(f"  data[1::2]:  {data[1::2]}")
    print(f"  data[::-1]:  {data[::-1]}")
    print(f"  data[::-2]:  {data[::-2]}")

    print("\n=== String Slicing ===")
    word = "Python"
    print(f"  word[:3]:    {word[:3]}")
    print(f"  word[3:]:    {word[3:]}")
    print(f"  word[::-1]:  {word[::-1]}")

    print("\n=== Slice Assignment ===")
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    lst[2:5] = [20, 30, 40]
    print(f"  After lst[2:5] = [20,30,40]: {lst}")

    print("\n=== Chunks ===")
    items = list(range(12))
    print(f"  Chunks of 4: {chunks(items, 4)}")


if __name__ == "__main__":
    main()
