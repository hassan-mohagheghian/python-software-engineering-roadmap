# Python Basics - Mutable vs Immutable
# -----------------------------------------------------------------------------
# In Python, objects are either mutable (can be changed) or immutable (cannot).
#
# Key concepts:
# 1. Immutable — int, float, str, tuple, frozenset, bool, None, bytes
# 2. Mutable — list, dict, set, bytearray, custom objects
# 3. Implications — mutability affects identity, assignment, and function behaviorj
# 4. Safe defaults — avoid mutable default arguments
# 5. Hashability — only immutable objects can be dict keys or set members
# -----------------------------------------------------------------------------

from collections import namedtuple

# =============================================================================
# Immutable Types
# =============================================================================


# Integers are immutable
x = 10
print(f"x = {x}, id: {id(x)}")
x = x + 1  # creates a NEW object
print(f"x = {x}, id: {id(x)} (new object)")

# Strings are immutable
s = "hello"
print(f"\ns = {s}, id: {id(s)}")
s = s + " world"  # creates a NEW string
print(f"s = {s}, id: {id(s)} (new object)")

# Tuples are immutable (but may contain mutable objects)
t = (1, 2, [3, 4])
print(f"\nTuple: {t}")
t[2][0] = 99  # this works — the list inside is mutable
print(f"After modifying list inside tuple: {t}")
# t[0] = 99  # TypeError — can't reassign tuple elements


# =============================================================================
# Mutable Types
# =============================================================================


# Lists are mutable
lst = [1, 2, 3]
print(f"\nlst = {lst}, id: {id(lst)}")
lst.append(4)  # modifies in place
print(f"lst = {lst}, id: {id(lst)} (same object)")

# Dictionaries are mutable
d = {"a": 1, "b": 2}
print(f"\nd = {d}, id: {id(d)}")
d["c"] = 3  # modifies in place
print(f"d = {d}, id: {id(d)} (same object)")

# Sets are mutable
s = {1, 2, 3}
print(f"\ns = {s}, id: {id(s)}")
s.add(4)  # modifies in place
print(f"s = {s}, id: {id(s)} (same object)")


# =============================================================================
# Identity vs Equality with Mutability
# =============================================================================


# Same value, different objects
a = [1, 2, 3]
b = [1, 2, 3]
print(f"\na == b: {a == b}")  # True — same value
print(f"a is b: {a is b}")  # False — different objects

# Assignment creates a reference, not a copy
c = a
print(f"\nc is a: {c is a}")  # True — same object
c.append(4)
print("After c.append(4):")
print(f"  a = {a}")  # a is also modified!
print(f"  c = {c}")

# Immutable types are interned (cached)
x = 256
y = 256
print(f"\n256 is 256: {x is y}")  # True — small ints are cached

x = 257
y = 257
print(f"257 is 257: {x is y}")  # May be False (implementation-dependent)


# =============================================================================
# Function Arguments and Mutability
# =============================================================================


# Mutable default arguments are shared across calls (common gotcha)
def append_to(item, target=[]):
    target.append(item)
    return target


print("\n--- Mutable Default Argument Gotcha ---")
print(f"append_to(1): {append_to(1)}")  # [1]
print(f"append_to(2): {append_to(2)}")  # [1, 2] — NOT [2]!
print(f"append_to(3): {append_to(3)}")  # [1, 2, 3]


# Fix: use None as default
def append_to_fixed(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target


print("\n--- Fixed Version ---")
print(f"append_to_fixed(1): {append_to_fixed(1)}")  # [1]
print(f"append_to_fixed(2): {append_to_fixed(2)}")  # [2]
print(f"append_to_fixed(3): {append_to_fixed(3)}")  # [3]


# =============================================================================
# Immutability and Function Side Effects
# =============================================================================


def modify_immutable(x):
    """Cannot modify the original — creates a new object."""
    x = x + 1
    return x


def modify_mutable(lst):
    """CAN modify the original — changes are visible outside."""
    lst.append(99)


num = 10
result = modify_immutable(num)
print(f"\nImmutable: num={num}, result={result}")

items = [1, 2, 3]
modify_mutable(items)
print(f"Mutable: items={items} (modified in place!)")


# =============================================================================
# Hashability
# =============================================================================


# Immutable objects are hashable (can be dict keys / set members)
point = (3, 4)
locations = {point: "origin"}
print(f"\nDict with tuple key: {locations}")

# Mutable objects are NOT hashable
try:
    key = [1, 2]
    d = {key: "value"}  # pyright: ignore[reportUnhashable]
except TypeError as e:
    print(f"List as dict key: {e}")

# frozenset is immutable and hashable
valid_ids = frozenset([1, 2, 3, 4, 5])
print(f"frozenset in set: {valid_ids}")


# =============================================================================
# Making Immutable Copies
# =============================================================================


# List to tuple (immutable)
lst = [1, 2, 3, 4, 5]
immutable = tuple(lst)
print(f"\nList to tuple: {lst} -> {immutable}")

# Convert dict into an immutable tuple of key-value pairs
d = {"a": 1, "b": 2}
immutable_d = tuple(sorted(d.items()))
print(f"Dict to tuple: {immutable_d}")

# Named tuple for immutable records
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"Named tuple: {p}")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Immutable ===")
    x = 10
    y = x
    x += 1
    print(f"  x={x}, y={y} (y unchanged)")

    s = "hello"
    t = s
    s = s + " world"
    print(f"  s='{s}', t='{t}' (t unchanged)")

    print("\n=== Mutable ===")
    a = [1, 2, 3]
    b = a
    a.append(4)
    print(f"  a={a}")
    print(f"  b={b} (b is same object, also modified)")

    print("\n=== Mutable Default Gotcha ===")

    def bad_append(item, target=[]):
        target.append(item)
        return target

    def good_append(item, target=None):
        if target is None:
            target = []
        target.append(item)
        return target

    print(f"  bad:  {bad_append(1)}, {bad_append(2)}")
    print(f"  good: {good_append(1)}, {good_append(2)}")

    print("\n=== Function Side Effects ===")
    nums = [1, 2, 3]
    nums.append(4)
    print(f"  After append: {nums}")

    print("\n=== Hashability ===")
    print(f"  tuple as key: { {(1, 2): 'point'} }")
    try:
        {[1, 2]: "point"}  # pyright: ignore[reportUnusedExpression, reportUnhashable]
    except TypeError as e:
        print(f"  list as key fails: {e}")


if __name__ == "__main__":
    main()
