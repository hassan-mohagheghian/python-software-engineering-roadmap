# Python Basics - Truthy and Falsy
# -----------------------------------------------------------------------------
# In Python, every value has a boolean context. Truthy values evaluate to True
# and falsy values evaluate to False in conditional expressions.
#
# Key concepts:
# 1. Falsy values — 0, 0.0, 0j, "", [], {}, set(), None, False
# 2. Truthy values — everything else
# 3. bool() — explicit conversion to boolean
# 4. Custom truthiness — __bool__() and __len__() dunder methods
# 5. Practical patterns — default values, guard clauses, short-circuit
# -----------------------------------------------------------------------------


# =============================================================================
# Falsy Values
# =============================================================================


print("--- Falsy Values ---")
falsy_values = [
    (0, "int zero"),
    (0.0, "float zero"),
    (0j, "complex zero"),
    (0.00, "float zero"),
    ("", "empty string"),
    ([], "empty list"),
    ((), "empty tuple"),
    ({}, "empty dict"),
    (set(), "empty set"),
    (frozenset(), "empty frozenset"),
    (None, "None"),
    (False, "False"),
    (b"", "empty bytes"),
    (range(0), "empty range"),
]

for value, label in falsy_values:
    print(f"  bool({label:>15}) = {bool(value)}")


# =============================================================================
# Truthy Values
# =============================================================================


print("\n--- Truthy Values ---")
truthy_values = [
    (1, "int one"),
    (-1, "negative int"),
    (3.14, "float"),
    ("hello", "non-empty string"),
    (" ", "space string"),
    ("0", "string '0'"),
    ([1], "non-empty list"),
    ((1,), "non-empty tuple"),
    ({"a": 1}, "non-empty dict"),
    ({0}, "set with zero"),
    (True, "True"),
    (object(), "object"),
]

for value, label in truthy_values:
    print(f"  bool({label:>20}) = {bool(value)}")


# =============================================================================
# Truthiness in Conditionals
# =============================================================================


# Direct use in if statements
name = "Alice"
if name:
    print(f"\nName is set: {name}")

empty_list = []
if not empty_list:
    print("List is empty")

# Check for None
value = None
if value is None:
    print("Value is None")


# =============================================================================
# Common Patterns
# =============================================================================


# Pattern 1: Default values using or
def get_greeting(name):
    return name or "Anonymous"


print(f"\nget_greeting('Alice'): {get_greeting('Alice')}")
print(f"get_greeting(''):      {get_greeting('')}")
print(f"get_greeting(None):    {get_greeting(None)}")


# Pattern 2: Guard clauses
def process_data(data):
    if not data:
        return "No data to process"
    return f"Processed {len(data)} items"


print(f"\nprocess_data([1,2,3]): {process_data([1, 2, 3])}")
print(f"process_data([]):      {process_data([])}")

# Pattern 3: Counting with truthiness
items = [0, 1, "", "hello", None, [1], [], True]
true_count = sum(bool(x) for x in items)
print(f"\nTruthy items in {items}: {true_count}")

# Pattern 4: Filter with bool
filtered = list(filter(None, [0, 1, "", "hello", None, [1]]))
print(f"filter(None, ...): {filtered}")


# =============================================================================
# Custom Truthiness with __bool__ and __len__
# =============================================================================


class PositiveNumber:
    """A number that is truthy when positive."""

    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return self.value > 0


print("\n--- Custom __bool__ ---")
a = PositiveNumber(5)
b = PositiveNumber(-3)
print(f"PositiveNumber(5) is truthy: {bool(a)}")
print(f"PositiveNumber(-3) is truthy: {bool(b)}")

if a:
    print(f"  {a.value} is positive")
if not b:
    print(f"  {b.value} is not positive")


class Bucket:
    """A collection that is truthy when non-empty (uses __len__)."""

    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


print("\n--- Custom __len__ for truthiness ---")
full = Bucket([1, 2, 3])
empty = Bucket([])
print(f"Bucket([1,2,3]) is truthy: {bool(full)}")
print(f"Bucket([]) is truthy:      {bool(empty)}")


# =============================================================================
# Gotchas
# =============================================================================


print("\n--- Gotchas ---")

# "0" is truthy (non-empty string), but 0 is falsy
print(f"bool('0'): {bool('0')}   (non-empty string)")
print(f"bool(0):   {bool(0)}    (zero)")

# Empty string is falsy, but " " is truthy
print(f"bool(''):  {bool('')}    (empty string)")
print(f"bool(' '): {bool(' ')}   (space)")

# False and 0 are equal but not identical
print(f"\nFalse == 0: {False == 0}")
print(f"False is 0: {False is 0}")  # noqa: F632
print(f"True == 1:  {True == 1}")
print(f"True is 1:  {True is 1}")  # noqa: F632


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Falsy Values ===")
    test_values = [0, 0.0, "", [], None, False, {}, set()]
    for v in test_values:
        print(f"  bool({str(v):>8}) = {bool(v)}")

    print("\n=== Truthy Values ===")
    test_values = [1, -1, "hi", [1], True, {"a": 1}]
    for v in test_values:
        print(f"  bool({str(v):>8}) = {bool(v)}")

    print("\n=== Default Values ===")

    def greet(name):
        return f"Hello, {name or 'World'}!"

    print(f"  {greet('Alice')}")
    print(f"  {greet('')}")
    print(f"  {greet(None)}")

    print("\n=== Truthiness Counting ===")
    data = [0, 1, 2, "", "a", None, True]
    truthy = [x for x in data if x]
    falsy = [x for x in data if not x]
    print(f"  Truthy: {truthy}")
    print(f"  Falsy:  {falsy}")

    print("\n=== Practical: Skip Empty ===")

    def process(items):
        if not items:
            print("  Nothing to process")
            return
        print(f"  Processing {len(items)} items")

    process([])
    process([1, 2, 3])


if __name__ == "__main__":
    main()
