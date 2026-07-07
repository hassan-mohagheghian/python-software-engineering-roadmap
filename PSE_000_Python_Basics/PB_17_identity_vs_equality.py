# Python Basics - Identity vs Equality
# -----------------------------------------------------------------------------
# Identity checks if two variables point to the same object in memory.
# Equality checks if two variables have the same value.
#
# Key concepts:
# 1. == checks value equality (calls __eq__)
# 2. is checks identity (compares memory addresses)
# 3. `is` is for None, True, False — not for value comparison
# 4. Integer caching — small ints (-5 to 256) are cached
# 5. String interning — short strings may share identity
# 6. Mutable objects — same value doesn't mean same object
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Identity vs Equality
# =============================================================================


a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

# Equality
print(f"\na == b: {a == b}")  # True — same value
print(f"a == c: {a == c}")  # True — same value

# Identity
print(f"a is b: {a is b}")  # False — different objects
print(f"a is c: {a is c}")  # True — same object


# =============================================================================
# Immutable Types and Identity
# =============================================================================


# Integers
x = 100
y = 100
print(f"\n100 is 100: {x is y}")  # True — cached

x = 1000
y = 1000
print(f"1000 is 1000: {x is y}")  # May be False (not cached)

# Strings
s1 = "hello"
s2 = "hello"
print(f"\n'hello' is 'hello': {s1 is s2}")  # True — interned

s1 = "hello world!"
s2 = "hello world!"
print(f"'hello world!' is 'hello world!': {s1 is s2}")  # May vary

# Tuples are immutable. `is` checks identity, not equality.
# Do not rely on tuple caching.
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(f"\n(1,2,3) is (1,2,3): {t1 is t2}")


# =============================================================================
# The is Operator
# =============================================================================


# `is` is for singleton comparisons
value = None
print(f"\nvalue is None:     {value is None}")
print(f"value is not None: {value is not None}")

# Boolean identity
print(f"\nTrue is True: {True is True}")
print(f"False is False: {False is False}")


# =============================================================================
# Common Pitfalls
# =============================================================================


# Pitfall 1: `is` checks identity, not value equality
a = 257
b = 257
print(f"\n257 == 257: {a == b}")  # True
print(f"257 is 257: {a is b}")  # May be True or False depending on implementation


# Pitfall 2: Empty containers are different objects
list1 = []
list2 = []
print(f"\n[] == []: {list1 == list2}")  # True (same values)
print(f"[] is []: {list1 is list2}")  # False (different objects)


# Pitfall 3: Small integer caching (CPython implementation detail)
x = 256
y = 256
print(f"\n256 is 256: {x is y}")  # Usually True (cached in CPython)
x = 257
y = 257
print(f"257 is 257: {x is y}")  # May be True or False


# Do not rely on object caching.
# Use == for values and `is` for singleton objects like None.
value = None
print(f"\nvalue is None: {value is None}")  # Correct usage of `is`

# =============================================================================
# When to Use is vs ==
# =============================================================================


# USE is for:
# - None checks
# - True/False checks (rare, usually just use truthiness)
# - Checking if two variables reference the same object

value = None
if value is None:  # Correct
    print("\nValue is None")

if value == None:  # Works but not Pythonic  # noqa: E711
    print("Value == None")


# USE == for:
# - Value comparison
# - All other comparisons

a = [1, 2, 3]
b = [1, 2, 3]
if a == b:  # Correct — comparing values
    print("Lists have same values")


# =============================================================================
# Custom Equality
# =============================================================================


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = p1

print(f"\np1 == p2: {p1 == p2}")  # True — same values
print(f"p1 is p2: {p1 is p2}")  # False — different objects
print(f"p1 is p3: {p1 is p3}")  # True — same object


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Identity vs Equality ===")
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    print(f"  a == b: {a == b} (same value)")
    print(f"  a is b: {a is b} (different objects)")
    print(f"  a is c: {a is c} (same object)")

    print("\n=== None Check ===")
    value = None
    print(f"  value is None: {value is None}")
    print(f"  value is not None: {value is not None}")

    print("\n=== Integer Caching ===")
    print(f"  256 is 256: {256 is 256} (cached)")  # noqa: F632
    print(f"  257 is 257: {257 is 257} (may differ)")  # noqa: F632

    print("\n=== String Interning ===")
    s1 = "hello"
    s2 = "hello"
    print(f"  'hello' is 'hello': {s1 is s2} (interned)")

    print("\n=== Custom Class ===")

    class Pair:
        def __init__(self, a, b):
            self.a, self.b = a, b

        def __eq__(self, other):
            return self.a == other.a and self.b == other.b

    p1 = Pair(1, 2)
    p2 = Pair(1, 2)
    print(f"  p1 == p2: {p1 == p2}")
    print(f"  p1 is p2: {p1 is p2}")

    print("\n=== Rule of Thumb ===")
    print("  Use 'is' for None, True, False")
    print("  Use '==' for everything else")


if __name__ == "__main__":
    main()
