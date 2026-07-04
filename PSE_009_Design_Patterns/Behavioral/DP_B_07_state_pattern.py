# Design Patterns - State Pattern
# -----------------------------------------------------------------------------
# The State Pattern is a behavioral design pattern that allows an object to
# alter its behavior when its internal state changes. The object will appear
# to change its class at runtime.
#
# It encapsulates each state into a separate class and delegates behavior
# to the current state object, eliminating complex conditional logic.
#
# -----------------------------------------------------------------------------
# When to use:
#
# - An object's behavior depends on its state, and it must change behavior
#   at runtime based on that state.
# - You have many states and transitions, leading to large if/elif/switch blocks.
# - State-specific logic is scattered across the class and hard to maintain.
# - You want to follow the Open/Closed Principle: adding new states without
#   modifying existing code.
#
# -----------------------------------------------------------------------------
# Key Idea:
#
#   Context  --->  State (interface)
#     |               ^
#     |               |--- ConcreteStateA.handle()
#     |               |--- ConcreteStateB.handle()
#     +-- delegates behavior to current_state
#
#   Each state knows which state comes next (transitions).
#
# -----------------------------------------------------------------------------
# Benefits:
#
# - Eliminates complex conditional logic (no giant if/elif chains).
# - Single Responsibility: each state class handles its own behavior.
# - Open/Closed: add new states without modifying existing state classes.
# - State transitions are explicit and centralized within each state.
#
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - Order lifecycle (pending -> paid -> shipped -> delivered -> cancelled)
# - Vending machine (idle -> selecting -> dispensing -> returning change)
# - TCP connection (closed -> listen -> established -> fin-wait)
# - Document workflow (draft -> review -> published -> archived)
# - Media player (stopped -> playing -> paused)
# -----------------------------------------------------------------------------

from __future__ import annotations

from abc import ABC, abstractmethod

# -----------------------------------------------------------------------------
# State Interface
# -----------------------------------------------------------------------------


class OrderState(ABC):
    """Interface for all order states."""

    @abstractmethod
    def pay(self, order: Order) -> str:
        pass

    @abstractmethod
    def ship(self, order: Order) -> str:
        pass

    @abstractmethod
    def deliver(self, order: Order) -> str:
        pass

    @abstractmethod
    def cancel(self, order: Order) -> str:
        pass

    @abstractmethod
    def status(self) -> str:
        pass


# -----------------------------------------------------------------------------
# Concrete States
# -----------------------------------------------------------------------------


class PendingState(OrderState):
    """Order has been created but not yet paid."""

    def pay(self, order: Order) -> str:
        order.set_state(PaidState())
        return "Payment received. Order is now paid."

    def ship(self, order: Order) -> str:
        return "Cannot ship: order is not paid yet."

    def deliver(self, order: Order) -> str:
        return "Cannot deliver: order has not been shipped."

    def cancel(self, order: Order) -> str:
        order.set_state(CancelledState())
        return "Order cancelled before payment."

    def status(self) -> str:
        return "Pending"


class PaidState(OrderState):
    """Order has been paid and is awaiting shipment."""

    def pay(self, order: Order) -> str:
        return "Order is already paid."

    def ship(self, order: Order) -> str:
        order.set_state(ShippedState())
        return "Order has been shipped."

    def deliver(self, order: Order) -> str:
        return "Cannot deliver: order has not been shipped yet."

    def cancel(self, order: Order) -> str:
        order.set_state(CancelledState())
        return "Order cancelled. Refund initiated."

    def status(self) -> str:
        return "Paid"


class ShippedState(OrderState):
    """Order has been shipped and is in transit."""

    def pay(self, order: Order) -> str:
        return "Order is already paid."

    def ship(self, order: Order) -> str:
        return "Order is already shipped."

    def deliver(self, order: Order) -> str:
        order.set_state(DeliveredState())
        return "Order delivered successfully."

    def cancel(self, order: Order) -> str:
        return "Cannot cancel: order is already in transit."

    def status(self) -> str:
        return "Shipped"


class DeliveredState(OrderState):
    """Order has been delivered to the customer."""

    def pay(self, order: Order) -> str:
        return "Order is already completed."

    def ship(self, order: Order) -> str:
        return "Order is already delivered."

    def deliver(self, order: Order) -> str:
        return "Order is already delivered."

    def cancel(self, order: Order) -> str:
        return "Cannot cancel a delivered order. Request a return instead."

    def status(self) -> str:
        return "Delivered"


class CancelledState(OrderState):
    """Order has been cancelled."""

    def pay(self, order: Order) -> str:
        return "Cannot pay: order has been cancelled."

    def ship(self, order: Order) -> str:
        return "Cannot ship: order has been cancelled."

    def deliver(self, order: Order) -> str:
        return "Cannot deliver: order has been cancelled."

    def cancel(self, order: Order) -> str:
        return "Order is already cancelled."

    def status(self) -> str:
        return "Cancelled"


# -----------------------------------------------------------------------------
# Context
# -----------------------------------------------------------------------------


class Order:
    """
    The Context maintains a reference to the current state and delegates
    all state-specific behavior to that state object.
    """

    def __init__(self, order_id: str):
        self.order_id = order_id
        self._state: OrderState = PendingState()

    def set_state(self, state: OrderState):
        self._state = state

    def pay(self) -> str:
        return self._state.pay(self)

    def ship(self) -> str:
        return self._state.ship(self)

    def deliver(self) -> str:
        return self._state.deliver(self)

    def cancel(self) -> str:
        return self._state.cancel(self)

    def status(self) -> str:
        return self._state.status()

    def __str__(self) -> str:
        return f"Order({self.order_id}) - [{self.status()}]"


# -----------------------------------------------------------------------------
# Additional Example: State Objects Returned by Behaviors
# -----------------------------------------------------------------------------


class TrafficLightState(ABC):
    """Each behavior returns the next state object instead of a string."""

    @abstractmethod
    def next(self) -> TrafficLightState:
        pass

    @abstractmethod
    def status(self) -> str:
        pass


class RedLightState(TrafficLightState):
    def next(self) -> TrafficLightState:
        return GreenLightState()

    def status(self) -> str:
        return "Red"


class GreenLightState(TrafficLightState):
    def next(self) -> TrafficLightState:
        return YellowLightState()

    def status(self) -> str:
        return "Green"


class YellowLightState(TrafficLightState):
    def next(self) -> TrafficLightState:
        return RedLightState()

    def status(self) -> str:
        return "Yellow"


class TrafficLight:
    def __init__(self):
        self._state: TrafficLightState = RedLightState()

    def advance(self) -> TrafficLightState:
        self._state = self._state.next()
        return self._state

    def status(self) -> str:
        return self._state.status()

    def __str__(self) -> str:
        return f"TrafficLight[{self.status()}]"


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    order = Order("ORD-1001")
    print(f"Created: {order}")

    # Normal lifecycle: pending -> paid -> shipped -> delivered
    print(order.pay())
    print(f"  -> {order}")
    print(order.ship())
    print(f"  -> {order}")
    print(order.deliver())
    print(f"  -> {order}")

    # Invalid transitions from delivered state
    print(order.cancel())  # cannot cancel delivered order
    print(order.pay())  # already completed

    print()

    # Cancellation flow
    order2 = Order("ORD-1002")
    print(f"Created: {order2}")
    print(order2.pay())
    print(f"  -> {order2}")
    print(order2.cancel())
    print(f"  -> {order2}")
    print(order2.ship())  # cannot ship cancelled order

    print()

    # Cancel before payment
    order3 = Order("ORD-1003")
    print(f"Created: {order3}")
    print(order3.cancel())
    print(f"  -> {order3}")

    print()

    # Enforce valid sequence: cannot ship before paying
    order4 = Order("ORD-1004")
    print(f"Created: {order4}")
    print(order4.ship())  # rejected
    print(order4.deliver())  # rejected
    print(order4.pay())  # now pay
    print(order4.ship())  # now it works
    print(f"  -> {order4}")

    print()

    # Example where each state returns the next state object
    light = TrafficLight()
    print(f"Created: {light}")
    for _ in range(5):
        next_state = light.advance()
        print(f"Advanced to: {next_state.status()} | Current: {light}")


if __name__ == "__main__":
    main()
