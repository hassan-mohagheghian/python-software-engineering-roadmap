# Design Patterns - Null Object Pattern
# -------------------------------------------------------------------------
# The Null Object Pattern provides an object that encapsulates the absence
# of an object by providing a do-nothing relationship or default behavior.
#
# Instead of using None or checking for null references (e.g., if obj is not None),
# the client calls the null object's methods, which safely do nothing.
#
# Benefits:
# - Eliminates repetitive and error-prone None checks (if obj is not None)
# - Simplifies client code by making it uniform and polymorphic
# - Provides a safe, default fallback implementation of an interface
# - Highly compatible with Python's duck typing and dynamic nature
#
# Real-world examples:
# - A NullLogger that suppresses logging output
# - A NullNotificationService that passes on sending notifications
# - An EmptyCallback or NullHandler in event handling
#
# ---------------------------Example------------------------------------------
# In this example:
#
# - NotificationService is the common interface.
# - EmailNotification and SMSNotification are concrete, active implementations.
# - NullNotification is the Null Object (passive implementation doing nothing).
# - UserRegistration is the context class that uses a NotificationService.
#
# The UserRegistration class does not need to check if the notification service
# is None. It can simply call send_notification() unconditionally.
#
# -----------------------------------------------------------------------------
#
# Relationship to OOP Concepts:
#
# - Abstraction:
#     NotificationService defines the common contract.
#
# - Polymorphism:
#     NullNotification and active notifications implement the same interface,
#     so the client uses them interchangeably.
#
# - Composition:
#     UserRegistration contains/uses a NotificationService.
#
# - Dependency Injection:
#     The notification service is injected into UserRegistration.
#
# Relationship to SOLID:
#
# - LSP (Liskov Substitution Principle):
#     NullNotification behaves as a true subtype of NotificationService
#     without changing program semantics or throwing unexpected exceptions.
#
# - OCP (Open/Closed Principle):
#     New notification types or a null fallback can be introduced without
#     modifying UserRegistration.
# -----------------------------------------------------------------------------


from abc import ABC, abstractmethod


class NotificationService(ABC):
    """
    Interface/Abstract Base Class for notification services.
    """

    @abstractmethod
    def send(self, message: str) -> None:
        """Send a notification message."""
        pass


class EmailNotification(NotificationService):
    """
    Concrete implementation of NotificationService for email delivery.
    """

    def __init__(self, email_address: str):
        self.email_address = email_address

    def send(self, message: str) -> None:
        print(f"Sending Email to {self.email_address}: {message}")


class SMSNotification(NotificationService):
    """
    Concrete implementation of NotificationService for SMS delivery.
    """

    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def send(self, message: str) -> None:
        print(f"Sending SMS to {self.phone_number}: {message}")


class NullNotification(NotificationService):
    """
    The Null Object implementation of NotificationService.

    It implements the same interface but performs no operation (do-nothing).
    """

    def send(self, message: str) -> None:
        # Do nothing: safely ignore the call
        pass


class UserRegistration:
    """
    Context class that processes user registrations and notifies them.
    """

    def __init__(self, username: str, notifier: NotificationService | None = None):
        self.username = username
        # Use NullNotification as the default to avoid None/null checks later.
        self.notifier = notifier if notifier is not None else NullNotification()

    def register(self) -> None:
        print(f"Registering user: {self.username}...")
        # Unconditional call. No need for: if self.notifier: self.notifier.send(...)
        self.notifier.send(f"Welcome to our platform, {self.username}!")
        print("Registration completed successfully.")


if __name__ == "__main__":
    # Case 1: Active notifications via Email
    print("--- Case 1: User registers with Email notification ---")
    email_notifier = EmailNotification("user@example.com")
    reg_with_email = UserRegistration("alice_dev", email_notifier)
    reg_with_email.register()

    print("\n--- Case 2: User registers with SMS notification ---")
    sms_notifier = SMSNotification("+1-555-0199")
    reg_with_sms = UserRegistration("bob_coder", sms_notifier)
    reg_with_sms.register()

    # Case 3: No notifications requested (uses NullNotification)
    print("\n--- Case 3: User registers with NO notification ---")
    # No notifier is passed, so it defaults to NullNotification.
    # The registration process executes without checking for None.
    reg_no_notify = UserRegistration("silent_user")
    reg_no_notify.register()
