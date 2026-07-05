# SOLID Principles in Python
# ISP - Interface Segregation Principle
# an ISP Violation Examples
# -------------------------------------------------------
# The Interface Segregation Principle states that clients
# should not be forced to depend on interfaces they do not use.
# In other words, it's better to have multiple specific
# interfaces rather than a single general-purpose interface.
# This principle helps to reduce the impact of changes and
# promotes a more modular and maintainable codebase.
# ------------------------------------------------------
# In this example, we have a single Worker interface that includes both
# work() and eat() methods. The Human class implements both methods, while
# the Robot class is forced to implement eat() even though it doesn't need it.
# This design violates the Interface Segregation Principle, as it forces
# the Robot class to depend on an interface that includes methods it does not use.
# This can lead to issues such as unimplemented methods or the need for workarounds,
# making the code less maintainable and more error-prone.


from abc import ABC, abstractmethod


class Worker(ABC):
    @abstractmethod
    def work(self):
        """Perform work"""
        pass

    @abstractmethod
    def eat(self):
        """Consume food."""
        pass


class Human(Worker):
    """Humans can both work and eat."""

    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")


class Robot(Worker):
    """
    Robots can work but can't eat.

    The worker interface forces Robot to implement
    east(), event though the behavior is meaningless
    """

    def work(self):
        print("Robot is workings")

    def eat(self):
        raise NotImplementedError("Robots do not eat")


if __name__ == "__main__":
    human = Human()
    human.work()  # Output: Human is working
    human.eat()  # Output: Human is eating

    robot = Robot()
    robot.work()  # Output: Robot is workings
    #  an ISP violation, as Robot is forced to implement a method it doesn't need.
    robot.eat()  # Raises NotImplementedError: Robots do not eat
