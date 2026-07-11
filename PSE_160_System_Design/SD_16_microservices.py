# System Design - Microservices Architecture
# -----------------------------------------------------------------------------
# Microservices Architecture splits one large application into small services.
# Each service owns one business capability and can be developed, deployed, and
# scaled independently.
#
# -----------------------------------------------------------------------------
# Why use microservices?
#
# - Independent deployment
# - Independent scaling
# - Clear service ownership
# - Better fault isolation
# - Easier integration with different technologies
#
# -----------------------------------------------------------------------------
# Trade-offs:
#
# - More network communication
# - More operational complexity
# - Data consistency becomes harder
# - Observability and debugging need more discipline
#
# -----------------------------------------------------------------------------
# High-Level Architecture
#
#                  Client
#                    |
#                    v
#              API Gateway
#          /        |        \
#         v         v         v
#   User Service Order Service Payment Service
#         |         |          |
#         v         v          v
#      User DB   Order DB   Payment DB
#
# Services can communicate synchronously through direct calls or asynchronously
# through events.
# -----------------------------------------------------------------------------

from collections import defaultdict
from dataclasses import dataclass
from typing import Callable


# -----------------------------------------------------------------------------
# Event Bus
# -----------------------------------------------------------------------------


class EventBus:
    """
    Simple in-memory event bus for asynchronous service communication.
    """

    def __init__(self):
        self.subscribers: dict[str, list[Callable]] = defaultdict(list)

    def subscribe(self, event_name: str, handler: Callable):
        self.subscribers[event_name].append(handler)

    def publish(self, event_name: str, payload: dict):
        print(f"[EventBus] Published event: {event_name}")

        for handler in self.subscribers[event_name]:
            handler(payload)


# -----------------------------------------------------------------------------
# User Service
# -----------------------------------------------------------------------------


class UserService:
    """
    Owns user data.
    """

    def __init__(self):
        self.users = {
            1: {"id": 1, "name": "Alice"},
            2: {"id": 2, "name": "Bob"},
        }

    def get_user(self, user_id: int):
        print(f"[UserService] Fetching user {user_id}")
        return self.users.get(user_id)


# -----------------------------------------------------------------------------
# Order Service
# -----------------------------------------------------------------------------


@dataclass
class Order:
    order_id: int
    user_id: int
    amount: float
    status: str


class OrderService:
    """
    Owns order data.
    """

    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.orders: dict[int, Order] = {}
        self.next_order_id = 1001

    def create_order(self, user_id: int, amount: float) -> Order:
        order = Order(
            order_id=self.next_order_id,
            user_id=user_id,
            amount=amount,
            status="created",
        )

        self.orders[order.order_id] = order
        self.next_order_id += 1

        print(f"[OrderService] Created order {order.order_id}")

        self.event_bus.publish(
            "order_created",
            {
                "order_id": order.order_id,
                "user_id": user_id,
                "amount": amount,
            },
        )

        return order

    def mark_paid(self, order_id: int):
        order = self.orders.get(order_id)

        if not order:
            print(f"[OrderService] Order {order_id} not found")
            return

        order.status = "paid"
        print(f"[OrderService] Marked order {order_id} as paid")


# -----------------------------------------------------------------------------
# Payment Service
# -----------------------------------------------------------------------------


class PaymentService:
    """
    Owns payment data and reacts to order events.
    """

    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.payments = {}

        self.event_bus.subscribe("order_created", self.process_payment)

    def process_payment(self, payload: dict):
        order_id = payload["order_id"]
        amount = payload["amount"]

        print(f"[PaymentService] Charging ${amount:.2f} for order {order_id}")

        self.payments[order_id] = {
            "order_id": order_id,
            "amount": amount,
            "status": "paid",
        }

        self.event_bus.publish(
            "payment_completed",
            {
                "order_id": order_id,
                "status": "paid",
            },
        )


# -----------------------------------------------------------------------------
# Notification Service
# -----------------------------------------------------------------------------


class NotificationService:
    """
    Sends messages when important events happen.
    """

    def __init__(self, event_bus: EventBus):
        event_bus.subscribe("payment_completed", self.send_payment_receipt)

    def send_payment_receipt(self, payload: dict):
        print(
            "[NotificationService] Sent receipt for "
            f"order {payload['order_id']}"
        )


# -----------------------------------------------------------------------------
# API Gateway
# -----------------------------------------------------------------------------


class APIGateway:
    """
    Single entry point for clients.

    The gateway hides internal service locations from the client.
    """

    def __init__(self, user_service: UserService, order_service: OrderService):
        self.user_service = user_service
        self.order_service = order_service

    def create_order(self, user_id: int, amount: float):
        print("\n[Gateway] POST /orders")

        user = self.user_service.get_user(user_id)

        if not user:
            print("[Gateway] Request failed: user not found")
            return None

        order = self.order_service.create_order(user_id, amount)

        print(
            "[Gateway] Response: "
            f"order_id={order.order_id}, status={order.status}"
        )

        return order


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    event_bus = EventBus()

    user_service = UserService()
    order_service = OrderService(event_bus)
    payment_service = PaymentService(event_bus)
    notification_service = NotificationService(event_bus)

    event_bus.subscribe(
        "payment_completed",
        lambda payload: order_service.mark_paid(payload["order_id"]),
    )

    gateway = APIGateway(user_service, order_service)

    gateway.create_order(user_id=1, amount=49.99)
    gateway.create_order(user_id=2, amount=19.99)
    gateway.create_order(user_id=999, amount=9.99)

    print("\n===== Service-Owned Data =====")
    print(f"Orders: {order_service.orders}")
    print(f"Payments: {payment_service.payments}")
    print(f"Notifications handled by: {notification_service.__class__.__name__}")


if __name__ == "__main__":
    main()
