# Python Basics - Operators
# -----------------------------------------------------------------------------
# Operators are special symbols that perform operations on values and variables.
#
# Key concepts:
# 1. Arithmetic — +, -, *, /, //, %, **
# 2. Comparison — ==, !=, <, >, <=, >=
# 3. Logical — and, or, not
# 4. Bitwise — &, |, ^, ~, <<, >>
# 5. Assignment — =, +=, -=, *=, etc.
# 6. Membership — in, not in
# 7. Identity — is, is not
# -----------------------------------------------------------------------------


# =============================================================================
# Arithmetic Operators
# =============================================================================


a, b = 17, 5

print(f"a = {a}, b = {b}")
print(f"a + b  = {a + b}")  # Addition: 22
print(f"a - b  = {a - b}")  # Subtraction: 12
print(f"a * b  = {a * b}")  # Multiplication: 85
print(f"a / b  = {a / b}")  # Division: 3.4
print(f"a // b = {a // b}")  # Floor division: 3
print(f"a % b  = {a % b}")  # Modulus: 2
print(f"a ** b = {a**b}")  # Exponentiation: 1419857


# =============================================================================
# Comparison Operators
# =============================================================================


x, y = 10, 20

print(f"\nx = {x}, y = {y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x < y:  {x < y}")
print(f"x > y:  {x > y}")
print(f"x <= y: {x <= y}")
print(f"x >= y: {x >= y}")

# Chained comparisons
print(f"\n1 < 5 < 10: {1 < 5 < 10}")
print(f"1 < 5 > 3:  {1 < 5 > 3}")


# =============================================================================
# Logical Operators
# =============================================================================


t, f = True, False

print(f"\nTrue and False: {t and f}")
print(f"True or False:  {t or f}")
print(f"not True:       {not t}")

# Short-circuit evaluation
# and returns first falsy value, or returns last value
print(f"\n5 and 3:   {5 and 3}")  # 3
print(f"0 and 5:   {0 and 5}")  # 0
print(f"5 or 0:    {5 or 0}")  # 5
print(f"0 or 'hi': {0 or 'hi'}")  # hi


# =============================================================================
# Bitwise Operators
# =============================================================================


a, b = 0b1100, 0b1010  # 12, 10

print(f"\na = {a} ({bin(a)})")
print(f"b = {b} ({bin(b)})")
print(f"a & b  = {a & b}  ({bin(a & b)})")  # AND: 8
print(f"a | b  = {a | b}  ({bin(a | b)})")  # OR: 14
print(f"a ^ b  = {a ^ b}  ({bin(a ^ b)})")  # XOR: 6
print(f"~a     = {~a} ({bin(~a)})")  # NOT: -13
print(f"a << 2 = {a << 2} ({bin(a << 2)})")  # Left shift: 48
print(f"a >> 2 = {a >> 2} ({bin(a >> 2)})")  # Right shift: 3


# =============================================================================
# Assignment Operators
# =============================================================================


x = 10
print(f"\nInitial: x = {x}")

x += 5
print(f"After x += 5:  {x}")

x -= 3
print(f"After x -= 3:  {x}")

x *= 2
print(f"After x *= 2:  {x}")

x //= 3
print(f"After x //= 3: {x}")

x **= 2
print(f"After x **= 2: {x}")

x %= 5
print(f"After x %= 5:  {x}")


# =============================================================================
# Membership Operators
# =============================================================================


fruits = ["apple", "banana", "cherry"]
text = "Hello, World!"

print(f"\n'banana' in fruits:  {'banana' in fruits}")
print(f"'grape' in fruits:   {'grape' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")
print(f"'World' in text:     {'World' in text}")

# Works with sets (O(1) lookup)
unique = {1, 2, 3, 4, 5}
print(f"3 in set: {3 in unique}")


# =============================================================================
# Identity Operators
# =============================================================================


a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"\na == b: {a == b}")  # True — same value
print(f"a is b: {a is b}")  # False — different objects
print(f"a is c: {a is c}")  # True — same object
print(f"a is not b: {a is not b}")

# Identity with None (preferred way to check)
value = None
print(f"\nvalue is None:     {value is None}")
print(f"value is not None: {value is not None}")


# =============================================================================
# Operator Precedence (highest to lowest)
# =============================================================================
# () grouping
# f() function call
# x[] subscription / slicing
# . attribute access
# ** exponentiation
# +x  -x  ~x   (unary operators)
# *  /  //  %  @   (multiplicative)
# +  -          (additive)
# <<  >>        (bitwise shifts)
# &             (bitwise AND)
# ^             (bitwise XOR)
# |             (bitwise OR)
# comparisons:
# == != < > <= >=
# is  is not
# in  not in
# not
# and
# or


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Arithmetic ===")
    print(f"  7 + 3 = {7 + 3}")
    print(f"  7 - 3 = {7 - 3}")
    print(f"  7 * 3 = {7 * 3}")
    print(f"  7 / 3 = {7 / 3:.2f}")
    print(f"  7 // 3 = {7 // 3}")
    print(f"  7 % 3 = {7 % 3}")
    print(f"  7 ** 3 = {7**3}")

    print("\n=== Comparison ===")
    print(f"  5 == 5: {5 == 5}")
    print(f"  5 != 3: {5 != 3}")
    print(f"  5 > 3:  {5 > 3}")
    print(f"  chained: 1 < 3 < 5: {1 < 3 < 5}")

    print("\n=== Logical ===")
    print(f"  True and False: {True and False}")
    print(f"  True or False:  {True or False}")
    print(f"  not True:       {not True}")

    print("\n=== Short-Circuit ===")
    print(f"  '' or 'default': {'' or 'default'}")
    print(f"  'hello' or 'default': {'hello' or 'default'}")

    print("\n=== Membership ===")
    nums = [10, 20, 30, 40]
    print(f"  20 in {nums}: {20 in nums}")
    print(f"  50 in {nums}: {50 in nums}")

    print("\n=== Identity ===")
    a = None
    print(f"  a is None: {a is None}")
    print(f"  [] is []: {[] is []}")  # noqa: F632


if __name__ == "__main__":
    main()
