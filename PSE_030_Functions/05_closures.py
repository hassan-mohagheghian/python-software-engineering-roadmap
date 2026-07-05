# Functions - Closures
# -----------------------------------------------------------------------------
# A closure is a function that captures variables from its enclosing scope.
# The inner function "remembers" the outer function's local variables even
# after the outer function has finished executing.
#
# Closures are useful for:
# - Factories that produce configured functions
# - Stateful counters or accumulators
# - Decorators (see FUN_06_decorators.py)
# -----------------------------------------------------------------------------


# =============================================================================
# Simple Closure — Counter
# =============================================================================


def make_counter(start: int = 0):
    count = start

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


# =============================================================================
# Closure as a Factory — Multiplier
# =============================================================================


def make_multiplier(factor: int):
    def multiply(x: int) -> int:
        return x * factor
    return multiply


# =============================================================================
# Closure for Configuration — Greeting
# =============================================================================


def make_greeter(template: str):
    def greeter(name: str) -> str:
        return template.format(name=name)
    return greeter


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Counter ===")
    counter = make_counter()
    print(f"Counter: {counter()}, {counter()}, {counter()}")

    counter_10 = make_counter(10)
    print(f"Counter from 10: {counter_10()}, {counter_10()}")

    print("\n=== Multiplier ===")
    double = make_multiplier(2)
    triple = make_multiplier(3)
    print(f"double(5): {double(5)}")
    print(f"triple(5): {triple(5)}")

    print("\n=== Greeting Factory ===")
    formal = make_greeter("Dear {name},")
    casual = make_greeter("Hey {name}!")
    print(formal("Alice"))
    print(casual("Bob"))


if __name__ == "__main__":
    main()
