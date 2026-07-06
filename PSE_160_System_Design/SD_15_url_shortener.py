# System Design - Pub/Sub System
# -----------------------------------------------------------------------------
# Publish/Subscribe (Pub/Sub) is a messaging pattern where senders (publishers)
# send messages to topics without knowing who will receive them. Receivers
# (subscribers) express interest in topics and receive only relevant messages.
#
# Unlike a simple message queue (point-to-point), Pub/Sub is one-to-many:
# a single published message can be delivered to multiple subscribers.
#
# -----------------------------------------------------------------------------
# Core Flow:
#
#   Publisher → Topic → Subscriber 1
#                    → Subscriber 2
#                    → Subscriber 3
#
# -----------------------------------------------------------------------------
# Key Characteristics:
#
# 1. Decoupling
#    - Publishers don't know about subscribers
#    - Subscribers don't know about publishers
#    - They only share the topic name
#
# 2. Broadcast
#    - One message → many receivers
#    - New subscribers can join without publisher changes
#
# 3. Async Communication
#    - Publisher doesn't wait for subscribers
#    - Subscribers process at their own pace
#
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - Google Cloud Pub/Sub, AWS SNS, Redis Pub/Sub
# - Event-driven microservices
# - Real-time notifications (chat, alerts)
# - IoT sensor data distribution
# - Log aggregation
# -----------------------------------------------------------------------------

import time
from dataclasses import dataclass, field
from typing import Any, Callable

# -----------------------------------------------------------------------------
# Message
# -----------------------------------------------------------------------------


@dataclass
class Message:
    topic: str
    payload: dict[str, Any]
    timestamp: float = field(default_factory=time.time)
    message_id: str = ""

    def __post_init__(self):
        if not self.message_id:
            self.message_id = f"msg_{int(self.timestamp * 1000)}"


# -----------------------------------------------------------------------------
# Subscriber (Callback-based)
# -----------------------------------------------------------------------------


@dataclass
class Subscriber:
    name: str
    callback: Callable[[Message], None]
    received: list[Message] = field(default_factory=list)

    def on_message(self, message: Message):
        self.received.append(message)
        self.callback(message)


# -----------------------------------------------------------------------------
# Topic
# -----------------------------------------------------------------------------


class Topic:
    def __init__(self, name: str):
        self.name = name
        self.subscribers: list[Subscriber] = []
        self.message_history: list[Message] = []

    def subscribe(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)
        print(f"  [{self.name}] {subscriber.name} subscribed")

    def unsubscribe(self, subscriber: Subscriber):
        self.subscribers.remove(subscriber)
        print(f"  [{self.name}] {subscriber.name} unsubscribed")

    def publish(self, message: Message):
        message.topic = self.name
        self.message_history.append(message)
        print(f"  [{self.name}] Published: {message.payload}")

        for subscriber in self.subscribers:
            subscriber.on_message(message)


# -----------------------------------------------------------------------------
# Pub/Sub Broker
# -----------------------------------------------------------------------------


class PubSubBroker:
    """
    Central broker that manages topics and routes messages.
    Simulates systems like Redis Pub/Sub or Google Cloud Pub/Sub.
    """

    def __init__(self):
        self.topics: dict[str, Topic] = {}

    def create_topic(self, name: str) -> Topic:
        if name not in self.topics:
            self.topics[name] = Topic(name)
            print(f"  [Broker] Created topic: {name}")
        return self.topics[name]

    def subscribe(self, topic_name: str, subscriber: Subscriber):
        topic = self.topics.get(topic_name)
        if not topic:
            topic = self.create_topic(topic_name)
        topic.subscribe(subscriber)

    def publish(self, topic_name: str, payload: dict[str, Any]):
        topic = self.topics.get(topic_name)
        if not topic:
            topic = self.create_topic(topic_name)
        message = Message(topic=topic_name, payload=payload)
        topic.publish(message)

    def get_topic_stats(self) -> dict:
        stats = {}
        for name, topic in self.topics.items():
            stats[name] = {
                "subscribers": len(topic.subscribers),
                "messages": len(topic.message_history),
            }
        return stats


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    broker = PubSubBroker()

    # Create topics
    broker.create_topic("orders")
    broker.create_topic("notifications")

    # Create subscribers with callbacks
    def order_logger(msg: Message):
        print(f"    [Logger] Order received: {msg.payload}")

    def inventory_service(msg: Message):
        print(f"    [Inventory] Updating stock for: {msg.payload.get('product')}")

    def email_service(msg: Message):
        print(f"    [Email] Sending confirmation to: {msg.payload.get('customer')}")

    def analytics_service(msg: Message):
        print(f"    [Analytics] Tracking event: {msg.topic}")

    # Subscribe to topics
    print("\n--- Setting up subscriptions ---")
    broker.subscribe("orders", Subscriber("OrderLogger", order_logger))
    broker.subscribe("orders", Subscriber("InventoryService", inventory_service))
    broker.subscribe("orders", Subscriber("EmailService", email_service))
    broker.subscribe("notifications", Subscriber("AnalyticsService", analytics_service))

    # Publish messages
    print("\n--- Publishing to 'orders' ---")
    broker.publish(
        "orders",
        {"order_id": 1001, "product": "Laptop", "customer": "alice@example.com"},
    )

    print("\n--- Publishing to 'notifications' ---")
    broker.publish(
        "notifications",
        {"type": "page_view", "user": "user_42", "page": "/products"},
    )

    # Show stats
    print("\n--- Topic Stats ---")
    stats = broker.get_topic_stats()
    for topic, info in stats.items():
        print(
            f"  {topic}: {info['subscribers']} subscribers, {info['messages']} messages"
        )


if __name__ == "__main__":
    main()
