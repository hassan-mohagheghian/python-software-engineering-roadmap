# Python Basics - Sets
# -----------------------------------------------------------------------------
# Sets are unordered collections of unique elements.
#
# 1. Mutable (frozenset is immutable) — can add/remove elements.
# 2. Unordered — no indexing.
# 3. No duplicates — automatically removes duplicates.
# 4. Use cases — membership testing, deduplication, set operations.
# -----------------------------------------------------------------------------


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
    # Remove duplicates
    nums = [1, 2, 2, 3, 3, 3, 4]
    unique = set(nums)
    print(f"\nUnique: {unique}")

    # Set operations
    python_devs = {"Alice", "Bob", "Charlie"}
    js_devs = {"Bob", "Diana", "Eve"}
    both = python_devs & js_devs
    either = python_devs | js_devs
    print(f"Python only: {python_devs - js_devs}")
    print(f"JS only: {js_devs - python_devs}")
    print(f"Both: {both}")
    print(f"Either: {either}")

    # Frozenset
    valid_roles = frozenset(["admin", "editor", "viewer"])
    print(f"Valid roles: {valid_roles}")
    print(f"Is 'admin' valid: {'admin' in valid_roles}")


if __name__ == "__main__":
    main()
