# Classes - Private Attributes
# -----------------------------------------------------------------------------
# Python uses name mangling with double underscores to indicate private
# attributes. Single underscore is a convention for internal use.
#
# Key concepts:
# 1. _name — protected (convention only)
# 2. __name — private (name mangling)
# 3. Name mangling mechanics
# 4. Accessing private attributes
# -----------------------------------------------------------------------------
# Why private attributes matter:
#
# - Prevent accidental external modification
# - Enforce invariants (balance can't be set directly)
# - Protect sensitive data (passwords, tokens)
# - Reduce coupling between classes
# -----------------------------------------------------------------------------
# High-level flow:
#
# __attr → Python renames to _ClassName__attr → External code can't access
#  (private)          (name mangling)                  (encapsulation)
# -----------------------------------------------------------------------------
# Attribute visibility:
#
# public      -> obj.attr
# protected   -> obj._attr      (convention only)
# private     -> obj.__attr     (name mangling)
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - account.__balance — prevent direct balance manipulation
# - user.__password_hash — protect credentials
# - db.__connection_pool — manage internal resources
# - config.__secret_key — sensitive configuration
# -----------------------------------------------------------------------------
# Name mangling:
#
# Python renames __balance to _Account__balance
# This prevents accidental access, but isn't security (can be bypassed)
# -----------------------------------------------------------------------------


# =============================================================================
# Protected vs Private
# =============================================================================


class Account:
    def __init__(self, owner, balance):
        self.owner = owner  # public
        self._bank = "Chase"  # protected (convention)
        self.__balance = balance  # private (mangled)

    def get_balance(self):
        return self.__balance


acc = Account("Alice", 1000)

print(f"Owner: {acc.owner}")
print(f"Bank: {acc._bank}")
print(f"Balance: {acc.get_balance()}")

# print(acc.__balance)  # AttributeError


# =============================================================================
# Name Mangling
# =============================================================================

# Python renames __balance to _Account__balance
print(f"Mangled: {acc._Account__balance}")  # pyright: ignore[reportAttributeAccessIssue]


# =============================================================================
# Practical Example
# =============================================================================


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self.__transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.__balance += amount
        self.__transactions.append(("deposit", amount))
        return self

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")

        self.__balance -= amount
        self.__transactions.append(("withdraw", amount))
        return self

    @property
    def balance(self):
        """Read-only balance."""
        return self.__balance

    @property
    def transactions(self):
        """Return a copy of transactions."""
        return list(self.__transactions)


account = BankAccount("Alice", 100)

account.deposit(50).withdraw(30)

print(f"Balance: {account.balance}")
print(f"Transactions: {account.transactions}")


# Creating account.__balance creates a NEW instance attribute.
# It does NOT modify the real private attribute.
account.__balance = 999999

print(f"Actual balance: {account.balance}")
print(f"Fake attribute: {account.__balance}")


# =============================================================================
# Inheritance and Private Attributes
# =============================================================================


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)

        # This would NOT work:
        # self.__balance += interest
        #
        # __balance is private to BankAccount.
        # It becomes _BankAccount__balance internally.


savings = SavingsAccount("Bob", 1000, 0.05)

savings.add_interest()

print(f"Savings balance: {savings.balance}")


def main():
    print("=== Private Attributes ===")

    acc = BankAccount("Charlie", 500)
    acc.deposit(200)

    print(f"Balance: {acc.balance}")
    print(f"Transactions: {acc.transactions}")


if __name__ == "__main__":
    main()
