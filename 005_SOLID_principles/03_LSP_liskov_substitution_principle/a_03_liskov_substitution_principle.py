# Liskov Substitution Principle - LSP
# If B is a subtype of A, then B should be usable anywhere A is expected without breaking the program
#
# LSP is about designing inheritance hierarchies so that parents only
# include behavior that all children can genuinely support, and more
# specific behavior is pushed down to specialized subtypes.


# --------------- Wrong Usage ----------------
# The function make_bird_fly expects that every Bird can fly
# But Penguin cannot satisfy that contract and violate LSP


class Bird:
    def fly(self):
        print("Flying")


class Sparrow(Bird):
    pass


class Penguin(Bird):
    def fly(self):
        raise RuntimeError("Penguins cannot fly")


def make_bird_fly(bird: Bird):
    bird.fly()


make_bird_fly(Sparrow())  # OK
make_bird_fly(Penguin())  # BOOM


# -------------- Right Usage ----------------------
from abc import ABC, abstractmethod


class Bird:
    pass


class FlyingBird(Bird, ABC):
    @abstractmethod
    def fly(self):
        pass


class Sparrow(FlyingBird):
    def fly(self):
        print("Flying")


class Penguin(Bird):
    def swim(self):
        print("Swimming")


# with this design below function can expresses its requirement clearly
# and follow LSP
def make_bird_flying(bird: FlyingBird):
    bird.fly()


make_bird_flying(Sparrow)  # OK


# ---------- a More Practical Example: Payment Processor --------------


# --------------- Wrong Usage --------------------
from abc import ABC, abstractmethod
from decimal import Decimal


class PaymentProcessor(ABC):
    @abstractmethod
    def charge(self, amount: Decimal):
        raise NotImplementedError()

    @abstractmethod
    def refund(self, amount: Decimal):
        raise NotImplementedError()


class CreditCardProcessor(PaymentProcessor):
    def charge(self, amount: Decimal):
        print(f"Charged ${amount}")

    def refund(self, amount):
        print(f"Refunded ${amount}")


class CashDeliveryProcessor(PaymentProcessor):
    def charge(self, amount: Decimal):
        print("Payment will be collected on delivery")

    def refund(self, amount):
        """This function violate LSP
        Because in case of use CashDeliveryProcessor in place that expected PaymentProcessor an error will be raised.
        """
        raise NotImplementedError(
            "Cash on delivery payments cannot be refunded electronically."
        )


def issue_refund(processor: PaymentProcessor, amount: Decimal):
    processor.refund(amount=amount)


issue_refund(CreditCardProcessor(), Decimal(100))  # Works correctly
issue_refund(CashDeliveryProcessor(), Decimal("100"))  # But this raise an error


# -------------- Right Usage ----------------

from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def charge(self, amount: Decimal):
        pass


class RefundedPaymentProcessor(PaymentProcessor):
    @abstractmethod
    def refund(self, amount: Decimal):
        pass


class CreditCartProcessor(RefundedPaymentProcessor):
    def charge(self, amount: Decimal):
        print(f"Charge ${amount}")

    def refund(self, amount: Decimal):
        print(f"Refunded ${amount}")


class CashDeliveryProcessor(PaymentProcessor):
    def charge(self, amount: Decimal):
        print("Payment will be collected on delivery")


def issue_refund(processor: RefundedPaymentProcessor, amount: Decimal):
    processor.refund(amount=amount)
