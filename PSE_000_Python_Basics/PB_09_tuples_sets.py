# Python Basics - Tuples and Sets
# -----------------------------------------------------------------------------
# Tuples and Sets are built-in collection types alongside lists and dicts.
#
# Tuples:
# 1. Immutable — cannot be modified after creation.
# 2. Ordered — maintain insertion order.
# 3. Allow duplicates — can contain repeated elements.
# 4. Use cases — fixed collections, dictionary keys, function returns.
#
# Sets:
# 1. Mutable (frozenset is immutable) — can add/remove elements.
# 2. Unordered — no indexing.
# 3. No duplicates — automatically removes duplicates.
# 4. Use cases — membership testing, deduplication, set operations.
# -----------------------------------------------------------------------------

from collections import namedtuple

# =============================================================================
# Tuple Creation
# =============================================================================


# Literal
point = (3, 4)
single = (42,)  # trailing comma required for single-element tuple
mixed = (1, "hello", 3.14, True)

# Constructor
from_list = tuple([1, 2, 3])
from_str = tuple("hello")

print(f"Point: {point}")
print(f"Single: {single}")
print(f"Mixed: {mixed}")
print(f"From list: {from_list}")
print(f"From string: {from_str}")


# =============================================================================
# Tuple Operations
# =============================================================================


a = (1, 2, 3)
b = (4, 5, 6)

# Concatenation
print(f"\nConcat: {a + b}")

# Repetition
print(f"Repeat: {a * 3}")

# Indexing and slicing
print(f"Index [0]: {a[0]}")
print(f"Slice [1:]: {a[1:]}")

# Unpacking
x, y, z = a
print(f"Unpack: x={x}, y={y}, z={z}")

# Swapping
m, n = 10, 20
m, n = n, m
print(f"Swap: m={m}, n={n}")

# Methods
data = (1, 2, 3, 2, 1)
print(f"\nCount of 2: {data.count(2)}")
print(f"Index of 3: {data.index(3)}")
print(f"Length: {len(data)}")


# =============================================================================
# Named Tuples
# =============================================================================


Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"\nNamed tuple: {p}")
print(f"Access by name: x={p.x}, y={p.y}")
print(f"Access by index: x={p[0]}, y={p[1]}")


# =============================================================================
# Set Creation
# =============================================================================


# Literal
fruits = {"apple", "banana", "cherry"}

# Constructor
numbers = set([1, 2, 2, 3, 3, 3])

# From string
chars = set("hello")

# Empty set (NOT {} which is a dict)
empty = set()

print(f"Fruits: {fruits}")
print(f"Numbers (deduped): {numbers}")
print(f"Chars: {chars}")
print(f"Empty: {empty}")


# =============================================================================
# Set Methods
# =============================================================================


s = {1, 2, 3}

# Add
s.add(4)
print(f"\nAfter add(4): {s}")

# Remove (KeyError if missing)
s.remove(3)
print(f"After remove(3): {s}")

# Discard (no error if missing)
s.discard(99)
print(f"After discard(99): {s}")

# Pop (arbitrary element)
popped = s.pop()
print(f"After pop(): {s}, popped: {popped}")

# Update
s.update([10, 20])
print(f"After update([10, 20]): {s}")


# =============================================================================
# Set Operations
# =============================================================================


a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"\nA = {a}")
print(f"B = {b}")

# Union — all elements from both
print(f"A | B (union): {a | b}")

# Intersection — common elements
print(f"A & B (intersection): {a & b}")

# Difference — in A but not in B
print(f"A - B (difference): {a - b}")

# Symmetric difference — in either but not both
print(f"A ^ B (sym_diff): {a ^ b}")

# Subset and superset
c = {1, 2}
print(f"\n{c} subset of {a}: {c.issubset(a)}")
print(f"{a} superset of {c}: {a.issuperset(c)}")

# Disjoint — no common elements
d = {10, 11}
print(f"{a} disjoint with {d}: {a.isdisjoint(d)}")


# =============================================================================
# Set Comprehension
# =============================================================================


squares = {x**2 for x in range(-3, 4)}
print(f"\nSquares of -3 to 3: {squares}")

evens = {x for x in range(20) if x % 2 == 0}
print(f"Evens: {evens}")


# =============================================================================
# Frozenset (Immutable Set)
# =============================================================================


fs = frozenset([1, 2, 3])
print(f"\nFrozenset: {fs}")
# fs.add(4)  # AttributeError — frozenset is immutable


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Tuples ===")
    coords = (10, 20)
    print(f"  Point: {coords}")
    print(f"  x={coords[0]}, y={coords[1]}")

    # Tuple unpacking
    name, age, role = ("Alice", 30, "Engineer")
    print(f"  Unpacked: {name}, {age}, {role}")

    # Tuple as dict key (hashable)
    locations = {(40.7, -74.0): "NYC", (34.0, -118.2): "LA"}
    print(f"  Dict with tuple keys: {locations}")

    print("\n=== Sets ===")
    # Remove duplicates
    nums = [1, 2, 2, 3, 3, 3, 4]
    unique = set(nums)
    print(f"  Unique: {unique}")

    # Set operations
    python_devs = {"Alice", "Bob", "Charlie"}
    js_devs = {"Bob", "Diana", "Eve"}
    both = python_devs & js_devs
    either = python_devs | js_devs
    print(f"  Python only: {python_devs - js_devs}")
    print(f"  JS only: {js_devs - python_devs}")
    print(f"  Both: {both}")
    print(f"  Either: {either}")

    print("\n=== Frozenset ===")
    valid_roles = frozenset(["admin", "editor", "viewer"])
    print(f"  Valid roles: {valid_roles}")
    print(f"  Is 'admin' valid: {'admin' in valid_roles}")


if __name__ == "__main__":
    main()
