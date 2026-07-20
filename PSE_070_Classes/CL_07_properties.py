# Classes - Properties
# -----------------------------------------------------------------------------
# Properties provide a Pythonic way to control access to attributes.
# They let you define getters, setters, and deleters with method-like syntax.
#
# Key concepts:
# 1. @property for getters
# 2. @<name>.setter for setters
# 3. Computed properties
# 4. Property vs direct attribute access
# -----------------------------------------------------------------------------
# Why properties matter:
#
# - Validate data before setting (invariants)
# - Compute values on-the-fly (no storage needed)
# - Maintain backward compatibility (add validation without breaking API)
# - Read-only attributes (getter without setter)
# -----------------------------------------------------------------------------
# High-level flow:
#
# obj.attr → @property getter → Validation/Computation → Return value
# obj.attr = val → @setter → Validate → Store in _attr
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - circle.radius — validate non-negative
# - user.full_name — compute from first/last
# - temperature.celsius — auto-convert to/from Fahrenheit
# - account.balance — read-only (no setter)
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Property
# =============================================================================


class Circle:
    def __init__(self, radius):
        self._radius = radius  # internal storage

    @property
    def radius(self):
        """Get radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius with validation."""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        """Computed property — no setter."""
        import math

        return math.pi * self._radius**2


c = Circle(5)
print(f"Radius: {c.radius}")
print(f"Area: {c.area:.2f}")

c.radius = 10
print(f"New area: {c.area:.2f}")


# =============================================================================
# Read-Only Property
# =============================================================================


class Person:
    def __init__(self, first, last):
        self._first = first
        self._last = last

    @property
    def full_name(self):
        """Computed — read only."""
        return f"{self._first} {self._last}"


p = Person("Alice", "Smith")
print(f"Name: {p.full_name}")


# =============================================================================
# Practical: Validated Attributes
# =============================================================================


class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9


t = Temperature(100)
print(f"Boiling: {t.celsius}C / {t.fahrenheit}F")

t.fahrenheit = 32
print(f"Freezing: {t.celsius}C / {t.fahrenheit}F")


def main():
    print("=== Properties ===")
    c = Circle(3)
    print(f"Radius: {c.radius}, Area: {c.area:.2f}")
    c.radius = 7
    print(f"New: {c.radius}, Area: {c.area:.2f}")


if __name__ == "__main__":
    main()
