# Design Patterns - Observer Pattern
# -----------------------------------------------------------------------------
# The Observer Pattern defines a one-to-many dependency between objects so that
# when one object changes state, all its dependents are notified and updated
# automatically.
#
# It is the foundation of Event-Driven programming, Publish-Subscribe (Pub/Sub)
# architectures, and model-view updates.
#
# Benefits:
# - Establishes loose coupling between the Subject (Publisher) and Observers (Subscribers).
# - Supports broadcast-style communication.
# - Allows adding or removing observers dynamically at runtime without modifying the Subject.
#
# Real-world examples:
# - Newsletter/Blog subscriptions (users subscribing to topics)
# - GUI event handlers (clicking a button notifies action listeners)
# - Stocks/Crypto price tickers notifying dashboard widgets
# - E-commerce orders notifying Inventory, Billing, and SMS dispatch services
# -----------------------------------------------------------------------------


from abc import ABC, abstractmethod


# -----------------------------------------------------------------------------
# Observer (Subscriber) Interface
# -----------------------------------------------------------------------------
class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects
    to notify the observer of state changes.
    """

    @abstractmethod
    def update(self, event_type: str, data: str):
        pass


# -----------------------------------------------------------------------------
# Subject (Publisher) Interface / Base Class
# -----------------------------------------------------------------------------
class Subject(ABC):
    """
    The Subject interface declares methods for managing subscribers (observers).
    """

    def __init__(self):
        self._observers: list[Observer] = []

    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"[Subject] Attached an observer: {observer.__class__.__name__}")

    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"[Subject] Detached an observer: {observer.__class__.__name__}")

    def notify(self, event_type: str, data: str):
        """Notifies all registered observers of an event."""
        for observer in self._observers:
            observer.update(event_type, data)


# -----------------------------------------------------------------------------
# Concrete Subject: News Agency
# -----------------------------------------------------------------------------
class NewsAgency(Subject):
    """
    A concrete Subject that holds some state (latest news) and notifies
    observers when the state changes.
    """

    def __init__(self):
        super().__init__()
        self._latest_news: str = ""

    def publish_news(self, category: str, headline: str):
        print(f"\n[NewsAgency] Publishing breaking news in {category}: '{headline}'")
        self._latest_news = headline
        # Notify all observers about this specific event type
        self.notify(event_type=category, data=headline)


# -----------------------------------------------------------------------------
# Concrete Observers: Subscribers
# -----------------------------------------------------------------------------
class EmailSubscriber(Observer):
    def __init__(self, email: str):
        self.email = email

    def update(self, event_type: str, data: str):
        # Email subscriber might care about all news categories
        print(f"[Email Notification] Sent to {self.email} -> [{event_type}] {data}")


class SmsSubscriber(Observer):
    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def update(self, event_type: str, data: str):
        # SMS subscriber might only care if it's "Urgent" or "Tech"
        if event_type in ["Urgent", "Tech"]:
            print(f"[SMS Notification] Sent to {self.phone_number} -> BREAKING: {data}")
        else:
            print(f"[SMS Filtered] Ignored '{event_type}' news for {self.phone_number}")


class PushNotifier(Observer):
    def __init__(self, device_id: str):
        self.device_id = device_id

    def update(self, event_type: str, data: str):
        # Push notification service pushes everything with an alert title
        print(f"[Push Notification] Sent to Device {self.device_id} -> 🔔 New {event_type} update: {data}")


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------
def main():
    # 1. Create the Subject (Publisher)
    news_agency = NewsAgency()

    # 2. Create Observers (Subscribers)
    email_sub = EmailSubscriber("hassan@example.com")
    sms_sub = SmsSubscriber("+1234567890")
    push_sub = PushNotifier("Device_Android_404")

    # 3. Register Subscribers
    print("--- Subscribing Observers ---")
    news_agency.attach(email_sub)
    news_agency.attach(sms_sub)
    news_agency.attach(push_sub)

    # 4. Publish News (trigger notifications)
    news_agency.publish_news("Tech", "Python 3.14 officially released with new features!")

    # 5. Publish another category (showing conditional filtering in SmsSubscriber)
    news_agency.publish_news("Sports", "Local team wins the championship.")

    # 6. Unsubscribe an observer
    print("\n--- Unsubscribing Email Observer ---")
    news_agency.detach(email_sub)

    # 7. Publish news again (only remaining observers get notified)
    news_agency.publish_news("Urgent", "Severe weather warning in your area.")


if __name__ == "__main__":
    main()
