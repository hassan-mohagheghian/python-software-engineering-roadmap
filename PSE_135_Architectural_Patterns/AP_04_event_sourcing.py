# Architectural Patterns - Event Sourcing
# -------------------------------------------------------------------------
# Event Sourcing stores every change to application state as an immutable
# event. Instead of saving the current state, you save the sequence of
# events that led to it. The current state is rebuilt by replaying events.
#
# Benefits:
# - Full audit log — every change is recorded
# - Time travel — reconstruct state at any point in time
# - Debugging — replay events to find where things went wrong
# - Flexibility — add new projections/views without changing stored events
#
# Real-world examples:
# - Bank accounts (every debit/credit is an event)
# - Shopping carts (item added, item removed, order placed)
# - Collaborative editing (every keystroke is an event)
# - Event-driven microservices (Kafka, event stores)
#
# Relationship to OOP Concepts:
#
# - Immutability:
#     Events are immutable records. Once created, they never change.
#
# - Encapsulation:
#     The aggregate hides its internal state reconstruction behind
#     a clean interface.
#
# - Separation of Concerns:
#     Events capture "what happened." Projections determine "how to
#     present it."
#
# Relationship to SOLID:
#
# - SRP:
#     Each event type describes one thing that happened. Each
#     projection has one way to read the data.
#
# - OCP:
#     New projections can be added without modifying existing events
#     or event handlers.
# -------------------------------------------------------------------------


from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List

# =============================================================================
# Event Base
# =============================================================================


@dataclass(frozen=True)
class Event:
    """Immutable record of something that happened."""

    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


# =============================================================================
# Concrete Events
# =============================================================================


@dataclass(frozen=True)
class AccountOpened(Event):
    account_id: str = ""
    owner: str = ""
    initial_balance: float = 0.0


@dataclass(frozen=True)
class MoneyDeposited(Event):
    account_id: str = ""
    amount: float = 0.0


@dataclass(frozen=True)
class MoneyWithdrawn(Event):
    account_id: str = ""
    amount: float = 0.0


# =============================================================================
# Event Store
# =============================================================================


class EventStore:
    """Append-only log of events."""

    def __init__(self):
        self._events: List[Event] = []

    def append(self, event: Event):
        self._events.append(event)

    def get_events(self, account_id: str | None = None) -> List[Event]:
        if account_id is None:
            return list(self._events)
        return [e for e in self._events if getattr(e, "account_id", None) == account_id]

    def get_all_events(self) -> List[Event]:
        return list(self._events)


# =============================================================================
# Aggregate — rebuilds state from events
# =============================================================================


class BankAccount:
    """Rebuilds its state by replaying events."""

    def __init__(self):
        self.account_id = ""
        self.owner = ""
        self.balance = 0.0

    def apply(self, event: Event):
        if isinstance(event, AccountOpened):
            self.account_id = event.account_id
            self.owner = event.owner
            self.balance = event.initial_balance
        elif isinstance(event, MoneyDeposited):
            self.balance += event.amount
        elif isinstance(event, MoneyWithdrawn):
            self.balance -= event.amount

    @classmethod
    def from_events(cls, events: List[Event]) -> BankAccount:
        account = cls()
        for event in events:
            account.apply(event)
        return account

    def __repr__(self):
        return f"BankAccount(id='{self.account_id}', owner='{self.owner}', balance={self.balance:.2f})"


# =============================================================================
# Service — produces events
# =============================================================================


class BankService:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store

    def open_account(self, account_id: str, owner: str, initial: float = 0.0):
        event = AccountOpened(
            account_id=account_id, owner=owner, initial_balance=initial
        )
        self.event_store.append(event)

    def deposit(self, account_id: str, amount: float):
        event = MoneyDeposited(account_id=account_id, amount=amount)
        self.event_store.append(event)

    def withdraw(self, account_id: str, amount: float):
        event = MoneyWithdrawn(account_id=account_id, amount=amount)
        self.event_store.append(event)


# =============================================================================
# Projection — read model built from events
# =============================================================================


class BalanceProjection:
    """Builds a read model (account balances) by replaying events."""

    def __init__(self):
        self.balances: Dict[str, float] = {}

    def update(self, events: List[Event]):
        for event in events:
            if isinstance(event, AccountOpened):
                self.balances[event.account_id] = event.initial_balance
            elif isinstance(event, MoneyDeposited):
                self.balances[event.account_id] = (
                    self.balances.get(event.account_id, 0) + event.amount
                )
            elif isinstance(event, MoneyWithdrawn):
                self.balances[event.account_id] = (
                    self.balances.get(event.account_id, 0) - event.amount
                )


# =============================================================================
# Usage
# =============================================================================


def main():
    store = EventStore()
    bank = BankService(store)

    # Perform operations
    print("=== Performing operations ===")
    bank.open_account("ACC-001", "Alice", 1000.0)
    bank.deposit("ACC-001", 500.0)
    bank.withdraw("ACC-001", 200.0)
    bank.open_account("ACC-002", "Bob", 300.0)
    bank.deposit("ACC-002", 100.0)

    # Show all events
    print(f"\nTotal events stored: {len(store.get_all_events())}")
    for e in store.get_all_events():
        print(f"  {e}")

    # Rebuild Alice's account from events
    print("\n=== Rebuild Alice's account ===")
    alice_events = store.get_events("ACC-001")
    alice_account = BankAccount.from_events(alice_events)
    print(f"  {alice_account}")

    # Rebuild Bob's account from events
    print("\n=== Rebuild Bob's account ===")
    bob_events = store.get_events("ACC-002")
    bob_account = BankAccount.from_events(bob_events)
    print(f"  {bob_account}")

    # Build balance projection
    print("\n=== Balance Projection ===")
    projection = BalanceProjection()
    projection.update(store.get_all_events())
    for acc_id, balance in projection.balances.items():
        print(f"  {acc_id}: ${balance:.2f}")


if __name__ == "__main__":
    main()
