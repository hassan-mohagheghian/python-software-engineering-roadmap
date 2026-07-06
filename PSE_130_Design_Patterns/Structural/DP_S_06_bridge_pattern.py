# Design Patterns - Bridge Pattern
# -----------------------------------------------------------------------------
# The Bridge Pattern is a structural design pattern that decouples an abstraction
# from its implementation so that both can vary independently.
#
# Instead of creating many subclasses for every combination, we use composition
# to "bridge" two independent hierarchies.
#
# -----------------------------------------------------------------------------
# Key Idea:
#
#   Abstraction  --->  Implementation
#        |                  |
#     (uses)            (provides behavior)
#
# -----------------------------------------------------------------------------
# Benefits:
#
# - Avoids class explosion
# - Follows Open/Closed Principle (OCP)
# - Composition over inheritance
# - Independent evolution of abstractions and implementations
#
# -----------------------------------------------------------------------------
# Example 1: Shapes and Colors
# Example 2: Products, Sizes, and Colors
# -----------------------------------------------------------------------------


from abc import ABC, abstractmethod

# =============================================================================
# IMPLEMENTATION HIERARCHY - Color (shared)
# =============================================================================


class Color(ABC):
    @abstractmethod
    def apply(self) -> str:
        pass


class Red(Color):
    def apply(self):
        return "Red"


class Blue(Color):
    def apply(self):
        return "Blue"


class Black(Color):
    def apply(self):
        return "Black"


# =============================================================================
# EXAMPLE 1 - Shapes (Abstraction 1)
# =============================================================================


class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print(f"Circle with color {self.color.apply()}")


class Square(Shape):
    def draw(self):
        print(f"Square with color {self.color.apply()}")


# =============================================================================
# EXAMPLE 2 - Products + Size (Abstraction 2)
# =============================================================================


class Size(ABC):
    @abstractmethod
    def name(self) -> str:
        pass


class Small(Size):
    def name(self):
        return "Small"


class Medium(Size):
    def name(self):
        return "Medium"


class Large(Size):
    def name(self):
        return "Large"


class Product(ABC):
    def __init__(self, color: Color, size: Size):
        self.color = color
        self.size = size

    @abstractmethod
    def describe(self):
        pass


class TShirt(Product):
    def describe(self):
        print(f"TShirt | Color: {self.color.apply()} | Size: {self.size.name()}")


class Shoes(Product):
    def describe(self):
        print(f"Shoes  | Color: {self.color.apply()} | Size: {self.size.name()}")


# =============================================================================
# USAGE
# =============================================================================


def main():
    print("\n===== Example 1: Shapes =====")

    shapes = [
        Circle(Red()),
        Circle(Blue()),
        Square(Black()),
    ]

    for s in shapes:
        s.draw()

    print("\n===== Example 2: Products =====")

    products = [
        TShirt(Red(), Small()),
        TShirt(Blue(), Large()),
        Shoes(Black(), Medium()),
    ]

    for p in products:
        p.describe()


if __name__ == "__main__":
    main()
