# Functions - Basic Functions
# -----------------------------------------------------------------------------
# Functions are reusable blocks of code that perform a specific task.
# They help organize code, avoid repetition, and make programs readable.
#
# Key concepts:
# 1. def keyword to define a function
# 2. Parameters vs arguments
# 3. Return values (explicit or implicit None)
# 4. Docstrings for documentation
# 5. Calling a function
# -----------------------------------------------------------------------------


# =============================================================================
# Defining and Calling
# =============================================================================


def greet(name):
    """Return a greeting string."""
    return f"Hello, {name}!"


print(greet("Alice"))


# =============================================================================
# Multiple Parameters
# =============================================================================


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


result = add(3, 5)
print(f"3 + 5 = {result}")


# =============================================================================
# No Return Value (returns None)
# =============================================================================


def print_even(numbers):
    """Print even numbers from a list."""
    for n in numbers:
        if n % 2 == 0:
            print(n, end=" ")
    print()


print_even([1, 2, 3, 4, 5, 6])


# =============================================================================
# Docstrings
# =============================================================================


def calculate_area(width, height):
    """
    Calculate the area of a rectangle.

    Args:
        width: The width of the rectangle.
        height: The height of the rectangle.

    Returns:
        The area as width * height.
    """
    return width * height


print(f"Area: {calculate_area(5, 3)}")


# =============================================================================
# Functions Are Objects
# =============================================================================


def square(x):
    return x * x


# Assign function to variable
my_func = square
print(f"my_func(4) = {my_func(4)}")

# Store in a list
operations = [square, abs, len]
print(f"First element: {operations[0](5)}")


def main():
    print("=== Basic Functions ===")
    print(greet("World"))
    print(f"Add: {add(10, 20)}")
    print(f"Area: {calculate_area(4, 6)}")


if __name__ == "__main__":
    main()
