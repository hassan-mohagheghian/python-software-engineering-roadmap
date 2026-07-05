# Advanced Patterns - Dependency Injection
# -------------------------------------------------------------------------
# Dependency Injection (DI) is a technique where an object receives its
# dependencies from the outside rather than creating them internally.
# This inverts the usual control flow — the caller decides which
# implementation to provide.
#
# Benefits:
# - Loose coupling between components
# - Easy to swap implementations (e.g., real vs mock for testing)
# - Follows the Dependency Inversion Principle (DIP)
#
# Real-world examples:
# - Web frameworks injecting database connections into handlers
# - Test suites injecting mock services into units under test
# - Plugin systems where the host injects implementations
#
# Relationship to OOP Concepts:
#
# - Abstraction:
#     Dependencies are coded against interfaces, not concrete classes.
#
# - Polymorphism:
#     The injected dependency can be any implementation of the interface.
#
# - Composition:
#     Objects are assembled from parts provided externally.
#
# Relationship to SOLID:
#
# - DIP:
#     High-level modules depend on abstractions, not concretions.
#     The injector (framework, test, or main()) chooses the concrete type.
# -------------------------------------------------------------------------


from abc import ABC, abstractmethod


# =============================================================================
# Dependency Interfaces
# =============================================================================


class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass


class Notifier(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str):
        pass


# =============================================================================
# Concrete Implementations
# =============================================================================


class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f"  [LOG] {message}")


class FileLogger(Logger):
    def __init__(self, path: str = "app.log"):
        self.path = path

    def log(self, message: str):
        print(f"  [FILE:{self.path}] {message}")


class EmailNotifier(Notifier):
    def send(self, recipient: str, message: str):
        print(f"  [EMAIL] To {recipient}: {message}")


class SMSNotifier(Notifier):
    def send(self, recipient: str, message: str):
        print(f"  [SMS] To {recipient}: {message}")


# =============================================================================
# Consumer — depends on abstractions, not concretions
# =============================================================================


class OrderService:
    def __init__(self, logger: Logger, notifier: Notifier):
        self.logger = logger
        self.notifier = notifier

    def place_order(self, user: str, item: str):
        self.logger.log(f"Order placed: {item} by {user}")
        self.notifier.send(user, f"Your order for '{item}' is confirmed!")


# =============================================================================
# Usage — different implementations injected at runtime
# =============================================================================


def main():
    print("=== Console Logger + Email Notifier ===")
    service = OrderService(ConsoleLogger(), EmailNotifier())
    service.place_order("alice@example.com", "Python book")

    print("\n=== File Logger + SMS Notifier ===")
    service2 = OrderService(FileLogger("orders.log"), SMSNotifier())
    service2.place_order("+1234567890", "Keyboard")


if __name__ == "__main__":
    main()
