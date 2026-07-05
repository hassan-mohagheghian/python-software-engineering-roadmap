# Design Patterns - Decorator Pattern
# -----------------------------------------------------------------------------
# The Decorator Pattern is a structural design pattern that allows behavior
# to be added to objects dynamically without modifying their code.
#
# Instead of using inheritance to extend behavior, we use composition to wrap
# an object with additional functionality.
#
# -----------------------------------------------------------------------------
# Key Idea:
#
# Base Object → Wrapped by Decorator(s) → Enhanced Object
#
# Each decorator implements the same interface as the base object.
#
# -----------------------------------------------------------------------------
# Benefits:
#
# - Follows Open/Closed Principle (OCP)
#   You can add new behavior without modifying existing classes.
#
# - Promotes composition over inheritance
#
# - Allows flexible and reusable feature stacking
#
# - Common in middleware systems and frameworks
#
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - Logging middleware in web frameworks
# - Authentication layers
# - Caching layers
# - Input validation layers
# - Python function decorators (@staticmethod, @lru_cache)
# -----------------------------------------------------------------------------

from abc import ABC, abstractmethod

# -----------------------------------------------------------------------------
# Component Interface
# -----------------------------------------------------------------------------


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


# -----------------------------------------------------------------------------
# Concrete Component
# -----------------------------------------------------------------------------


class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending Email: {message}")


# -----------------------------------------------------------------------------
# Base Decorator
# -----------------------------------------------------------------------------


class NotifierDecorator(Notifier):
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def send(self, message: str):
        self.notifier.send(message)


# -----------------------------------------------------------------------------
# Concrete Decorators
# -----------------------------------------------------------------------------


class SMSDecorator(NotifierDecorator):
    def send(self, message: str):
        super().send(message)
        print(f"Sending SMS: {message}")


class SlackDecorator(NotifierDecorator):
    def send(self, message: str):
        super().send(message)
        print(f"Sending Slack message: {message}")


class LoggingDecorator(NotifierDecorator):
    def send(self, message: str):
        print(f"[LOG] About to send message: {message}")
        super().send(message)


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    notifier = EmailNotifier()

    # Wrap with logging
    notifier = LoggingDecorator(notifier)

    # Add SMS
    notifier = SMSDecorator(notifier)

    # Add Slack
    notifier = SlackDecorator(notifier)

    notifier.send("System is down!")


if __name__ == "__main__":
    main()
