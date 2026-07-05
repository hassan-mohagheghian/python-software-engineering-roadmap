# Design Patterns - Visitor Pattern
# -------------------------------------------------------------------------
# The Visitor Pattern lets you add new operations to an existing class
# hierarchy without modifying the classes themselves.
#
# Instead of putting the logic inside each element, you define a separate
# visitor object that "visits" each element and performs the operation.
# The elements accept the visitor and call back into it.
#
# Benefits:
# - Add new operations without changing element classes (OCP)
# - Group related operations into a single visitor class
# - Maintain a clean separation between data structure and algorithm
#
# Real-world examples:
# - Compilers traversing AST nodes to generate code or check types
# - Document processing (exporting elements to HTML, PDF, plain text)
# - File system traversal (calculating size, generating checksums)
# - Serialization / deserialization of complex object graphs
#
# Trade-offs:
# - Adding new element types requires updating every visitor
# - Visitors may need access to internal state of elements
#
# Relationship to OOP Concepts:
#
# - Polymorphism:
#     Each element type implements accept() differently, dispatching
#     to the visitor's type-specific method.
#
# - Double Dispatch:
#     accept() calls visitor.visit_<type>(self), combining two
#     dynamic dispatches — element type + visitor type.
#
# - Separation of Concerns:
#     Elements own structure; visitors own operations on that structure.
#
# Relationship to SOLID:
#
# - OCP:
#     New operations are added by creating new visitors, not by
#     modifying existing element classes.
#
# - SRP:
#     Each visitor encapsulates one well-defined operation.
# -------------------------------------------------------------------------


from abc import ABC, abstractmethod
from typing import Generic, TypeVar

# =============================================================================
# Element Interface
# =============================================================================


class Shape(ABC):
    """Base element — every shape must accept a visitor."""

    @abstractmethod
    def accept(self, visitor: "ShapeVisitor"):
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def accept(self, visitor: "ShapeVisitor"):
        return visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def accept(self, visitor: "ShapeVisitor"):
        return visitor.visit_rectangle(self)


class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def accept(self, visitor: "ShapeVisitor"):
        return visitor.visit_triangle(self)


# =============================================================================
# Visitor Interface
# =============================================================================

T = TypeVar("T")


class ShapeVisitor(ABC, Generic[T]):
    @abstractmethod
    def visit_circle(self, circle: Circle) -> T:
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle: Rectangle) -> T:
        pass

    @abstractmethod
    def visit_triangle(self, triangle: Triangle) -> T:
        pass


# =============================================================================
# Concrete Visitors
# =============================================================================


class AreaCalculator(ShapeVisitor):
    def visit_circle(self, circle: Circle) -> float:
        return 3.14159 * circle.radius**2

    def visit_rectangle(self, rectangle: Rectangle) -> float:
        return rectangle.width * rectangle.height

    def visit_triangle(self, triangle: Triangle) -> float:
        return 0.5 * triangle.base * triangle.height


class DescriptionPrinter(ShapeVisitor):
    def visit_circle(self, circle: Circle) -> str:
        desc = f"Circle with radius {circle.radius}"
        print(f"  {desc}")
        return desc

    def visit_rectangle(self, rectangle: Rectangle) -> str:
        desc = f"Rectangle {rectangle.width}x{rectangle.height}"
        print(f"  {desc}")
        return desc

    def visit_triangle(self, triangle: Triangle) -> str:
        desc = f"Triangle with base {triangle.base} and height {triangle.height}"
        print(f"  {desc}")
        return desc


class SVGExporter(ShapeVisitor):
    def visit_circle(self, circle: Circle) -> str:
        svg = f'<circle r="{circle.radius}" />'
        print(f"  {svg}")
        return svg

    def visit_rectangle(self, rectangle: Rectangle) -> str:
        svg = f'<rect width="{rectangle.width}" height="{rectangle.height}" />'
        print(f"  {svg}")
        return svg

    def visit_triangle(self, triangle: Triangle) -> str:
        svg = f'<polygon points="0,{triangle.height} {triangle.base},{triangle.height} {triangle.base / 2},0" />'
        print(f"  {svg}")
        return svg


# =============================================================================
# Usage
# =============================================================================


def main():
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 8),
    ]

    print("=== Area Calculator ===")
    area_visitor = AreaCalculator()
    for shape in shapes:
        area = shape.accept(area_visitor)
        print(f"  Area: {area:.2f}")

    print("\n=== Description Printer ===")
    desc_visitor = DescriptionPrinter()
    for shape in shapes:
        shape.accept(desc_visitor)

    print("\n=== SVG Exporter ===")
    svg_visitor = SVGExporter()
    for shape in shapes:
        shape.accept(svg_visitor)


if __name__ == "__main__":
    main()
