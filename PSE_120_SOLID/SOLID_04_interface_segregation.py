# SOLID Principles - Interface Segregation Principle
# -----------------------------------------------------------------------------
# Clients should not be forced to depend on interfaces they do not use.
# It's better to have multiple specific interfaces rather than one
# general-purpose interface.
#
# Benefits:
# - Reduces the impact of changes
# - Promotes modular, maintainable code
# - Classes implement only what they actually need
#
# Real-world examples:
# - Payment processors (charge-only vs charge+refund)
# - Worker roles (work-only vs work+eat)
# - Storage backends (read-only vs read+write)
# -----------------------------------------------------------------------------


# =============================================================================
# VIOLATION: Single fat interface forces unnecessary implementations
# =============================================================================

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
    eat(), even though the behavior is meaningless
    """

    def work(self):
        print("Robot is working")

    def eat(self):
        raise NotImplementedError("Robots do not eat")


# =============================================================================
# FOLLOW: Split into focused interfaces
# =============================================================================


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


class RobotWorker(Workable):
    """A robot worker can only work. No eat() required."""

    def work(self):
        print("Robot is working.")


# =============================================================================
# Usage
# =============================================================================

if __name__ == "__main__":
    # Violation
    print("=== Violation ===")
    human = Human()
    human.work()
    human.eat()
    robot = Robot()
    robot.work()
    # robot.eat()  # Raises NotImplementedError

    # Follow
    print("\n=== Follow ===")
    human = HumanWorker()
    human.work()
    human.eat()
    robot = RobotWorker()
    robot.work()
