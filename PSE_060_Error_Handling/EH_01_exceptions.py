# Python Basics - Error Handling
# -----------------------------------------------------------------------------
# Error handling lets you gracefully manage runtime errors instead of crashing.
#
# Key concepts:
# 1. try / except — catch and handle exceptions.
# 2. Multiple except blocks — handle different exception types.
# 3. else / finally — code that runs on success / always.
# 4. Raising exceptions — raise, custom exceptions.
# 5. Built-in exceptions — common exception types.
# 6. Best practices — specific exceptions, minimal try blocks.
# -----------------------------------------------------------------------------


# =============================================================================
# Basic try / except
# =============================================================================


def safe_divide(a: int, b: int) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None


# =============================================================================
# Multiple Except Blocks
# =============================================================================


def safe_index(the_list: list, index: int):
    try:
        return the_list[index]
    except IndexError:
        print(f"Index {index} out of range (length {len(the_list)})")
        return None
    except TypeError as e:
        print(f"Type error: {e}")
        return None


# =============================================================================
# else and finally
# =============================================================================


def read_file_safe(path: str) -> str | None:
    try:
        f = open(path, "r")
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    else:
        # This block runs ONLY if NO error occurred (file was found)
        content = f.read()
        f.close()
        return content
    finally:
        # This block ALWAYS runs (whether error or not)
        print(f"Attempted to read: {path}")


# =============================================================================
# Raising Exceptions
# =============================================================================


def validate_age(age: int) -> int:
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}")
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    if age > 150:
        raise ValueError(f"Age seems unrealistic: {age}")
    return age


def set_password(password: str) -> str:
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters")
    if not any(c.isupper() for c in password):
        raise ValueError("Password must contain an uppercase letter")
    if not any(c.isdigit() for c in password):
        raise ValueError("Password must contain a digit")
    return "Password set successfully"


# =============================================================================
# Custom Exceptions
# =============================================================================


class AppError(Exception):
    """Base exception for the application."""

    pass


class NotFoundError(AppError):
    """Resource not found."""

    def __init__(self, resource: str, id: str):
        self.resource = resource
        self.id = id
        super().__init__(f"{resource} with id '{id}' not found")


class PermissionError(AppError):
    """Insufficient permissions."""

    def __init__(self, action: str):
        self.action = action
        super().__init__(f"Permission denied for action: {action}")


def find_user(user_id: str) -> dict:
    users = {"u1": {"name": "Alice"}, "u2": {"name": "Bob"}}
    if user_id not in users:
        raise NotFoundError("User", user_id)
    return users[user_id]


# =============================================================================
# Exception Chaining
# =============================================================================


def process_data(data: dict):
    try:
        return data["key"]["nested"]
    # Raise a higher-level exception while preserving the original cause
    except KeyError as e:
        raise ValueError("Invalid data structure") from e


# =============================================================================
# Best Practices
# =============================================================================


# 1. Be specific with exceptions
def good_example():
    try:
        _result = int("abc")
    except ValueError:  # Good — specific exception
        print("Caught specific exception")


# 2. Don't suppress exceptions silently
def bad_example():
    try:
        _result = int("abc")
    except:  # Bad — catches everything including KeyboardInterrupt  # noqa: E722
        pass  # Bad — silently swallows error


# 3. Keep try blocks minimal
def minimal_try():
    data = None
    try:
        data = load_data()
    except IOError:
        print("Failed to load")
        return
    # Process data outside try
    process(data)


def load_data():
    return {"key": "value"}


def process(data):
    print(f"Processing: {data}")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Basic try/except ===")
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")

    print("\n=== Multiple Exceptions ===")
    numbers = [1, 2, 3]
    print(f"Index 1: {safe_index(numbers, 1)}")
    print(f"Index 10: {safe_index(numbers, 10)}")
    print(f"Index '10': {safe_index(numbers, '10')}")  # pyright: ignore[reportArgumentType]

    print("\n=== else/finally ===")
    result = read_file_safe("nonexistent.txt")
    print(f"Result: {result}")

    print("\n=== Raising Exceptions ===")
    try:
        validate_age(25)
        print("Age 25: valid")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        validate_age(-5)
    except ValueError as e:
        print(f"Age -5: {e}")

    print("\n=== Custom Exceptions ===")
    try:
        find_user("u99")
    except NotFoundError as e:
        print(f"Error: {e}")
        print(f"Resource: {e.resource}, ID: {e.id}")

    print("\n=== Password Validation ===")
    tests = ["abc", "abcdefgh", "Abcdefg1", "ABCDEFG1"]
    for pwd in tests:
        try:
            result = set_password(pwd)
            print(f"'{pwd}': {result}")
        except ValueError as e:
            print(f"'{pwd}': {e}")

    print("\n=== Exception Chaining ===")
    try:
        process_data({"other": "value"})
    except ValueError as e:
        print(f"Error: {e}")
        print(f"Caused by: {e.__cause__}")


if __name__ == "__main__":
    main()
