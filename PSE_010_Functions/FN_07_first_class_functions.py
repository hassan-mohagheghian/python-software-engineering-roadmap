# Functions - First-Class Functions
# -----------------------------------------------------------------------------
# In Python, functions are first-class objects. They can be assigned to
# variables, passed as arguments, returned from other functions, and
# stored in data structures.
#
# Key concepts:
# 1. Assigning functions to variables
# 2. Passing functions as arguments
# 3. Returning functions from functions
# 4. Storing functions in collections
# -----------------------------------------------------------------------------


# =============================================================================
# Functions as Objects
# =============================================================================


def greet(name):
    return f"Hello, {name}!"


# Assign to variable
say_hello = greet
print(say_hello("Alice"))

# Check type
print(f"Type: {type(greet).__name__}")
print(f"Has __call__: {callable(greet)}")


# =============================================================================
# Passing Functions as Arguments
# =============================================================================


def apply(func, value):
    """Apply a function to a value."""
    return func(value)


print(f"apply(str.upper, 'hello') = {apply(str.upper, 'hello')}")
print(f"apply(len, [1, 2, 3]) = {apply(len, [1, 2, 3])}")


# =============================================================================
# Functions in Collections
# =============================================================================


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
}

for op, func in operations.items():
    print(f"  10 {op} 5 = {func(10, 5)}")


# =============================================================================
# Returning Functions
# =============================================================================


def make_greeting(prefix):
    """Return a greeting function with a fixed prefix."""
    def greet(name):
        return f"{prefix}, {name}!"
    return greet


hello = make_greeting("Hello")
hey = make_greeting("Hey")

print(hello("Alice"))
print(hey("Bob"))


def main():
    print("=== First-Class Functions ===")
    result = apply(lambda x: x ** 3, 4)
    print(f"Cube: {result}")
    greet_fn = make_greeting("Welcome")
    print(greet_fn("World"))


if __name__ == "__main__":
    main()
