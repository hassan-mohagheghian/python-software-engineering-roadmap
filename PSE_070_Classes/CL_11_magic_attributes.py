# Classes - Magic Attributes
# -----------------------------------------------------------------------------
# Every Python object carries built-in special (dunder) attributes that
# expose metadata about the object, its class, and its structure.
#
# Key concepts:
# 1. Object identity — __class__, __id__
# 2. Class metadata — __name__, __module__, __qualname__, __doc__
# 3. Class structure — __bases__, __mro__, __subclasses__
# 4. Attribute access — __dict__, __slots__, __weakref__
# 5. Customization hooks — __sizeof__, __class_getitem__
# -----------------------------------------------------------------------------
# Why magic attributes matter:
#
# - Inspect objects at runtime (debugging, serialization, ORMs)
# - Build frameworks that discover class structure (dataclasses, Pydantic)
# - Enforce memory/speed constraints with __slots__
# - Support generic types with __class_getitem__
# -----------------------------------------------------------------------------
# High-level flow:
#
# Built-in function → Python reads magic attribute → Returns metadata
#    (type(obj))          (__class__)                 (<class 'MyClass'>)
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - ORM uses __name__ to map classes to database tables
# - Serializer uses __dict__ to extract all instance attributes
# - __slots__ in high-performance systems to reduce memory
# - __mro__ for debugging complex multiple inheritance
# -----------------------------------------------------------------------------

import sys

# =============================================================================
# Object Identity & Class Metadata
# =============================================================================


class User:
    """A user in the system."""

    pass


class Admin(User):
    """An admin user with elevated privileges."""

    pass


u = Admin()

print(f"__class__:  {u.__class__}")
print(f"__name__:   {u.__class__.__name__}")
print(f"__module__: {u.__class__.__module__}")
print(f"__qualname__: {u.__class__.__qualname__}")
print(f"__doc__:    {u.__class__.__doc__}")


# =============================================================================
# Class Structure: Inheritance
# =============================================================================


print(f"\n__bases__:      {Admin.__bases__}")
print(f"__mro__:        {Admin.__mro__}")
print(f"__subclasses__: {User.__subclasses__()}")


# =============================================================================
# __dict__ — Attribute Dictionary
# =============================================================================


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def read(self): ...


p = Product("Widget", 9.99)

# Instance __dict__ — stores instance attributes
print(f"\nInstance __dict__: {p.__dict__}")

# Class __dict__ — stores class-level attributes and methods
print(f"Class __dict__:    {list(Product.__dict__.keys())}")


# =============================================================================
# __slots__ — Fixed Attribute Set
# =============================================================================


class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(3, 4)
print(f"\nPoint: ({p.x}, {p.y})")

# No __dict__ when __slots__ is defined
print(f"Has __dict__: {hasattr(p, '__dict__')}")
print(f"But User class Has __dict__: {hasattr(Point, '__dict__')}")

# Cannot add arbitrary attributes
try:
    p.z = 5
except AttributeError as e:
    print(f"Cannot add attr: {e}")


# =============================================================================
# __weakref__ — Weak Reference Support
# =============================================================================


class Node:
    def __init__(self, value):
        self.value = value


n = Node(42)
print(f"\n__weakref__: {n.__weakref__}")


# =============================================================================
# __sizeof__ — Memory Footprint
# =============================================================================


class Lightweight:
    __slots__ = ("x",)

    def __init__(self, x):
        self.x = x


class Heavy:
    def __init__(self, x):
        self.x = x


lw = Lightweight(1)
hv = Heavy(1)


def print_size(obj, name):
    # Note:
    # __slots__ stores attributes directly inside the object, so the object itself
    # is slightly larger. A regular class keeps most attribute data in a separate
    # __dict__, making the object appear smaller while using more memory overall.
    print(f"\n{name}")
    print("-" * 40)
    print(f"obj.__sizeof__:   {obj.__sizeof__()} bytes")
    print(f"Object size     : {sys.getsizeof(obj):>4} bytes")

    if hasattr(obj, "__dict__"):
        print(f"__dict__ size   : {sys.getsizeof(obj.__dict__):>4} bytes")
        print(
            f"Total (approx.) : {sys.getsizeof(obj) + sys.getsizeof(obj.__dict__):>4} bytes"
        )
    else:
        print("__dict__        : <not available>")
        print(f"Total (approx.) : {sys.getsizeof(obj):>4} bytes")


print_size(lw, "Lightweight (__slots__)")
print_size(hv, "Heavy (normal class)")


# =============================================================================
# __class_getitem__ — Generic Type Support
# =============================================================================


class Response:
    def __init__(self, data):
        self.data = data

    def __class_getitem__(cls, item):
        return cls


# Supports Response[int], Response[str], etc.
print(f"\nResponse[int]:  {Response[int]}")
print(f"Response[str]:  {Response[str]}")


# =============================================================================
# Common Magic Attributes Cheat Sheet
# =============================================================================


def main():
    print("=== Magic Attributes ===")

    obj = Product("Demo", 1.0)

    # Identity
    print(f"type:     {type(obj)}")
    print(f"id:       {id(obj)}")

    # Class metadata
    print(f"class:    {obj.__class__.__name__}")
    print(f"module:   {obj.__class__.__module__}")
    print(f"doc:      {obj.__class__.__doc__}")

    # Structure
    print(f"bases:    {Product.__bases__}")
    print(f"mro:      {[c.__name__ for c in Product.__mro__]}")

    # Attributes
    print(f"dict:     {obj.__dict__}")
    print(f"sizeof:   {obj.__sizeof__()} bytes")


if __name__ == "__main__":
    main()
