# Design Patterns - Strategy Pattern
# -------------------------------------------------------------------------
# The Strategy Pattern defines a family of algorithms, encapsulate each one,
# and makes them interchangeable.
#
# Instead of using large if/else blocks, the behavior is delegated to a
# strategy object that can be swapped at runtime
#
# Benefits:
# - Follows the Open/Closed Principle (OCP)
# - Reduces conditional complexity
# - Makes behavior interchangeable
#
# Real-world examples:
# - Different payment methods
# - Different storing algorithms
# - Different authentication mechanisms
# - Different notification providers


# ---------------------------Example------------------------------------------
# In this example:
#
# - PaymentStrategy is the strategy interface.
# - CreditCardPayment, PayPalPayment, and CryptoPayment are concrete strategies.
# - Checkout is the context class that uses a payment strategy.
#
# The Checkout class does not need to know how each payment method works.
# It only knows that every strategy provides a pay() method.

# -----------------------------------------------------------------------------
#
# Relationship to OOP Concepts:
#
# - Abstraction:
#     PaymentStrategy defines the common contract.
#
# - Polymorphism:
#     Different payment strategies provide different implementations
#     of the same pay() method.
#
# - Composition:
#     Checkout contains a PaymentStrategy.
#
# - Dependency Injection:
#     The strategy is provided from outside the Checkout class.
#
# Relationship to SOLID:
#
# - OCP:
#     New strategies can be added without changing existing code.
#
# - DIP:
#     Checkout depends on an abstraction rather than concrete classes.
# -----------------------------------------------------------------------------


from abc import ABC, abstractmethod
from decimal import Decimal


class PaymentStrategy(ABC):
    """
    Strategy Interface

    Every payment strategy must implement the pay() method
    """

    @abstractmethod
    def pay(self, amount: Decimal):
        pass


class CreditCardPayment(PaymentStrategy):
    """
    Concrete strategy for credit payments
    """

    def pay(self, amount):
        print(f"Paid ${amount:.2f} using Credit Card")


class PayPalPayment(PaymentStrategy):
    """
    Concrete strategy for Paypal payments
    """

    def pay(self, amount: float):
        print(f"Paid ${amount:.2f} using PayPal")


class CryptoPayment(PaymentStrategy):
    """
    Concrete strategy for cryptocurrency payments.
    """

    def pay(self, amount: float):
        print(f"Paid ${amount:.2f} using Cryptocurrency")


class Checkout:
    """
    Context class.

    The Checkout process does not know the details of
    how a payment is performed.

    It only depends on the PaymentStrategy abstraction.
    """

    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def process_payment(self, amount: float):
        self.payment_strategy.pay(amount)


if __name__ == "__main__":
    checkout = Checkout(payment_strategy=CreditCardPayment())
    checkout.process_payment(amount=100)

    checkout = Checkout(payment_strategy=PayPalPayment())
    checkout.process_payment(amount=100)

    checkout = Checkout(payment_strategy=CryptoPayment())
    checkout.process_payment(amount=100)
