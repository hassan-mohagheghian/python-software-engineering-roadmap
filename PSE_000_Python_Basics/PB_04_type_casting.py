# Python Basics - Type Casting
# -----------------------------------------------------------------------------
# Type casting (type conversion) transforms a value from one type to another.
#
# Key concepts:
# 1. Explicit casting — int(), float(), str(), bool(), list(), tuple(), set(), dict()
# 2. Implicit casting — Python automatically converts in certain contexts.
# 3. Common pitfalls — truncation, ValueError, precision loss.
# 4. Safe conversion patterns — using try/except or custom helpers.
# -----------------------------------------------------------------------------


# =============================================================================
# Numeric Conversions
# =============================================================================


# int to float
x = 10
print(f"int({x}) -> float: {float(x)} ({type(float(x)).__name__})")

# float to int (truncates toward zero, does NOT round)
print(f"float(3.7) -> int: {int(3.7)}")
print(f"float(3.2) -> int: {int(3.2)}")
print(f"float(-3.7) -> int: {int(-3.7)}")

# int to complex
c = complex(3, 4)
print(f"complex(3, 4): {c}")

# float precision
print(f"\nPrecision issue: 0.1 + 0.2 = {0.1 + 0.2}")
print(f"Rounded: {round(0.1 + 0.2, 1)}")


# =============================================================================
# String Conversions
# =============================================================================


# Number to string
print(f"\nstr(42): '{str(42)}'")
print(f"str(3.14): '{str(3.14)}'")
print(f"str(True): '{str(True)}'")

# String to number
print(f"int('42'): {int('42')}")
print(f"float('3.14'): {float('3.14')}")

# String with base
print(f"int('ff', 16): {int('ff', 16)}")  # hex
print(f"int('1010', 2): {int('1010', 2)}")  # binary
print(f"int('77', 8): {int('77', 8)}")  # octal

# Invalid conversions raise ValueError
try:
    int("hello")
except ValueError as e:
    print(f"\nint('hello') -> ValueError: {e}")

try:
    float("abc")
except ValueError as e:
    print(f"float('abc') -> ValueError: {e}")


# =============================================================================
# Boolean Conversions
# =============================================================================


# To bool
print("\n--- Falsy values (bool() returns False) ---")
falsy = [0, 0.0, 0j, "", [], {}, set(), None, False]
for v in falsy:
    print(f"  bool({str(v):>10}) = {bool(v)}")

print("\n--- Truthy values (bool() returns True) ---")
truthy = [1, -1, 3.14, "hello", [1], {"a": 1}, {1}, True]
for v in truthy:
    print(f"  bool({str(v):>10}) = {bool(v)}")

# bool to int
print(f"\nint(True): {int(True)}")
print(f"int(False): {int(False)}")


# =============================================================================
# Sequence Conversions
# =============================================================================


# List conversion
print("\n--- List Conversion ---")
print(f"list('hello'): {list('hello')}")
print(f"list((1, 2, 3)): {list((1, 2, 3))}")
print(f"list({{1, 2, 3}}): {list({1, 2, 3})}")

# Tuple conversion
print("\n--- Tuple Conversion ---")
print(f"tuple([1, 2, 3]): {tuple([1, 2, 3])}")
print(f"tuple('abc'): {tuple('abc')}")

# Set conversion (removes duplicates)
print("\n--- Set Conversion ---")
print(f"set([1, 2, 2, 3]): {set([1, 2, 2, 3])}")
print(f"set('hello'): {set('hello')}")

# Dict conversion
print("\n--- Dict Conversion ---")
pairs = [("a", 1), ("b", 2)]
print(f"dict([('a',1),('b',2)]): {dict(pairs)}")
print(f"dict(name='Alice', age=30): {dict(name='Alice', age=30)}")


# =============================================================================
# Implicit Type Conversion
# =============================================================================


# Python promotes types automatically in arithmetic
x = 10  # int
y = 3.14  # float
z = x + y  # int + float -> float
print(f"\nImplicit: {x} (int) + {y} (float) = {z} ({type(z).__name__})")

# int + complex -> complex
result = 5 + 2j
print(f"Implicit: 5 (int) + 2j (complex) = {result} ({type(result).__name__})")

# bool + int -> int (True=1, False=0)
print(f"Implicit: True + 5 = {True + 5}")
print(f"Implicit: False + 5 = {False + 5}")


# =============================================================================
# Safe Conversion Patterns
# =============================================================================


def safe_int(value, default=0):
    """Convert to int, returning default on failure."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def safe_float(value, default=0.0):
    """Convert to float, returning default on failure."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


print("\n--- Safe Conversion ---")
print(f"safe_int('42'): {safe_int('42')}")
print(f"safe_int('abc'): {safe_int('abc')}")
print(f"safe_int(None): {safe_int(None)}")
print(f"safe_float('3.14'): {safe_float('3.14')}")
print(f"safe_float('hello'): {safe_float('hello')}")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Numeric Casting ===")
    print(f"  float(10) = {float(10)}")
    print(f"  int(3.99) = {int(3.99)} (truncates, not rounds)")
    print(f"  round(3.99) = {round(3.99)} (rounds)")

    print("\n=== String to Number ===")
    print(f"  int('100'): {int('100')}")
    print(f"  float('3.14'): {float('3.14')}")
    print(f"  int('0xff', 16): {int('0xff', 16)}")

    print("\n=== Number to String ===")
    print(f"  str(42): '{str(42)}'")
    print(f"  str(3.14): '{str(3.14)}'")
    print(f"  repr(3.14): '{repr(3.14)}'")

    print("\n=== Boolean Conversion ===")
    values = [0, 1, "", "text", [], [1], None]
    for v in values:
        print(f"  bool({str(v):>8}) = {bool(v)}")

    print("\n=== Collection Conversion ===")
    print(f"  list('abc') = {list('abc')}")
    print(f"  tuple([1,2,3]) = {tuple([1, 2, 3])}")
    print(f"  set([1,1,2,3]) = {set([1, 1, 2, 3])}")

    print("\n=== Implicit Conversion ===")
    print(f"  1 + 2.0 = {1 + 2.0} ({type(1 + 2.0).__name__})")
    print(f"  True + 10 = {True + 10}")


if __name__ == "__main__":
    main()
