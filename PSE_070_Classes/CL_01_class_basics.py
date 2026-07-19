# Classes - Class Basics
# -----------------------------------------------------------------------------
# A class is a blueprint for creating objects. It bundles data (attributes)
# and behavior (methods) into a single unit.
#
# Key concepts:
# 1. Class definition and instantiation
# 2. __init__ constructor
# 3. Instance attributes (self.name)
# 4. Instance methods
# 5. Object identity (id)
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - User class in a web app (name, email, login())
# - Product in an e-commerce system (price, name, discount())
# - File handler in a CLI tool (path, read(), write())
# - Database connection (host, port, query())
# -----------------------------------------------------------------------------
# High-level flow:
#
# Class Definition → Instantiation → Use Attributes & Methods → Object
#     (blueprint)       (create)        (interact)           (in memory)
# -----------------------------------------------------------------------------
# Why classes matter:
#
# - Organize code into logical units
# - Enable code reuse via inheritance
# - Model real-world entities naturally
# - Support encapsulation and abstraction
# -----------------------------------------------------------------------------

# =============================================================================
# Basic Class Definition
# =============================================================================


class Person:
    """A simple person class demonstrating class basics."""

    def __init__(self, name: str, age: int):
        # Instance attributes — unique to each object
        self.name = name
        self.age = age

    def greet(self):
        """Instance method — operates on instance data."""
        print(f"Hello, I'm {self.name}")


# =============================================================================
# Instantiation and Usage
# =============================================================================


def main():
    print("=== Class Basics ===")

    # Create instances (objects) from the class blueprint
    p1 = Person("Alice", 30)
    p2 = Person("Bob", 25)

    # Access attributes
    print(f"Name: {p1.name}")
    print(f"Age: {p2.age}")

    # Call methods
    p1.greet()
    p2.greet()

    # Objects are independent
    p1.name = "Alice Updated"
    print(f"p1 name: {p1.name}")
    print(f"p2 name: {p2.name}")  # unchanged

    # Each object has a unique identity
    print(f"p1 id: {id(p1)}")
    print(f"p2 id: {id(p2)}")
    print(f"Same object? {p1 is p2}")


if __name__ == "__main__":
    main()
