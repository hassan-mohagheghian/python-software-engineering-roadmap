# SOLID Principles - Dependency Inversion Principle
# -----------------------------------------------------------------------------
# High-level modules should not depend on low-level modules.
# Both should depend on abstractions (interfaces/abstract classes).
#
# Benefits:
# - Decouples high-level logic from low-level implementations
# - Easier to swap or mock dependencies
# - Improves testability and maintainability
#
# Real-world examples:
# - Email services (SMTP vs API)
# - Database drivers (PostgreSQL vs SQLite)
# - Notification systems (email vs SMS vs push)
# -----------------------------------------------------------------------------


# =============================================================================
# VIOLATION: High-level module directly depends on low-level module
# =============================================================================


class EmailService:
    """Low-level module responsible for sending emails."""

    def send_email(self, recipient: str, subject: str, body: str):
        print(
            f"Sending email to {recipient} with subject '{subject}' and body '{body}'"
        )


class OrderProcessor:
    """High-level module that processes orders and sends notifications."""

    def __init__(self):
        self.email_service = EmailService()  # Direct dependency on low-level module

    def process_order(self, order_id: int, customer_email: str):
        print(f"Processing order {order_id}")
        self.email_service.send_email(
            recipient=customer_email,
            subject="Order Confirmation",
            body=f"Your order {order_id} has been processed.",
        )


# =============================================================================
# FOLLOW: Both modules depend on an abstraction
# =============================================================================

from abc import ABC, abstractmethod


class MessageService(ABC):
    """Abstraction for notification services."""

    @abstractmethod
    def send(self, recipient: str, subject: str, body: str):
        pass


class SmtpEmailService(MessageService):
    """Concrete implementation using SMTP."""

    def send(self, recipient: str, subject: str, body: str):
        print(
            f"Sending email to {recipient} with subject '{subject}' and body '{body}' via SMTP"
        )


class SmsService(MessageService):
    """Concrete implementation using SMS."""

    def send(self, recipient: str, subject: str, body: str):
        print(f"Sending SMS to {recipient}: {body}")


class OrderProcessor:
    """High-level module depends on abstraction, not concrete class."""

    def __init__(self, message_service: MessageService):
        self.message_service = message_service

    def process_order(self, order_id: int, customer_email: str):
        print(f"Processing order {order_id}")
        self.message_service.send(
            recipient=customer_email,
            subject="Order Confirmation",
            body=f"Your order {order_id} has been processed.",
        )


# =============================================================================
# Usage
# =============================================================================

if __name__ == "__main__":
    # Violation
    print("=== Violation ===")
    processor = OrderProcessor()
    processor.process_order(order_id=123, customer_email="customer@example.com")

    # Follow
    print("\n=== Follow ===")
    smtp = SmtpEmailService()
    processor = OrderProcessor(message_service=smtp)
    processor.process_order(order_id=456, customer_email="customer@example.com")

    # Easy to swap
    sms = SmsService()
    processor = OrderProcessor(message_service=sms)
    processor.process_order(order_id=789, customer_email="+1234567890")
