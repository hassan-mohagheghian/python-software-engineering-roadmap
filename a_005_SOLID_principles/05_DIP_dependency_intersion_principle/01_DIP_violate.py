# SOLID Principles in Python
# DIP - Dependency Inversion Principle
# an DIP violate Example
# -------------------------------------------------------
# The Dependency Inversion Principle states that high-level
# modules should not depend on low-level modules.
# Both should depend on abstractions (e.g., interfaces or
# abstract classes).
# --------------------------------------------------------
# In this example, the OrderProcessor class directly depends on the EmailService class.
# This creates a tight coupling between the two classes, making it difficult to change
# the email sending mechanism without modifying the OrderProcessor class. This design
# violates the Dependency Inversion Principle, as the high-level module (OrderProcessor)
# depends on a low-level module (EmailService) instead of an abstraction. This can lead
# to issues such as difficulty in testing and maintenance, as changes to the EmailService
# may require changes to the OrderProcessor class.


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
        # After processing the order, send a notification email
        self.email_service.send_email(
            recipient=customer_email,
            subject="Order Confirmation",
            body=f"Your order {order_id} has been processed.",
        )


if __name__ == "__main__":
    processor = OrderProcessor()
    processor.process_order(order_id=123, customer_email="customer@example.com")
    # This design is problematic because if we want to change how emails are sent
    # (e.g., using a different email service or adding logging),
    # we would need to modify the OrderProcessor class,
    # which violates the Dependency Inversion Principle.
