# Classes - Instance Methods
# -----------------------------------------------------------------------------
# Instance methods are functions defined inside a class that operate on
# instance data through the self parameter.
#
# Key concepts:
# 1. self parameter (reference to instance)
# 2. Methods that read/write instance state
# 3. Method chaining
# 4. Method as behavior
# -----------------------------------------------------------------------------
# Why instance methods matter:
#
# - Define what objects can DO (behavior)
# - Encapsulate logic that operates on instance data
# - Enable method chaining for fluent APIs
# - Enforce invariants through controlled access
# -----------------------------------------------------------------------------
# High-level flow:
#
# Object created → Call method → Method accesses self → Returns result
#      (state)       (action)        (reads/writes)       (or self for chaining)
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - account.deposit(100) — modify balance with validation
# - user.set_password("new") — hash and store securely
# - request.add_header("Auth", "token") — chain configuration
# - rect.scale(2).rotate(90) — fluent transformation API
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Instance Methods
# =============================================================================


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account."""
        self.balance += amount
        return self

    def withdraw(self, amount):
        """Remove money from the account."""
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self

    def get_balance(self):
        """Return current balance."""
        return self.balance

    def __repr__(self):
        return f"BankAccount({self.owner!r}, {self.balance})"


account = BankAccount("Alice", 100)
print(f"Initial: {account}")

account.deposit(50)
print(f"After deposit: {account.get_balance()}")

account.withdraw(30)
print(f"After withdraw: {account.get_balance()}")


# =============================================================================
# Method Chaining
# =============================================================================


account.deposit(200).withdraw(50).deposit(100)
print(f"After chain: {account.get_balance()}")


# =============================================================================
# Methods with Logic
# =============================================================================


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def scale(self, factor):
        """Return a new rectangle scaled by factor."""
        return Rectangle(self.width * factor, self.height * factor)


rect = Rectangle(5, 3)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")
print(f"Is square: {rect.is_square()}")

scaled = rect.scale(2)
print(f"Scaled: {scaled.width}x{scaled.height}")


def main():
    print("=== Instance Methods ===")
    rect = Rectangle(4, 4)
    print(f"Is square: {rect.is_square()}")
    print(f"Area: {rect.area()}")


if __name__ == "__main__":
    main()
