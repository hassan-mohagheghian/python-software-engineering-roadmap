# Design Patterns - Mediator Pattern
# -------------------------------------------------------------------------
# The Mediator Pattern defines how a set of objects interact with each other.
# It promotes loose coupling by avoiding explicit references between objects,
# and allows them to communicate through a central mediator object.
#
# Instead of having objects directly communicate with each other, they
# communicate through the mediator, which controls and coordinates their interactions.
#
# Benefits:
# - Reduces the number of communication pathways between objects
# - Promotes loose coupling between components
# - Centralizes complex communication logic
# - Makes it easier to modify and extend object interactions
#
# Real-world examples:
# - Chat applications (users communicate through a chat server)
# - Air traffic control (planes communicate with controllers, not each other)
# - GUI components (buttons, text fields, etc. communicating through a dialog manager)
# - Trading systems (buyers, sellers, and exchanges mediated by a broker)
#
# Relationship to OOP Concepts:
#
# - Encapsulation:
#     The mediator encapsulates the communication logic.
#
# - Composition:
#     The mediator holds references to colleague objects.
#
# - Dependency Injection:
#     Colleagues are injected into the mediator.
#
# Relationship to SOLID:
#
# - OCP:
#     New colleagues can be added without changing existing code.
#
# - DIP:
#     Colleagues depend on abstractions (mediator interface) rather than concrete classes.
# -----------------------------------------------------------------------------


from abc import ABC, abstractmethod
from typing import List


class Mediator(ABC):
    """
    Mediator interface
    
    Defines the communication protocol between colleagues
    """
    
    @abstractmethod
    def notify(self, sender, event: str):
        """
        Handle notifications from colleagues
        
        Args:
            sender: The colleague that sent the notification
            event: The event that occurred
        """
        pass


class Colleague(ABC):
    """
    Base class for all colleagues
    
    Colleagues interact with each other through the mediator
    """
    
    def __init__(self, mediator: Mediator):
        self._mediator = mediator
        
    @abstractmethod
    def send(self, message: str):
        """Send a message to the mediator"""
        pass
        
    @abstractmethod
    def receive(self, message: str):
        """Receive a message from the mediator"""
        pass


class ChatMediator(Mediator):
    """
    Concrete mediator for a chat room
    
    Manages communication between chat participants
    """
    
    def __init__(self):
        self._colleagues: List[Colleague] = []
        
    def add_colleague(self, colleague: Colleague):
        """Add a participant to the chat"""
        self._colleagues.append(colleague)
        
    def notify(self, sender: Colleague, event: str):
        """Handle notifications from colleagues"""
        # Forward the message to all other colleagues except the sender
        for colleague in self._colleagues:
            if colleague != sender:
                colleague.receive(f"[{sender.__class__.__name__}]: {event}")


class User(Colleague):
    """
    Concrete colleague representing a chat user
    
    Users can send and receive messages via the mediator
    """
    
    def __init__(self, mediator: Mediator, name: str):
        super().__init__(mediator)
        self.name = name
        
    def send(self, message: str):
        """Send a message to the chat room"""
        print(f"{self.name} sends: {message}")
        self._mediator.notify(self, message)
        
    def receive(self, message: str):
        """Receive a message from the chat room"""
        print(f"{self.name} receives: {message}")


class NotificationSystem(Mediator):
    """
    Concrete mediator for a notification system
    
    Manages communication between different notification services
    """
    
    def __init__(self):
        self._services: List[Colleague] = []
        
    def add_service(self, service: Colleague):
        """Add a notification service"""
        self._services.append(service)
        
    def notify(self, sender: Colleague, event: str):
        """Handle notifications from services"""
        # Forward the notification to all other services
        for service in self._services:
            if service != sender:
                service.receive(f"[{sender.__class__.__name__}]: {event}")


class EmailService(Colleague):
    """
    Concrete colleague for email notifications
    """
    
    def send(self, message: str):
        """Send an email notification"""
        print(f"Email Service sending: {message}")
        self._mediator.notify(self, message)
        
    def receive(self, message: str):
        """Receive notification about email"""
        print(f"Email Service received: {message}")


class SMSNotification(Colleague):
    """
    Concrete colleague for SMS notifications
    """
    
    def send(self, message: str):
        """Send an SMS notification"""
        print(f"SMS Service sending: {message}")
        self._mediator.notify(self, message)
        
    def receive(self, message: str):
        """Receive notification about SMS"""
        print(f"SMS Service received: {message}")


class PushNotification(Colleague):
    """
    Concrete colleague for push notifications
    """
    
    def send(self, message: str):
        """Send a push notification"""
        print(f"Push Service sending: {message}")
        self._mediator.notify(self, message)
        
    def receive(self, message: str):
        """Receive notification about push notification"""
        print(f"Push Service received: {message}")


def main():
    print("=== Testing Chat Room with Mediator Pattern ===")
    
    # Create mediator
    chat_mediator = ChatMediator()
    
    # Create colleagues
    alice = User(chat_mediator, "Alice")
    bob = User(chat_mediator, "Bob")
    charlie = User(chat_mediator, "Charlie")
    
    # Register colleagues with mediator
    chat_mediator.add_colleague(alice)
    chat_mediator.add_colleague(bob)
    chat_mediator.add_colleague(charlie)
    
    # Alice sends a message
    alice.send("Hello everyone!")
    
    print("\n=== Testing Notification System with Mediator Pattern ===")
    
    # Create notification system mediator
    notification_mediator = NotificationSystem()
    
    # Create notification services
    email_service = EmailService(notification_mediator)
    sms_service = SMSNotification(notification_mediator)
    push_service = PushNotification(notification_mediator)
    
    # Register services with mediator
    notification_mediator.add_service(email_service)
    notification_mediator.add_service(sms_service)
    notification_mediator.add_service(push_service)
    
    # Send notification from email service
    email_service.send("User registered successfully")


if __name__ == "__main__":
    main()