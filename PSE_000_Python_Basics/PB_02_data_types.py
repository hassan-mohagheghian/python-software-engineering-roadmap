# Python Basics - Data Types
# -----------------------------------------------------------------------------
# Python has several built-in data types organized into categories:
#
# 1. Numeric: int, float, complex
# 2. Text: str
# 3. Boolean: bool
# 4. Sequence: list, tuple, range
# 5. Mapping: dict
# 6. Set: set, frozenset
# 7. None: NoneType
#
# Python is dynamically typed — types are determined at runtime, not declared.
# -----------------------------------------------------------------------------


# =============================================================================
# Numeric Types
# =============================================================================


# Integer (int) — unlimited precision
big_int = 999999999999999999999999999999
print(f"Integer: {big_int}, type: {type(big_int).__name__}")

# Float — 64-bit double precision
pi = 3.14159265358979
print(f"Float: {pi}, type: {type(pi).__name__}")

# Complex — real + imaginary parts
z = 3 + 4j
print(f"Complex: {z}, real: {z.real}, imaginary: {z.imag}")


# =============================================================================
# Boolean Type
# =============================================================================


is_active = True
is_deleted = False
print(f"Bool: {is_active}, {is_deleted}")

# Truthy and Falsy values
print("\n--- Truthy/Falsy ---")
print(f"bool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f"bool(''): {bool('')}")
print(f"bool('hello'): {bool('hello')}")
print(f"bool([]): {bool([])}")
print(f"bool([1]): {bool([1])}")
print(f"bool(None): {bool(None)}")


# =============================================================================
# String Type
# =============================================================================


single = "hello"
double = "hello"
multi = """This is
a multi-line
string"""

print(f"Single: {single}")
print(f"Double: {double}")
print(f"Multi-line:\n{multi}")

# String operations
name = "Python"
print(f"\nUppercase: {name.upper()}")
print(f"Lowercase: {name.lower()}")
print(f"Length: {len(name)}")
print(f"Replace: {name.replace('Py', 'Cy')}")
print(f"Slicing: {name[0:3]}")


# =============================================================================
# None Type
# =============================================================================


result = None
print(f"\nNone value: {result}")
print(f"Type: {type(result).__name__}")
print(f"Is None: {result is None}")


# =============================================================================
# Type Checking and Conversion
# =============================================================================


print("\n--- Type Checking ---")
print(f"type(42): {type(42)}")
print(f"isinstance(42, int): {isinstance(42, int)}")
print(f"isinstance(42, (int, float)): {isinstance(42, (int, float))}")

print("\n--- Type Conversion ---")
# int -> float
x = float(10)
print(f"float(10) = {x} ({type(x).__name__})")

# float -> int (truncates)
y = int(3.99)
print(f"int(3.99) = {y}")

# str -> int
z = int("42")
print(f"int('42') = {z}")

# int -> str
s = str(100)
print(f"str(100) = '{s}' ({type(s).__name__})")

# str -> list
chars = list("hello")
print(f"list('hello') = {chars}")

# list -> tuple
t = tuple([1, 2, 3])
print(f"tuple([1,2,3]) = {t}")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Numeric Types ===")
    a, b, c = 42, 3.14, 2 + 3j
    print(f"int: {a}, float: {b}, complex: {c}")

    print("\n=== Type Checking ===")
    values = [42, 3.14, "hello", True, None, [1, 2], {"key": "val"}]
    for v in values:
        print(f"{str(v):>15} -> {type(v).__name__}")

    print("\n=== Type Conversion ===")
    num_str = "123"
    num_int = int(num_str)
    num_float = float(num_str)
    print(f"str '{num_str}' -> int {num_int} -> float {num_float}")

    print("\n=== Truthy/Falsy ===")
    test_values = [0, 1, "", "text", [], [1], None, True, False]
    for v in test_values:
        print(f"bool({str(v):>8}) = {bool(v)}")


if __name__ == "__main__":
    main()
