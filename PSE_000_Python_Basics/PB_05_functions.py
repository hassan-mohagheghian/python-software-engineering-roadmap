# Python Basics - Functions
# -----------------------------------------------------------------------------
# Functions are reusable blocks of code that perform a specific task.
#
# Key concepts:
# 1. Basic definition — def, parameters, return values.
# 2. Default parameters — parameters with fallback values.
# 3. Docstrings — documenting functions.
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Function
# =============================================================================


def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


# =============================================================================
# Default Parameters
# =============================================================================


def power(base: int, exponent: int = 2) -> int:
    return base**exponent


def create_user(name: str, age: int = 0, active: bool = True) -> dict:
    return {"name": name, "age": age, "active": active}


# =============================================================================
# Docstrings
# =============================================================================


def calculate_area(width: float, height: float) -> float:
    """Calculate the area of a rectangle.

    Args:
        width: The width of the rectangle.
        height: The height of the rectangle.

    Returns:
        The product of width and height.
    """
    return width * height


def format_name(first: str, last: str) -> str:
    """Format a person's full name in 'Last, First' order."""
    return f"{last}, {first}"


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Basic Functions ===")
    print(greet("Alice"))
    print(f"2 + 3 = {add(2, 3)}")

    print("\n=== Default Parameters ===")
    print(f"power(3): {power(3)}")
    print(f"power(3, 3): {power(3, 3)}")
    print(f"create_user('Bob'): {create_user('Bob')}")
    print(f"create_user('Alice', age=25): {create_user('Alice', age=25)}")

    print("\n=== Docstrings ===")
    print(f"calculate_area(4, 5): {calculate_area(4, 5)}")
    print(f"format_name('Jane', 'Doe'): {format_name('Jane', 'Doe')}")
    print("calculate_area.__doc__:")
    print(calculate_area.__doc__)


if __name__ == "__main__":
    main()
