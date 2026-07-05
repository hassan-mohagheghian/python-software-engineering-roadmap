# Data Structures - Dictionaries as Maps
# -----------------------------------------------------------------------------
# Dictionaries are hash maps — they store key-value pairs with O(1) lookup.
# Python dicts are insertion-ordered since 3.7.
#
# Key concepts:
# 1. Basic operations — create, access, update, delete.
# 2. Dictionary comprehensions — {expr for item in iterable}.
# 3. defaultdict — auto-creates missing keys.
# 4. Counter — counts occurrences efficiently.
# 5. Nested dicts — hierarchical data.
# -----------------------------------------------------------------------------


from collections import Counter, defaultdict


# =============================================================================
# Basic Operations
# =============================================================================


def basic_operations():
    # Create
    user = {"name": "Alice", "age": 30, "city": "NYC"}

    # Access
    print(f"  name: {user['name']}")
    print(f"  get (missing): {user.get('email', 'N/A')}")

    # Update
    user["age"] = 31
    user["email"] = "alice@example.com"
    print(f"  updated: {user}")

    # Delete
    del user["city"]
    print(f"  after delete: {user}")

    # Check existence
    print(f"  'name' in user: {'name' in user}")


# =============================================================================
# Dictionary Comprehensions
# =============================================================================


def comprehensions():
    # Squares
    squares = {x: x**2 for x in range(1, 6)}
    print(f"  squares: {squares}")

    # Filter
    even_squares = {k: v for k, v in squares.items() if k % 2 == 0}
    print(f"  even squares: {even_squares}")

    # Invert
    inverted = {v: k for k, v in squares.items()}
    print(f"  inverted: {inverted}")


# =============================================================================
# defaultdict and Counter
# =============================================================================


def defaultdict_demo():
    # Group words by first letter
    words = ["apple", "banana", "avocado", "blueberry", "cherry", "cranberry"]
    grouped = defaultdict(list)
    for word in words:
        grouped[word[0]].append(word)
    print(f"  grouped: {dict(grouped)}")


def counter_demo():
    text = "hello world hello python world hello"
    counts = Counter(text.split())
    print(f"  counts: {counts}")
    print(f"  most common 2: {counts.most_common(2)}")


# =============================================================================
# Nested Dictionaries
# =============================================================================


def nested_demo():
    school = {
        "class_A": {"teacher": "Mr. Smith", "students": ["Alice", "Bob"]},
        "class_B": {"teacher": "Ms. Jones", "students": ["Charlie", "Diana"]},
    }
    for cls, info in school.items():
        print(f"  {cls}: {info['teacher']} — {info['students']}")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Basic Operations ===")
    basic_operations()

    print("\n=== Comprehensions ===")
    comprehensions()

    print("\n=== defaultdict ===")
    defaultdict_demo()

    print("\n=== Counter ===")
    counter_demo()

    print("\n=== Nested Dictionaries ===")
    nested_demo()


if __name__ == "__main__":
    main()
