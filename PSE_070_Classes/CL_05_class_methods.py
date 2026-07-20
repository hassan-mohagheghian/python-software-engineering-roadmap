# Classes - Class Methods
# -----------------------------------------------------------------------------
# Class methods receive the class (cls) as the first argument instead of
# the instance. They are commonly used as factory methods.
#
# Key concepts:
# 1. @classmethod decorator
# 2. cls parameter (the class itself)
# 3. Factory methods
# 4. Alternative constructors
# -----------------------------------------------------------------------------
# Why class methods matter:
#
# - Create objects from different input formats (factory pattern)
# - Provide alternative constructors
# - Access/modify class-level state
# - Support inheritance properly (cls refers to the actual class)
# -----------------------------------------------------------------------------
# High-level flow:
#
# Call ClassName.method() → cls receives the class → Returns new instance
#      (factory call)           (not instance)          (constructed object)
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - Point.from_tuple((x, y)) — create from tuple
# - User.from_string("name:email") — parse and construct
# - datetime.fromisoformat("2024-01-01") — alternative constructor
# - Config.from_file("config.yaml") — load from external source
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Class Method
# =============================================================================


class MyClass:
    class_var = "I belong to the class"

    @classmethod
    def get_class_var(cls):
        return cls.class_var


print(MyClass.get_class_var())


# =============================================================================
# Factory Methods
# =============================================================================


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    @classmethod
    def from_tuple(cls, coords):
        """Create Point from (x, y) tuple."""
        return cls(coords[0], coords[1])

    @classmethod
    def from_dict(cls, data):
        """Create Point from dictionary."""
        return cls(data["x"], data["y"])

    @classmethod
    def origin(cls):
        """Create Point at origin."""
        return cls(0, 0)


p1 = Point(3, 4)
p2 = Point.from_tuple((5, 6))
p3 = Point.from_dict({"x": 1, "y": 2})
p4 = Point.origin()

print(f"Direct: {p1}")
print(f"From tuple: {p2}")
print(f"From dict: {p3}")
print(f"Origin: {p4}")


# =============================================================================
# Practical: User Factory
# =============================================================================


class User:
    def __init__(self, name, email, role="user"):
        self.name = name
        self.email = email
        self.role = role

    def __repr__(self):
        return f"User({self.name!r}, {self.role!r})"

    @classmethod
    def admin(cls, name, email):
        """Create an admin user."""
        return cls(name, email, role="admin")

    @classmethod
    def from_string(cls, user_str):
        """Create user from 'Name:Email' string."""
        name, email = user_str.split(":")
        return cls(name.strip(), email.strip())


user = User.admin("Alice", "alice@example.com")
print(f"Admin: {user}")

user2 = User.from_string("Bob: bob@example.com")
print(f"From string: {user2}")


def main():
    print("=== Class Methods ===")
    p = Point.from_tuple((10, 20))
    print(f"Point: {p}")
    admin = User.admin("Root", "root@example.com")
    print(f"Admin: {admin}")


if __name__ == "__main__":
    main()
