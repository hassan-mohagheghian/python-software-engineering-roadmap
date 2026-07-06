# Advanced Patterns - Unit of Work
# -------------------------------------------------------------------------
# The Unit of Work Pattern maintains a list of objects affected by a
# business transaction and coordinates the writing of changes and the
# resolution of concurrency problems.
#
# Instead of saving each object individually, the Unit of Work tracks
# what's new, what's changed, and what's deleted — then commits them
# all in one atomic operation.
#
# Benefits:
# - Atomic transactions — all changes succeed or all roll back
# - Reduces database round-trips by batching writes
# - Centralizes transaction management
# - Keeps domain logic clean of persistence concerns
#
# Real-world examples:
# - ORM change tracking (Django, SQLAlchemy, Hibernate)
# - E-commerce checkout (order + inventory + payment in one transaction)
# - Any multi-step operation that must be all-or-nothing
#
# Relationship to OOP Concepts:
#
# - Encapsulation:
#     The Unit of Work encapsulates which objects changed and how
#     to persist them.
#
# - Separation of Concerns:
#     Domain objects don't manage their own persistence. The Unit
#     of Work coordinates it.
#
# - Composition:
#     The Unit of Work holds collections of new, changed, and
#     deleted objects.
#
# Relationship to SOLID:
#
# - SRP:
#     The Unit of Work has one job: coordinate transactional persistence.
#
# - OCP:
#     New entity types can be registered without changing the
#     Unit of Work itself.
# -------------------------------------------------------------------------


from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List, Set


# =============================================================================
# Domain Models
# =============================================================================


class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"


class Order:
    def __init__(self, id: int, user_id: int, item: str, total: float):
        self.id = id
        self.user_id = user_id
        self.item = item
        self.total = total

    def __repr__(self):
        return f"Order(id={self.id}, item='{self.item}', total={self.total})"


# =============================================================================
# Repository Interfaces
# =============================================================================


class UserRepository(ABC):
    @abstractmethod
    def add(self, user: User):
        pass

    @abstractmethod
    def update(self, user: User):
        pass

    @abstractmethod
    def remove(self, user_id: int):
        pass


class OrderRepository(ABC):
    @abstractmethod
    def add(self, order: Order):
        pass

    @abstractmethod
    def update(self, order: Order):
        pass

    @abstractmethod
    def remove(self, order_id: int):
        pass


# =============================================================================
# In-Memory Repositories (simulating database)
# =============================================================================


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._store: Dict[int, User] = {}
        self._next_id = 1

    def add(self, user: User):
        user.id = self._next_id
        self._next_id += 1
        self._store[user.id] = user
        print(f"    [DB] INSERT user {user}")

    def update(self, user: User):
        self._store[user.id] = user
        print(f"    [DB] UPDATE user {user}")

    def remove(self, user_id: int):
        self._store.pop(user_id, None)
        print(f"    [DB] DELETE user id={user_id}")


class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self._store: Dict[int, Order] = {}
        self._next_id = 1

    def add(self, order: Order):
        order.id = self._next_id
        self._next_id += 1
        self._store[order.id] = order
        print(f"    [DB] INSERT order {order}")

    def update(self, order: Order):
        self._store[order.id] = order
        print(f"    [DB] UPDATE order {order}")

    def remove(self, order_id: int):
        self._store.pop(order_id, None)
        print(f"    [DB] DELETE order id={order_id}")


# =============================================================================
# Unit of Work
# =============================================================================


class UnitOfWork:
    """Tracks new, dirty, and deleted objects, then commits them atomically."""

    def __init__(
        self,
        users: UserRepository,
        orders: OrderRepository,
    ):
        self.users = users
        self.orders = orders
        self._new_users: Set[User] = set()
        self._dirty_users: Set[User] = set()
        self._deleted_users: Set[int] = set()
        self._new_orders: Set[Order] = set()
        self._dirty_orders: Set[Order] = set()
        self._deleted_orders: Set[int] = set()

    def register_new_user(self, user: User):
        self._new_users.add(user)

    def register_dirty_user(self, user: User):
        self._dirty_users.add(user)

    def register_deleted_user(self, user_id: int):
        self._deleted_users.add(user_id)

    def register_new_order(self, order: Order):
        self._new_orders.add(order)

    def register_dirty_order(self, order: Order):
        self._dirty_orders.add(order)

    def register_deleted_order(self, order_id: int):
        self._deleted_orders.add(order_id)

    def commit(self):
        print("  [UoW] Committing transaction...")
        for user in self._new_users:
            self.users.add(user)
        for user in self._dirty_users:
            self.users.update(user)
        for user_id in self._deleted_users:
            self.users.remove(user_id)
        for order in self._new_orders:
            self.orders.add(order)
        for order in self._dirty_orders:
            self.orders.update(order)
        for order_id in self._deleted_orders:
            self.orders.remove(order_id)
        self._clear()
        print("  [UoW] Transaction committed.")

    def rollback(self):
        print("  [UoW] Rolling back transaction...")
        self._clear()
        print("  [UoW] Transaction rolled back.")

    def _clear(self):
        self._new_users.clear()
        self._dirty_users.clear()
        self._deleted_users.clear()
        self._new_orders.clear()
        self._dirty_orders.clear()
        self._deleted_orders.clear()


# =============================================================================
# Usage
# =============================================================================


def main():
    user_repo = InMemoryUserRepository()
    order_repo = InMemoryOrderRepository()

    # --- Successful transaction ---
    print("=== Commit a transaction ===")
    uow = UnitOfWork(user_repo, order_repo)

    alice = User(0, "Alice", "alice@example.com")
    uow.register_new_user(alice)

    order = Order(0, alice.id, "Python Book", 29.99)
    uow.register_new_order(order)

    alice.email = "alice@newdomain.com"
    uow.register_dirty_user(alice)

    uow.commit()

    # --- Rolled-back transaction ---
    print("\n=== Rollback a transaction ===")
    uow2 = UnitOfWork(user_repo, order_repo)

    bob = User(0, "Bob", "bob@example.com")
    uow2.register_new_user(bob)

    bad_order = Order(0, bob.id, "Cancelled Item", 0.0)
    uow2.register_new_order(bad_order)

    uow2.rollback()
    print(f"  Bob was NOT persisted: {user_repo._store}")


if __name__ == "__main__":
    main()
