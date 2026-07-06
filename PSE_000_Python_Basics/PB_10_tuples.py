# Python Basics - Tuples
# -----------------------------------------------------------------------------
# Tuples are immutable, ordered collections that allow duplicates.
#
# 1. Immutable — cannot be modified after creation.
# 2. Ordered — maintain insertion order.
# 3. Allow duplicates — can contain repeated elements.
# 4. Use cases — fixed collections, dictionary keys, function returns.
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
# Usage
# =============================================================================


def main():
    coords = (10, 20)
    print(f"\nPoint: {coords}")
    print(f"x={coords[0]}, y={coords[1]}")

    # Tuple unpacking
    name, age, role = ("Alice", 30, "Engineer")
    print(f"Unpacked: {name}, {age}, {role}")

    # Tuple as dict key (hashable)
    locations = {(40.7, -74.0): "NYC", (34.0, -118.2): "LA"}
    print(f"Dict with tuple keys: {locations}")


if __name__ == "__main__":
    main()
