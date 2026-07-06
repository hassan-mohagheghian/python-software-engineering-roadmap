# Design Patterns - Template Method Pattern
# -----------------------------------------------------------------------------
# The Template Method Pattern defines the skeleton of an algorithm in a method,
# deferring some steps to subclasses. It lets subclasses redefine certain steps
# of an algorithm without changing the algorithm's structure.
#
# This pattern is based on inheritance and implements the "Hollywood Principle"
# ("Don't call us, we'll call you"). The parent class controls the execution flow,
# calling subclass methods when customization is needed.
#
# Benefits:
# - Promotes code reuse by placing common algorithm behavior in the base class.
# - Provides extension hooks for subclasses to customize specific steps.
# - Enforces a consistent step-by-step algorithm structure across variants.
#
# Real-world examples:
# - Ingesting files (open -> read -> parse -> close)
# - Build pipelines (checkout -> build -> test -> deploy)
# - Notification text generators (header -> body -> footer formatting per channel)
# -----------------------------------------------------------------------------


from abc import ABC, abstractmethod


# -----------------------------------------------------------------------------
# Abstract Class (Template)
# -----------------------------------------------------------------------------
class NotificationGenerator(ABC):
    """
    Abstract class defining the template method for generating notifications.
    Different channels (Email, SMS, Push) share the same overall creation 
    lifecycle but format the content differently.
    """

    def generate_notification(self, recipient: str, message: str) -> str:
        """
        The Template Method.
        Defines the skeleton for formatting a notification.
        """
        header = self.format_header(recipient)
        body = self.format_body(message)
        footer = self.format_footer()
        
        # Enforce assembly in a standard structure
        full_text = self.assemble(header, body, footer)
        return full_text

    @abstractmethod
    def format_header(self, recipient: str) -> str:
        """Step 1: Format header details (varies by channel)."""
        pass

    @abstractmethod
    def format_body(self, message: str) -> str:
        """Step 2: Format the main message body (varies by channel)."""
        pass

    def format_footer(self) -> str:
        """
        Step 3 (Hook): Optional footer formatting.
        Default implementation provided, but subclasses can override.
        """
        return "Sent via Antigravity Notification System."

    def assemble(self, header: str, body: str, footer: str) -> str:
        """
        Helper method to join the parts.
        """
        return f"{header}\n{body}\n{footer}\n" + "-" * 40


# -----------------------------------------------------------------------------
# Concrete Class 1: Email Notification Generator
# -----------------------------------------------------------------------------
class EmailNotificationGenerator(NotificationGenerator):
    """
    Formats the notification using HTML styling suitable for Emails.
    """

    def format_header(self, recipient: str) -> str:
        return f"To: <{recipient}>\nSubject: 📧 System Update\n<html>"

    def format_body(self, message: str) -> str:
        return f"  <body>\n    <p>{message}</p>\n  </body>"

    def format_footer(self) -> str:
        # Overrides hook to add HTML unsubscribe links
        return "  <footer>\n    <hr>\n    <a href='#'>Unsubscribe</a>\n  </footer>\n</html>"


# -----------------------------------------------------------------------------
# Concrete Class 2: SMS Notification Generator
# -----------------------------------------------------------------------------
class SMSNotificationGenerator(NotificationGenerator):
    """
    Formats the notification as plain text, enforcing SMS constraints.
    """

    def format_header(self, recipient: str) -> str:
        # SMS doesn't have headers, just the recipient phone
        return f"SMS to: {recipient}"

    def format_body(self, message: str) -> str:
        # Enforce SMS character limitations
        if len(message) > 120:
            print("[SMS Warning] Message too long, truncating body.")
            return message[:117] + "..."
        return message

    def format_footer(self) -> str:
        # Overrides hook for text-based opt-out footer
        return "Reply STOP to end."


# -----------------------------------------------------------------------------
# Concrete Class 3: Push Notification Generator
# -----------------------------------------------------------------------------
class PushNotificationGenerator(NotificationGenerator):
    """
    Formats highly concise push notification previews with emojis.
    """

    def format_header(self, recipient: str) -> str:
        return f"Push -> Device ({recipient})"

    def format_body(self, message: str) -> str:
        # Short alert style body
        return f"🔔 Alert: {message}"

    # Uses the base class format_footer() default implementation


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------
def main():
    message_content = "Your package has been dispatched and will arrive by 5 PM today."

    print("=== Generating Email Notification ===")
    email_gen = EmailNotificationGenerator()
    email_output = email_gen.generate_notification("hassan@example.com", message_content)
    print(email_output)
    print()

    print("=== Generating SMS Notification ===")
    sms_gen = SMSNotificationGenerator()
    # Test message truncation limit
    long_message = "Your package has been dispatched and will arrive by 5 PM today. Please make sure someone is at home to sign for it."
    sms_output = sms_gen.generate_notification("+1234567890", long_message)
    print(sms_output)
    print()

    print("=== Generating Push Notification ===")
    push_gen = PushNotificationGenerator()
    push_output = push_gen.generate_notification("UserDevice_992", message_content)
    print(push_output)
    print()


if __name__ == "__main__":
    main()
