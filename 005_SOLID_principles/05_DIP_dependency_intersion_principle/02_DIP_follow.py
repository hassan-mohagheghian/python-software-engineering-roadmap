# SOLID Principles in Python
# DIP - Dependency Inversion Principle
# an DIP follow Example
# -------------------------------------------------------
# The Dependency Inversion Principle states that high-level
# modules should not depend on low-level modules.
# Both should depend on abstractions (e.g., interfaces or
# abstract classes).
# --------------------------------------------------------
# In this example, we define an abstract EmailService interface
# that both the high-level OrderProcessor and the low-level
# EmailService implementation depend on. The OrderProcessor
# class depends on the EmailService abstraction rather than a
# concrete implementation, allowing for greater flexibility and
# easier testing. This design follows the Dependency Inversion
# Principle, as it decouples the high-level module (OrderProcessor) from the
# low-level module (EmailService), making the code more maintainable and adaptable to change.


from abc import ABC, abstractmethod


class EmailService(ABC):
    """Abstraction for email services."""

    @abstractmethod
    def send_email(self, recipient: str, subject: str, body: str):
        pass


class SmtpEmailService(EmailService):
    """Concrete implementation of EmailService using SMTP."""

    def send_email(self, recipient: str, subject: str, body: str):
        print(
            f"Sending email to {recipient} with subject '{subject}' and body '{body}' using SMTP"
        )


class OrderProcessor:
    """High-level module that processes orders and sends notifications."""

    def __init__(self, email_service: EmailService):
        self.email_service = email_service  # Dependency on abstraction

    def process_order(self, order_id: int, customer_email: str):
        print(f"Processing order {order_id}")
        # After processing the order, send a notification email
        self.email_service.send_email(
            recipient=customer_email,
            subject="Order Confirmation",
            body=f"Your order {order_id} has been processed.",
        )


if __name__ == "__main__":
    email_service = SmtpEmailService()  # Create a concrete email service
    processor = OrderProcessor(email_service=email_service)  # Inject the dependency
    processor.process_order(order_id=123, customer_email="customer@example.com")
