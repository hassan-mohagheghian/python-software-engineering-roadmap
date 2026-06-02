# SOLID Principles in Python
# ISP - Interface Segregation Principle
# an ISP Follow Examples
# -------------------------------------------------------
# The Interface Segregation Principle states that clients
# should not be forced to depend on interfaces they do not use.
# In other words, it's better to have multiple specific
# interfaces rather than a single general-purpose interface.
# This principle helps to reduce the impact of changes and
# promotes a more modular and maintainable codebase.
# ------------------------------------------------------
# In this example, we have two separate interfaces: Workable and Eatable.
# The HumanWorker class implements both interfaces, while the Robot class
# only implements the Workable interface. This design adheres to the
# Interface Segregation Principle, allowing each class to only implement
# the methods that are relevant to its functionality.

from abc import ABC, abstractmethod


class Workable(ABC):
    """Capability: can perform work"""

    @abstractmethod
    def work(self):
        raise NotImplementedError()


class Eatable(ABC):
    """Capability: can consume food."""

    @abstractmethod
    def eat(self):
        raise NotImplementedError()


class HumanWorker(Workable, Eatable):
    """A human worker can work and eat."""

    def work(self):
        print("Human is working.")

    def eat(self):
        print("Human is eating.")


class Robot(Workable):
    """
    A robot worker can only work.

    Note: By splitting the interfaces,
    we avoid forcing the Robot class to implement the eat() method,
    which it doesn't need.This adheres to the Interface Segregation
    Principle, ensuring that classes only implement the methods
    they actually use.
    """

    def work(self):
        print("Robot is working.")


# Example usage
if __name__ == "__main__":
    human = HumanWorker()
    robot = Robot()

    human.work()  # Output: Human is working.
    human.eat()  # Output: Human is eating.

    robot.work()  # Output: Robot is working.
    # robot.eat()  # This would raise an AttributeError since Robot doesn't implement eat()
