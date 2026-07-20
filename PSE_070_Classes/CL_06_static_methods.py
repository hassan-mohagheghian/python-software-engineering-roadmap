# Classes - Static Methods
# -----------------------------------------------------------------------------
# Static methods don't receive self or cls. They are utility functions
# that belong to the class namespace for organizational purposes.
#
# Key concepts:
# 1. @staticmethod decorator
# 2. No implicit first argument
# 3. Utility/helper functions
# 4. When to use static vs class vs instance
# -----------------------------------------------------------------------------
# Why static methods matter:
#
# - Group related utilities with the class they serve
# - No instance or class state needed
# - Easier to test (no mocking required)
# - Clear intent: pure function in class namespace
# -----------------------------------------------------------------------------
# High-level flow:
#
# ClassName.method(args) → Pure function → Returns result
#     (namespace)            (no state)       (deterministic)
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - MathUtils.add(a, b) — pure arithmetic
# - Temperature.celsius_to_fahrenheit(c) — unit conversion
# - Validator.is_valid_email(email) — input validation
# - StringUtils.slugify("Hello World") — text transformation
# -----------------------------------------------------------------------------
# When to use which:
#
# - Instance method: needs self (instance state)
# - Class method: needs cls (class state or factory)
# - Static method: needs neither (pure utility)
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Static Method
# =============================================================================


class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def is_even(n):
        return n % 2 == 0


print(f"Add: {MathUtils.add(3, 4)}")
print(f"Even: {MathUtils.is_even(4)}")


# =============================================================================
# Practical: Temperature Converter
# =============================================================================


class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5 / 9


print(f"100C = {Temperature.celsius_to_fahrenheit(100)}F")
print(f"212F = {Temperature.fahrenheit_to_celsius(212)}C")


# =============================================================================
# Static vs Class vs Instance
# =============================================================================


class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    # Instance method — uses self
    def area(self):
        return Circle.PI * self.radius ** 2

    # Class method — uses cls
    @classmethod
    def unit(cls):
        return cls(1)

    # Static method — uses neither
    @staticmethod
    def validate_radius(r):
        return r > 0


c = Circle(5)
print(f"Area: {c.area():.2f}")
print(f"Unit circle: {Circle.unit().radius}")
print(f"Valid: {Circle.validate_radius(5)}")


def main():
    print("=== Static Methods ===")
    print(f"Convert 37C: {Temperature.celsius_to_fahrenheit(37):.1f}F")
    print(f"Circle valid: {Circle.validate_radius(-1)}")


if __name__ == "__main__":
    main()
