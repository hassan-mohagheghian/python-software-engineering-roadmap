# Functions - Parameters
# -----------------------------------------------------------------------------
# Parameters define what inputs a function accepts. Python supports several
# parameter types for flexible function signatures.
#
# Key concepts:
# 1. Positional parameters
# 2. Keyword parameters
# 3. Default parameter values
# 4. *args for variable positional arguments
# 5. **kwargs for variable keyword arguments
# -----------------------------------------------------------------------------


# =============================================================================
# Positional Parameters
# =============================================================================


def power(base, exp):
    """Raise base to the power of exp."""
    return base ** exp


print(f"2^10 = {power(2, 10)}")
print(f"10^2 = {power(10, 2)}")  # order matters


# =============================================================================
# Default Parameters
# =============================================================================


def greet(name, greeting="Hello"):
    """Greet someone with a custom greeting."""
    return f"{greeting}, {name}!"


print(greet("Alice"))
print(greet("Bob", "Hey"))


# =============================================================================
# Keyword Arguments
# =============================================================================


def create_profile(name, age, city="Unknown", role="Student"):
    """Create a user profile string."""
    return f"{name}, {age}, from {city}, role: {role}"


# Mixed: positional then keyword
print(create_profile("Alice", 30, city="NYC", role="Engineer"))
print(create_profile(age=25, name="Bob", role="Designer"))


# =============================================================================
# *args — Variable Positional Arguments
# =============================================================================


def sum_all(*args):
    """Sum any number of arguments."""
    print(f"  args type: {type(args).__name__}, value: {args}")
    return sum(args)


print(f"Sum: {sum_all(1, 2, 3)}")
print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")


# =============================================================================
# **kwargs — Variable Keyword Arguments
# =============================================================================


def show_info(**kwargs):
    """Display any keyword arguments passed."""
    print(f"  kwargs type: {type(kwargs).__name__}")
    for key, value in kwargs.items():
        print(f"    {key}: {value}")


show_info(name="Alice", age=30, role="Engineer")


# =============================================================================
# Combining *args and **kwargs
# =============================================================================


def flexible(required, *args, **kwargs):
    """Function with mixed parameter types."""
    print(f"  required: {required}")
    print(f"  args: {args}")
    print(f"  kwargs: {kwargs}")


flexible("hello", 1, 2, 3, key1="a", key2="b")


def main():
    print("=== Parameters ===")
    print(f"Power: {power(3, 4)}")
    print(f"Greeting: {greet('World')}")
    print(f"Profile: {create_profile('Eve', 28)}")
    print(f"Sum all: {sum_all(10, 20, 30)}")


if __name__ == "__main__":
    main()
