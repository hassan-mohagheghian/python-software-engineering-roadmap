# Error Handling - Custom Exceptions
# -----------------------------------------------------------------------------
# Custom exceptions let you create meaningful error types for your domain.
# They help callers handle specific failure modes appropriately.
#
# Key concepts:
# 1. Inheriting from Exception
# 2. Adding context with __init__
# 3. Exception hierarchy
# 4. Raising with 'raise from'
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Custom Exception
# =============================================================================


class InsufficientFundsError(Exception):
    """Raised when an account has insufficient funds."""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw ${amount:.2f}: balance is ${balance:.2f}")


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance


account = BankAccount(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"Error: {e}")
    print(f"  Tried: ${e.amount}, Balance: ${e.balance}")


# =============================================================================
# Exception Hierarchy
# =============================================================================


class AppError(Exception):
    """Base exception for application errors."""

    pass


class ValidationError(AppError):
    """Raised when input validation fails."""

    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"Validation failed for '{field}': {message}")


class NotFoundError(AppError):
    """Raised when a resource is not found."""

    def __init__(self, resource, identifier):
        self.resource = resource
        self.identifier = identifier
        super().__init__(f"{resource} with id '{identifier}' not found")


# =============================================================================
# raise from — Exception Chaining
# =============================================================================


class DatabaseError(Exception):
    pass


class UserNotFoundError(DatabaseError):
    pass


def find_user(user_id):
    try:
        # Simulated database error
        raise ConnectionError("DB connection lost")
    except ConnectionError as e:
        raise UserNotFoundError(f"Cannot find user {user_id}") from e


try:
    find_user(42)
except UserNotFoundError as e:
    print(f"Chained: {e}")
    print(f"  Original: {e.__cause__}")


def main():
    print("=== Custom Exceptions ===")
    account = BankAccount(50)
    try:
        account.withdraw(100)
    except InsufficientFundsError as e:
        print(f"Caught: {e}")


if __name__ == "__main__":
    main()
