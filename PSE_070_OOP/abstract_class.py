# OOP in Python - Abstract Class
# ----------------------------------------------------------------------------
# An Abstract Class is a class that cannot be instantiated and is meant to be subclassed.
# It can contain abstract methods, which are methods that are declared but not implemented.
# Subclasses of an abstract class must implement all abstract methods, or they will also be considered abstract.
# ----------------------------------------------------------------------------
# In this example, we have an abstract class called `Vehicle` that defines an abstract method `move()`.
# The `Car` and `Bike` classes inherit from `Vehicle` and provide their own implementations of the `move()` method.
# This allows us to create a common interface for all vehicles while still allowing for specific behavior in each subclass.

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("The car is driving.")


class Bike(Vehicle):
    def move(self):
        print("The bike is pedaling.")


if __name__ == "__main__":
    car = Car()
    bike = Bike()

    car.move()  # Output: The car is driving.
    bike.move()  # Output: The bike is pedaling.
