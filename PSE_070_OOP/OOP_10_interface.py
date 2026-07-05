# OOP in Python - Interface
# ----------------------------------------------------------------------------
# An Interface is a programming structure that allows you to define a contract for classes to follow.
# It specifies a set of methods that a class must implement, but does not provide any implementation
# for those methods. In Python, we can use abstract base classes (ABCs) to create interfaces.
# ----------------------------------------------------------------------------
# In this example, we have an interface called `Shape` that defines a method `area()`.
# The `Circle` and `Rectangle` classes implement this interface by providing their
# own implementations of the `area()` method. This allows us to use polymorphism, where we can treat
# different shapes in a uniform way, as long as they implement the `Shape` interface.


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
