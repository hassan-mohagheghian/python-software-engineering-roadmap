# Data Structures - Sets and Relationships
# -----------------------------------------------------------------------------
# Sets are unordered collections of unique elements with O(1) lookup.
# They support mathematical set operations: union, intersection, difference.
#
# Key concepts:
# 1. Set operations — union, intersection, difference, symmetric difference.
# 2. Set comprehensions — {expr for item in iterable}.
# 3. Frozen sets — immutable sets that can be dictionary keys.
# 4. Real-world uses — deduplication, membership testing, relationships.
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Set Operations
# =============================================================================


def basic_operations():
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}

    print(f"  a = {a}")
    print(f"  b = {b}")
    print(f"  Union: {a | b}")
    print(f"  Intersection: {a & b}")
    print(f"  Difference (a-b): {a - b}")
    print(f"  Symmetric diff: {a ^ b}")


# =============================================================================
# Set Comprehensions
# =============================================================================


def comprehensions():
    words = ["hello", "world", "hello", "python", "world"]
    unique_lengths = {len(w) for w in words}
    print(f"  unique lengths: {unique_lengths}")

    first_letters = {w[0] for w in words}
    print(f"  first letters: {first_letters}")


# =============================================================================
# Frozen Sets
# =============================================================================


def frozen_set_demo():
    # Frozen sets are immutable — can be dict keys or set elements
    fs = frozenset([1, 2, 3])
    cache = {fs: "cached value"}
    print(f"  frozen set as key: {cache[fs]}")


# =============================================================================
# Real-World: Deduplication and Membership
# =============================================================================


def deduplication():
    ids = [1, 2, 3, 2, 1, 4, 5, 3]
    unique = list(set(ids))
    print(f"  original: {ids}")
    print(f"  deduplicated: {unique}")


def membership_testing():
    large_set = set(range(1_000_000))
    print(f"  999999 in set: {999999 in large_set}")
    print(f"  1000000 in set: {1000000 in large_set}")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Basic Operations ===")
    basic_operations()

    print("\n=== Comprehensions ===")
    comprehensions()

    print("\n=== Frozen Sets ===")
    frozen_set_demo()

    print("\n=== Deduplication ===")
    deduplication()

    print("\n=== Membership Testing ===")
    membership_testing()


if __name__ == "__main__":
    main()
