# Functions - Closures
# -----------------------------------------------------------------------------
# A closure is a function that remembers the values from its enclosing scope
# even after that scope has finished executing. This enables powerful
# patterns like factory functions and decorators.
#
# Key concepts:
# 1. nested functions
# 2. nonlocal keywordj
# 3. Factory functions
# 4. State preservation without classes
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Closure
# =============================================================================


def make_adder(n):
    """Return a function that adds n to its argument."""

    def adder(x):
        return x + n  # 'n' is captured from enclosing scope

    return adder


add5 = make_adder(5)
add10 = make_adder(10)

print(f"add5(3) = {add5(3)}")
print(f"add10(3) = {add10(3)}")


# =============================================================================
# Closures for State
# =============================================================================


def make_counter(start=0):
    """Create a counter that preserves state."""
    count = start

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter = make_counter()
print(f"Counter: {counter()}, {counter()}, {counter()}")


# =============================================================================
# Closures for Configuration
# =============================================================================


def make_multiplier(factor):
    """Create a multiplier with a fixed factor."""

    def multiply(x):
        return x * factor

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

print(f"Double 5: {double(5)}")
print(f"Triple 5: {triple(5)}")


# =============================================================================
# Practical: Rate Limiter
# =============================================================================


def make_logger(prefix):
    """Create a logging function with a fixed prefix."""

    def log(message):
        print(f"[{prefix}] {message}")

    return log


info_log = make_logger("INFO")
error_log = make_logger("ERROR")

info_log("Server started")
error_log("Connection failed")


def main():
    print("=== Closures ===")
    add7 = make_adder(7)
    print(f"add7(3) = {add7(3)}")
    c = make_counter(10)
    print(f"Counter: {c()}, {c()}, {c()}")
    triple = make_multiplier(3)
    print(f"Triple 4: {triple(4)}")


if __name__ == "__main__":
    main()
