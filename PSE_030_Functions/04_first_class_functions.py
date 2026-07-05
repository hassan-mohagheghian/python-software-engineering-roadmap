# Functions - First-Class Functions
# -----------------------------------------------------------------------------
# In Python, functions are first-class objects. That means you can:
#
# - Assign a function to a variable
# - Pass a function as an argument to another function
# - Return a function from another function
#
# This enables patterns like callbacks, strategy selection, and higher-order
# functions such as map, filter, and sorted.
# -----------------------------------------------------------------------------


# =============================================================================
# Passing a Function as an Argument
# =============================================================================


def apply(func, value):
    return func(value)


def double(x: int) -> int:
    return x * 2


def negate(x: int) -> int:
    return -x


# =============================================================================
# Returning a Function
# =============================================================================


def get_operation(op: str):
    operations = {
        "add": lambda a, b: a + b,
        "sub": lambda a, b: a - b,
        "mul": lambda a, b: a * b,
        "div": lambda a, b: a / b if b != 0 else "undefined",
    }
    return operations.get(op)


# =============================================================================
# Functions Stored in Collections
# =============================================================================


def describe_person(name: str, age: int) -> str:
    return f"{name} is {age}"


def list_commands():
    commands = {
        "greet": lambda name: f"Hello, {name}!",
        "farewell": lambda name: f"Goodbye, {name}!",
    }
    return commands


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Passing Functions ===")
    print(f"apply(double, 6): {apply(double, 6)}")
    print(f"apply(negate, 6): {apply(negate, 6)}")

    print("\n=== Returning Functions ===")
    op = get_operation("mul")
    print(f"get_operation('mul')(3, 4): {op(3, 4)}")

    print("\n=== Functions in Collections ===")
    cmds = list_commands()
    print(f"cmds['greet']('Alice'): {cmds['greet']('Alice')}")
    print(f"cmds['farewell']('Bob'): {cmds['farewell']('Bob')}")


if __name__ == "__main__":
    main()
