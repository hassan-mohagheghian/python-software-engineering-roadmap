# Design Patterns - Adapter Pattern
# -----------------------------------------------------------------------------
# The Adapter Pattern is a structural design pattern that allows objects with
# incompatible interfaces to work together.
#
# It acts as a bridge between two incompatible interfaces by wrapping one
# class and exposing a compatible interface expected by the client.
#
# In this example:
#
# - The client expects a "PaymentProcessor" interface with a process_payment() method.
# - The existing legacy system provides a "LegacyPaymentService" with a make_payment() method.
# - The Adapter converts the interface of LegacyPaymentService into a form
#   that the client can use without changing the legacy code.
#
# Benefits:
#
# - Follows the Open/Closed Principle (OCP)
#   You can introduce new adapters without modifying existing code.
#
# - Enables integration of legacy systems
#   Old code can be reused without rewriting it.
#
# - Promotes composition over inheritance
#   Adapter wraps existing objects instead of inheriting from them.
#
# - Improves flexibility
#   Multiple incompatible systems can work together through adapters.
#
# Real-world examples:
#
# - Integrating third-party APIs with different interfaces
# - Wrapping legacy payment gateways
# - Database driver adapters (e.g., different SQL engines)
# - Logging systems with different formats
# -----------------------------------------------------------------------------

from abc import ABC, abstractmethod

# -----------------------------------------------------------------------------
# Target Interface (What the client expects)
# -----------------------------------------------------------------------------


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass


# -----------------------------------------------------------------------------
# Adaptee (Existing incompatible class)
# -----------------------------------------------------------------------------


class LegacyPaymentService:
    def make_payment(self, amount: float):
        print(f"[Legacy] Processing payment of ${amount}")


# -----------------------------------------------------------------------------
# Adapter
# -----------------------------------------------------------------------------
# Converts LegacyPaymentService into a PaymentProcessor-compatible interface.
# -----------------------------------------------------------------------------


class PaymentAdapter(PaymentProcessor):
    def __init__(self, legacy_service: LegacyPaymentService):
        self.legacy_service = legacy_service

    def process_payment(self, amount: float):
        # translate request to legacy format
        self.legacy_service.make_payment(amount)


# -----------------------------------------------------------------------------
# Client
# -----------------------------------------------------------------------------
# The client depends only on the PaymentProcessor abstraction.
# -----------------------------------------------------------------------------


class CheckoutService:
    def __init__(self, processor: PaymentProcessor):
        self.processor = processor

    def checkout(self, amount: float):
        self.processor.process_payment(amount)


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    legacy_service = LegacyPaymentService()

    adapter = PaymentAdapter(legacy_service)

    checkout = CheckoutService(adapter)

    checkout.checkout(99.99)


if __name__ == "__main__":
    main()
