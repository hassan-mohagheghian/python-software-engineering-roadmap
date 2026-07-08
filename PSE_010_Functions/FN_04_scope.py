# Functions - Scope
# -----------------------------------------------------------------------------
# Scope determines where a variable is accessible. Python uses the LEGB rule:
# Local → Enclosing → Global → Built-in.
#
# Key concepts:
# 1. Local scope — inside the function
# 2. Enclosing scope — in a nested function's outer function
# 3. Global scope — module level
# 4. Built-in scope — Python's built-in names
# 5. global and nonlocal keywords
# -----------------------------------------------------------------------------


# =============================================================================
# Local Scope
# =============================================================================


def my_function():
    x = 10  # local to my_function
    print(f"  Inside function: x = {x}")


my_function()
# print(x)  # NameError — x is not defined here


# =============================================================================
# Global Scope
# =============================================================================


counter: int = 0  # global variable


def increment():
    global counter  # declare intent to modify global
    counter += 1


increment()
increment()
print(f"Counter: {counter}")


# =============================================================================
# Enclosing Scope (nonlocal)
# =============================================================================


def outer():
    message = "Hello"

    def inner():
        nonlocal message  # access enclosing scope's variable
        message = "World"

    inner()
    print(f"  After inner(): message = {message}")


outer()


# =============================================================================
# LEGB Rule in Action
# =============================================================================


x = "global"


def legb_demo():
    x = "local"
    print(f"  x inside function: {x}")


legb_demo()
print(f"  x outside function: {x}")


# =============================================================================
# Nested Scopes
# =============================================================================


def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter_func = make_counter()
print(f"Counter: {counter_func()}, {counter_func()}, {counter_func()}")


def main():
    print("=== Scope ===")
    my_function()
    increment()
    print(f"Global counter: {counter}")
    outer()
    legb_demo()
    c = make_counter()
    print(f"Nested counter: {c()}, {c()}")


if __name__ == "__main__":
    main()
