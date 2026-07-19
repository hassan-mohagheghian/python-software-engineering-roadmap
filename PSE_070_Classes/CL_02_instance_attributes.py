# Classes - Instance Attributes
# -----------------------------------------------------------------------------
# Instance attributes are data unique to each object. They are created
# inside __init__ and stored on self.
#
# Key concepts:
# 1. Public attributes — accessible anywhere
# 2. Protected attributes (_name) — convention for internal use
# 3. Private attributes (__name) — name mangling for encapsulation
# 4. Attribute access patterns
# -----------------------------------------------------------------------------
# Why attribute access control matters:
#
# - Prevent accidental modification of internal state
# - Enforce invariants (e.g., balance can't go negative)
# - Communicate intent (public API vs internal detail)
# - Support subclassing without breaking encapsulation
# -----------------------------------------------------------------------------
# High-level flow:
#
# Class defines attributes → __init__ sets defaults → Methods enforce rules
#       (blueprint)              (construction)          (controlled access)
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - Bank account: _balance (protected), deposit() (public API)
# - User profile: __password_hash (private), check_password() (public API)
# - Database connection: _connection_pool (protected), query() (public API)
# -----------------------------------------------------------------------------

# =============================================================================
# Public Attributes
# =============================================================================


class Person:
    """Public attributes — accessible from anywhere."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


p = Person("Alice", 30)
print(f"Name: {p.name}")
print(f"Age: {p.age}")

# Direct modification — works but no validation
p.name = "Bob"
print(f"Updated name: {p.name}")


# =============================================================================
# Protected Attributes (convention: _prefix)
# =============================================================================


class BankAccount:
    """Protected attributes signal internal use only."""

    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self._pin = "123"
        self._balance = balance

    def deposit(self, amount: int):
        if amount > 0:
            self._balance += amount
            self._log_transaction(amount)

    def get_balance(self):
        return self._balance

    def _log_transaction(self, amount: int):
        """Internal method — not part of public API."""
        print(f"Transaction: {amount}")


account = BankAccount("Alice", 8000)

# Accessible but discouraged — underscore warns you
print(f"Pin: {account._pin}")
account._balance = 9000  # works but you're bypassing validation

# Preferred: use public methods
print(f"Balance: {account.get_balance()}")


# =============================================================================
# Protected Attributes with Subclasses
# =============================================================================


class Vehicle:
    def __init__(self):
        self._engine_status = "off"

    def _start_engine(self):
        self._engine_status = "on"
        print("Engine started")


class Car(Vehicle):
    def drive(self):
        # Subclass can access protected members
        self._start_engine()
        print(f"Driving with engine {self._engine_status}")


car = Car()
car.drive()


# =============================================================================
# Private Attributes (name mangling: __prefix)
# =============================================================================


class SecureAccount:
    """Private attributes use name mangling for extra protection."""

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.__balance = balance
        self.__transactions: list[str] = []

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount
        self.__transactions.append(f"deposit:{amount}")
        return self

    def withdraw(self, amount: float):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        self.__transactions.append(f"withdraw:{amount}")
        return self

    @property
    def balance(self):
        """Read-only access via property."""
        return self.__balance

    @property
    def transactions(self):
        """Return a copy to prevent external modification."""
        return list(self.__transactions)


def main():
    print("=== Instance Attributes ===")

    acc = SecureAccount("Bob", 500)
    acc.deposit(200).withdraw(50)
    print(f"Balance: {acc.balance}")
    print(f"Transactions: {acc.transactions}")

    # Direct access fails — creates a new attribute, doesn't modify private
    acc.__balance = 999999
    print(f"Still original: {acc.balance}")  # unchanged


if __name__ == "__main__":
    main()
