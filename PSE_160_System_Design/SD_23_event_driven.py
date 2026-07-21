# System Design - Event-Driven Architecture
# -----------------------------------------------------------------------------
# Event-Driven Architecture (EDA) is a design pattern where components
# communicate by producing and consuming events rather than making
# direct synchronous calls.
#
# Traditional (Request/Response):
#
#   Service A → HTTP call → Service B → HTTP call → Service C
#   (tightly coupled, synchronous, blocking)
#
# Event-Driven:
#
#   Service A → publishes Event → Event Bus → Service B (subscribes)
#                                           → Service C (subscribes)
#   (decoupled, asynchronous, non-blocking)
#
# -----------------------------------------------------------------------------
# Core Concepts:
#
# 1. Event
#    - An immutable record of something that happened
#    - Contains: event type, timestamp, payload, metadata
#    - Examples: OrderPlaced, PaymentProcessed, ItemShipped
#
# 2. Event Producer
#    - Creates and publishes events
#    - Doesn't know or care who consumes them
#
# 3. Event Bus / Broker
#    - Routes events from producers to consumers
#    - Examples: Kafka, RabbitMQ, AWS SNS/SQS, Redis Streams
#
# 4. Event Consumer
#    - Subscribes to events and reacts
#    - Can process independently, at its own pace
#
# -----------------------------------------------------------------------------
# Two Major Patterns:
#
# 1. Event Notification
#    - Events trigger reactions in consumers
#    - Consumers maintain their own state
#    - Simple, but consumers may miss events
#
# 2. Event Sourcing
#    - Events ARE the source of truth (append-only log)
#    - State is derived by replaying events
#    - Full audit trail, time-travel, but more complex
#
# -----------------------------------------------------------------------------
# CQRS (Command Query Responsibility Segregation):
#
#   Separates write model (commands) from read model (queries):
#
#   Command → Event Store → Read Model → Query
#     │                          ▲
#     └── Event Bus ────────────┘
#
#   Write side: validates commands, produces events
#   Read side: builds optimized views from events
#   Benefits: independent scaling, optimized read/write models
#
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - Apache Kafka (event streaming platform)
# - Event sourcing in DDD (Domain-Driven Design)
# - CQRS in .NET / Java applications
# - AWS EventBridge, Google Pub/Sub
# - Netflix event-driven microservices
# -----------------------------------------------------------------------------


import time
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

# =============================================================================
# Event
# =============================================================================


@dataclass
class Event:
    event_type: str
    payload: Dict[str, Any]
    timestamp: float = field(default_factory=time.time)
    event_id: str = ""
    version: int = 1

    def __post_init__(self):
        if not self.event_id:
            self.event_id = f"evt_{int(self.timestamp * 1000)}"

    def __repr__(self) -> str:
        return f"Event({self.event_type}, {self.payload})"


# =============================================================================
# Event Store (Event Sourcing)
# =============================================================================


class EventStore:
    """
    Append-only log of events. Events ARE the source of truth.
    State is rebuilt by replaying events from the store.
    """

    def __init__(self):
        self._events: List[Event] = []

    def append(self, event: Event):
        self._events.append(event)
        print(f"    [EventStore] Appended: {event.event_type}")

    def get_events(self, event_type: Optional[str] = None) -> List[Event]:
        if event_type:
            return [e for e in self._events if e.event_type == event_type]
        return list(self._events)

    def get_all(self) -> List[Event]:
        return list(self._events)

    @property
    def size(self) -> int:
        return len(self._events)


# =============================================================================
# Event Bus
# =============================================================================


class EventBus:
    """
    Routes events from producers to subscribers.
    In production: Kafka, RabbitMQ, Redis Pub/Sub, AWS SNS.
    """

    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = {}
        self.event_log: List[str] = []

    def subscribe(self, event_type: str, handler: Callable):
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(handler)
        print(f"    [EventBus] Subscribed to '{event_type}'")

    def publish(self, event: Event):
        self.event_log.append(f"{event.event_type}: {event.payload}")
        handlers = self._subscribers.get(event.event_type, [])
        wildcard_handlers = self._subscribers.get("*", [])

        for handler in handlers + wildcard_handlers:
            handler(event)


# =============================================================================
# Event-Sourced Aggregate (Order)
# =============================================================================


class OrderAggregate:
    """
    An aggregate that uses event sourcing — all state changes
    are captured as events and the state is rebuilt from them.
    """

    def __init__(self, order_id: str, event_store: EventStore):
        self.order_id = order_id
        self.event_store = event_store
        # Rebuild state from events
        self.status = "pending"
        self.items: List[Dict[str, Any]] = []
        self.total = 0.0
        self._rebuild()

    def _rebuild(self):
        """Replay all events for this order to rebuild current state."""
        events = self.event_store.get_events()
        for event in events:
            if event.payload.get("order_id") != self.order_id:
                continue
            self._apply(event, save=False)

    def _apply(self, event: Event, save: bool = True):
        """Apply an event to update state."""
        if event.event_type == "OrderCreated":
            self.status = "created"
        elif event.event_type == "ItemAdded":
            item = event.payload.get("item", {})
            self.items.append(item)
            self.total += item.get("price", 0) * item.get("quantity", 1)
        elif event.event_type == "OrderPaid":
            self.status = "paid"
        elif event.event_type == "OrderShipped":
            self.status = "shipped"

        if save:
            self.event_store.append(event)

    def add_item(self, name: str, price: float, quantity: int = 1):
        event = Event(
            event_type="ItemAdded",
            payload={
                "order_id": self.order_id,
                "item": {"name": name, "price": price, "quantity": quantity},
            },
        )
        self._apply(event)

    def pay(self):
        event = Event(
            event_type="OrderPaid",
            payload={"order_id": self.order_id, "total": self.total},
        )
        self._apply(event)

    def ship(self):
        event = Event(
            event_type="OrderShipped",
            payload={"order_id": self.order_id},
        )
        self._apply(event)

    def get_state(self) -> Dict[str, Any]:
        return {
            "order_id": self.order_id,
            "status": self.status,
            "items": self.items,
            "total": self.total,
        }


# =============================================================================
# CQRS: Command Side
# =============================================================================


class CommandHandler:
    """
    Handles commands (write operations). Validates and produces events.
    """

    def __init__(self, event_store: EventStore, event_bus: EventBus):
        self.event_store = event_store
        self.event_bus = event_bus
        self._orders: Dict[str, OrderAggregate] = {}

    def create_order(self, order_id: str) -> OrderAggregate:
        event = Event(
            event_type="OrderCreated",
            payload={"order_id": order_id},
        )
        self.event_store.append(event)
        order = OrderAggregate(order_id, self.event_store)
        self._orders[order_id] = order
        self.event_bus.publish(event)
        return order

    def add_item_to_order(
        self, order_id: str, name: str, price: float, quantity: int = 1
    ):
        order = self._orders.get(order_id)
        if order:
            order.add_item(name, price, quantity)
            # Publish the latest event
            events = self.event_store.get_events("ItemAdded")
            if events:
                self.event_bus.publish(events[-1])

    def pay_order(self, order_id: str):
        order = self._orders.get(order_id)
        if order:
            order.pay()
            events = self.event_store.get_events("OrderPaid")
            if events:
                self.event_bus.publish(events[-1])

    def ship_order(self, order_id: str):
        order = self._orders.get(order_id)
        if order:
            order.ship()
            events = self.event_store.get_events("OrderShipped")
            if events:
                self.event_bus.publish(events[-1])

    def get_order(self, order_id: str) -> Optional[OrderAggregate]:
        return self._orders.get(order_id)


# =============================================================================
# CQRS: Query Side (Read Model)
# =============================================================================


class QueryHandler:
    """
    Handles queries (read operations). Maintains a read-optimized view
    built from events.
    """

    def __init__(self, event_store: EventStore):
        self.event_store = event_store
        self._order_views: Dict[str, Dict[str, Any]] = {}
        self._rebuild()

    def _rebuild(self):
        """Build read model from all events."""
        for event in self.event_store.get_all():
            self._process_event(event)

    def _process_event(self, event: Event):
        oid = event.payload.get("order_id")
        if not oid:
            return

        if oid not in self._order_views:
            self._order_views[oid] = {
                "order_id": oid,
                "status": "pending",
                "items": [],
                "total": 0,
            }

        view = self._order_views[oid]

        if event.event_type == "OrderCreated":
            view["status"] = "created"
        elif event.event_type == "ItemAdded":
            item = event.payload.get("item", {})
            view["items"].append(item)
            view["total"] += item.get("price", 0) * item.get("quantity", 1)
        elif event.event_type == "OrderPaid":
            view["status"] = "paid"
        elif event.event_type == "OrderShipped":
            view["status"] = "shipped"

    def get_order_view(self, order_id: str) -> Optional[Dict[str, Any]]:
        return self._order_views.get(order_id)

    def get_all_orders(self) -> List[Dict[str, Any]]:
        return list(self._order_views.values())


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=" * 65)
    print("EVENT-DRIVEN ARCHITECTURE — Events, Sourcing, CQRS")
    print("=" * 65)

    event_store = EventStore()
    event_bus = EventBus()

    # --- 1. Event Notification ---
    print("\n" + "-" * 65)
    print("1. EVENT NOTIFICATION")
    print("   Services communicate through events")
    print("-" * 65)

    def order_placed_handler(event: Event):
        print(f"    [EmailService] Sending confirmation for {event.payload}")

    def order_placed_analytics(event: Event):
        print(f"    [Analytics] Tracking order: {event.payload}")

    event_bus.subscribe("OrderCreated", order_placed_handler)
    event_bus.subscribe("OrderCreated", order_placed_analytics)

    print("\n  Publishing OrderCreated event:")
    event_bus.publish(Event(event_type="OrderCreated", payload={"order_id": "ORD-001"}))

    # --- 2. Event Sourcing ---
    print("\n" + "-" * 65)
    print("2. EVENT SOURCING")
    print("   Events are the source of truth — state is rebuilt from them")
    print("-" * 65)

    print("\n  Creating order and adding items:")
    command = CommandHandler(event_store, event_bus)

    order = command.create_order("ORD-002")
    command.add_item_to_order("ORD-002", "Laptop", 999.99, 1)
    command.add_item_to_order("ORD-002", "Mouse", 29.99, 2)
    command.pay_order("ORD-002")
    command.ship_order("ORD-002")

    print(f"\n  Order state (rebuilt from {event_store.size} events):")
    state = order.get_state()
    for key, value in state.items():
        print(f"    {key}: {value}")

    print(f"\n  Full event log:")
    for i, event in enumerate(event_store.get_all(), 1):
        print(f"    {i}. {event.event_type}: {event.payload}")

    # --- 3. CQRS ---
    print("\n" + "-" * 65)
    print("3. CQRS — Separate Read and Write Models")
    print("   Write side produces events, Read side builds views")
    print("-" * 65)

    query = QueryHandler(event_store)

    print("\n  Creating another order:")
    command.create_order("ORD-003")
    command.add_item_to_order("ORD-003", "Keyboard", 79.99, 1)
    command.pay_order("ORD-003")

    print("\n  Query: All orders (read-optimized view):")
    for view in query.get_all_orders():
        print(
            f"    {view['order_id']}: status={view['status']}, "
            f"items={len(view['items'])}, total=${view['total']:.2f}"
        )

    print("\n  Query: Single order detail:")
    detail = query.get_order_view("ORD-002")
    if detail:
        print(f"    Order: {detail['order_id']}")
        print(f"    Status: {detail['status']}")
        print(f"    Items: {detail['items']}")
        print(f"    Total: ${detail['total']:.2f}")

    # --- 4. Rebuild from Events ---
    print("\n" + "-" * 65)
    print("4. REBUILD FROM EVENTS")
    print("   If the read model is lost, rebuild from the event store")
    print("-" * 65)

    new_query = QueryHandler(event_store)
    print(f"\n  Rebuilt query model from {event_store.size} events:")
    for view in new_query.get_all_orders():
        print(f"    {view['order_id']}: {view['status']} (${view['total']:.2f})")

    # --- Summary ---
    print("\n" + "=" * 65)
    print("SUMMARY — Event-Driven Architecture")
    print("=" * 65)
    print("""
  Pattern        What it does                    When to use
  -------        ------------                    -----------
  Event          Services react to events        Decoupling, async workflows
  Notification   without direct coupling

  Event          Events are source of truth;     Audit trail, time-travel,
  Sourcing       state rebuilt by replay          complex domain logic

  CQRS           Separate read/write models      Heavy reads, complex queries,
                 for independent scaling          eventual consistency OK

  Pros:
  + Loose coupling between services
  + Async — no blocking, better throughput
  + Full audit trail (event sourcing)
  + Easy to add new consumers without changing producers
  + Time-travel debugging (replay events)

  Cons:
  - Eventual consistency (not immediate)
  - Complexity of event ordering and idempotency
  - Event schema evolution is challenging
  - Debugging async flows is harder

  Real-world: Kafka, EventStoreDB, Axon Framework, DDD aggregates
""")


if __name__ == "__main__":
    main()
