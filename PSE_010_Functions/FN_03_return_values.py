# Functions - Return Values
# -----------------------------------------------------------------------------
# Functions can return values using the return statement. Python functions
# can return single values, multiple values (as tuples), or nothing (None).
#
# Key concepts:
# 1. Single return value
# 2. Multiple return values (tuple unpacking)
# 3. Early return
# 4. Returning None explicitly
# 5. Returning functions
# -----------------------------------------------------------------------------


# =============================================================================
# Single Return
# =============================================================================


def square(x):
    """Return the square of x."""
    return x * x


print(f"square(5) = {square(5)}")


# =============================================================================
# Multiple Returns (Tuple)
# =============================================================================


def min_max(numbers):
    """Return both the minimum and maximum of a list."""
    return min(numbers), max(numbers)


lo, hi = min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Min: {lo}, Max: {hi}")


# =============================================================================
# Early Return
# =============================================================================


def divide(a, b):
    """Divide a by b, returning None if b is zero."""
    if b == 0:
        return None
    return a / b


print(f"10 / 3 = {divide(10, 3)}")
print(f"10 / 0 = {divide(10, 0)}")


# =============================================================================
# Returning None Explicitly
# =============================================================================


def log_message(msg):
    """Print a message and return None."""
    print(f"[LOG] {msg}")
    return


result = log_message("System started")
print(f"Return value: {result}")


# =============================================================================
# Returning Functions
# =============================================================================


def make_multiplier(factor):
    """Return a function that multiplies by factor."""

    def multiply(x):
        return x * factor

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)
print(f"double(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")


# =============================================================================
# Unpacking Returns
# =============================================================================


def get_user():
    """Return user data as a tuple."""
    return "Alice", 30, "alice@example.com"


name, age, email = get_user()
print(f"User: {name}, {age}, {email}")


def main():
    print("=== Return Values ===")
    print(f"Square: {square(7)}")
    lo, hi = min_max([10, 20, 5, 15])
    print(f"Range: {lo} to {hi}")
    print(f"Divide: {divide(20, 4)}")
    print(f"Double 8: {double(8)}")


if __name__ == "__main__":
    main()
