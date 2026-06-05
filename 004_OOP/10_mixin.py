# OOP in Python - Mixin
# ----------------------------------------------------------------------------
# A Mixin is a class that provides methods to other classes but is not intended to be
# instantiated on its own. Mixins are used to add functionality to classes in a flexible way,
# allowing for code reuse without the need for inheritance from a common base class.
# ----------------------------------------------------------------------------
# In this example, we have a Mixin class called `Flyable` that provides a method for flying.
# The `Bird` class inherits from both `Flyable` and a base class called `Animal`.
# This allows the `Bird` class to have both the properties of an `Animal`
# and the ability to fly without needing to create a complex inheritance hierarchy.


class Flyable:
    def fly(self):
        print("I can fly!")


class Animal:
    def eat(self):
        print("I can eat!")


class Bird(Flyable, Animal):
    pass


if __name__ == "__main__":
    bird = Bird()
    bird.eat()  # Output: I can eat!
    bird.fly()  # Output: I can fly!
