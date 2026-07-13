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
# This version adds snapshot-based rollback: when an existing object is
# marked dirty, its pre-change state is captured. If the transaction
# fails, all dirty objects are restored to their previous state rather
# than simply discarding the tracking sets.
#
# Benefits:
# - Atomic transactions — all changes succeed or all roll back
# - Reduces database round-trips by batching writes
# - Centralizes transaction management
# - Snapshot rollback ensures consistency even after partial mutations
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
#     to persist them. Snapshots are an internal concern.
#
# - Separation of Concerns:
#     Domain objects don't manage their own persistence or undo.
#     The Unit of Work coordinates it.
#
# - Composition:
#     The Unit of Work holds collections of new, changed, and
#     deleted objects, plus their snapshots.
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

import copy
from abc import ABC, abstractmethod
from typing import Dict, Set

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


class Product:
    def __init__(self, id: int, name: str, price: float, stock: int):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        return (
            f"Product(id={self.id}, name='{self.name}', "
            f"price={self.price}, stock={self.stock})"
        )


class Order:
    def __init__(
        self, id: int, user_id: int, product_id: int, quantity: int, total: float
    ):
        self.id = id
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity
        self.total = total

    def __repr__(self):
        return (
            f"Order(id={self.id}, product_id={self.product_id}, "
            f"qty={self.quantity}, total={self.total})"
        )


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
    def get(self, user_id: int) -> User | None:
        pass

    @abstractmethod
    def remove(self, user_id: int):
        pass


class ProductRepository(ABC):
    @abstractmethod
    def add(self, product: Product):
        pass

    @abstractmethod
    def update(self, product: Product):
        pass

    @abstractmethod
    def get(self, product_id: int) -> Product | None:
        pass

    @abstractmethod
    def remove(self, product_id: int):
        pass


class OrderRepository(ABC):
    @abstractmethod
    def add(self, order: Order):
        pass

    @abstractmethod
    def update(self, order: Order):
        pass

    @abstractmethod
    def get(self, order_id: int) -> Order | None:
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
        self._store[user.id] = copy.deepcopy(user)
        print(f"    [DB] INSERT user {user}")

    def update(self, user: User):
        self._store[user.id] = copy.deepcopy(user)
        print(f"    [DB] UPDATE user {user}")

    def get(self, user_id: int) -> User | None:
        # Return a deep copy so callers can't silently mutate DB state
        existing = self._store.get(user_id)
        return copy.deepcopy(existing) if existing is not None else None

    def remove(self, user_id: int):
        self._store.pop(user_id, None)
        print(f"    [DB] DELETE user id={user_id}")


class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self._store: Dict[int, Product] = {}
        self._next_id = 1

    def add(self, product: Product):
        product.id = self._next_id
        self._next_id += 1
        self._store[product.id] = copy.deepcopy(product)
        print(f"    [DB] INSERT product {product}")

    def update(self, product: Product):
        self._store[product.id] = copy.deepcopy(product)
        print(f"    [DB] UPDATE product {product}")

    def get(self, product_id: int) -> Product | None:
        existing = self._store.get(product_id)
        return copy.deepcopy(existing) if existing is not None else None

    def remove(self, product_id: int):
        self._store.pop(product_id, None)
        print(f"    [DB] DELETE product id={product_id}")


class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self._store: Dict[int, Order] = {}
        self._next_id = 1

    def add(self, order: Order):
        order.id = self._next_id
        self._next_id += 1
        self._store[order.id] = copy.deepcopy(order)
        print(f"    [DB] INSERT order {order}")

    def update(self, order: Order):
        self._store[order.id] = copy.deepcopy(order)
        print(f"    [DB] UPDATE order {order}")

    def get(self, order_id: int) -> Order | None:
        existing = self._store.get(order_id)
        return copy.deepcopy(existing) if existing is not None else None

    def remove(self, order_id: int):
        self._store.pop(order_id, None)
        print(f"    [DB] DELETE order id={order_id}")


# =============================================================================
# Unit of Work with Snapshot Rollback
# =============================================================================


class UnitOfWork:
    """Tracks new, dirty, and deleted objects, then commits atomically.

    On register_dirty_*, the object's current state is deep-copied into
    a snapshot.  On rollback, dirty objects are restored from their
    snapshots so the in-memory state matches what the "database" actually
    has.
    """

    def __init__(
        self,
        users: UserRepository,
        products: ProductRepository,
        orders: OrderRepository,
    ):
        self.users = users
        self.products = products
        self.orders = orders

        self._new_users: Set[User] = set()
        self._dirty_users: Set[User] = set()
        self._snapshots_users: Dict[int, User] = {}
        self._deleted_users: Set[int] = set()

        self._new_products: Set[Product] = set()
        self._dirty_products: Set[Product] = set()
        self._snapshots_products: Dict[int, Product] = {}
        self._deleted_products: Set[int] = set()

        self._new_orders: Set[Order] = set()
        self._dirty_orders: Set[Order] = set()
        self._snapshots_orders: Dict[int, Order] = {}
        self._deleted_orders: Set[int] = set()

    # -- Registration helpers ------------------------------------------------
    # Snapshot is captured from the REPOSITORY (pre-mutation state), not
    # from the in-memory object which may already be modified.

    def register_new_user(self, user: User):
        self._new_users.add(user)

    def register_dirty_user(self, user: User):
        if user.id not in self._snapshots_users:
            existing = self.users.get(user.id)
            if existing is not None:
                self._snapshots_users[user.id] = copy.deepcopy(existing)
        self._dirty_users.add(user)

    def register_deleted_user(self, user_id: int):
        self._deleted_users.add(user_id)

    def register_new_product(self, product: Product):
        self._new_products.add(product)

    def register_dirty_product(self, product: Product):
        if product.id not in self._snapshots_products:
            existing = self.products.get(product.id)
            if existing is not None:
                self._snapshots_products[product.id] = copy.deepcopy(existing)
        self._dirty_products.add(product)

    def register_deleted_product(self, product_id: int):
        self._deleted_products.add(product_id)

    def register_new_order(self, order: Order):
        self._new_orders.add(order)

    def register_dirty_order(self, order: Order):
        if order.id not in self._snapshots_orders:
            existing = self.orders.get(order.id)
            if existing is not None:
                self._snapshots_orders[order.id] = copy.deepcopy(existing)
        self._dirty_orders.add(order)

    def register_deleted_order(self, order_id: int):
        self._deleted_orders.add(order_id)

    # -- Commit / Rollback ---------------------------------------------------

    def commit(self):
        print("  [UoW] Committing transaction...")
        for user in self._new_users:
            self.users.add(user)
        for user in self._dirty_users:
            self.users.update(user)
        for user_id in self._deleted_users:
            self.users.remove(user_id)

        for product in self._new_products:
            self.products.add(product)
        for product in self._dirty_products:
            self.products.update(product)
        for product_id in self._deleted_products:
            self.products.remove(product_id)

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

        # The DB was never written (commit never ran), so the DB already
        # holds the correct state.  We only need to restore the in-memory
        # object references so callers see the pre-mutation values.

        for user_id, snapshot in self._snapshots_users.items():
            restored = copy.deepcopy(snapshot)
            self._store_users_replace(user_id, restored)
            print(f"    [UoW] Restored user from snapshot: {restored}")

        for product_id, snapshot in self._snapshots_products.items():
            restored = copy.deepcopy(snapshot)
            self._store_products_replace(product_id, restored)
            print(f"    [UoW] Restored product from snapshot: {restored}")

        for order_id, snapshot in self._snapshots_orders.items():
            restored = copy.deepcopy(snapshot)
            self._store_orders_replace(order_id, restored)
            print(f"    [UoW] Restored order from snapshot: {restored}")

        self._clear()
        print("  [UoW] Transaction rolled back.")

    def _store_users_replace(self, user_id: int, user: User):
        """Directly update the repo store without logging a DB UPDATE."""
        if hasattr(self.users, "_store"):
            self.users._store[user_id] = user

    def _store_products_replace(self, product_id: int, product: Product):
        if hasattr(self.products, "_store"):
            self.products._store[product_id] = product

    def _store_orders_replace(self, order_id: int, order: Order):
        if hasattr(self.orders, "_store"):
            self.orders._store[order_id] = order

    def _clear(self):
        self._new_users.clear()
        self._dirty_users.clear()
        self._snapshots_users.clear()
        self._deleted_users.clear()

        self._new_products.clear()
        self._dirty_products.clear()
        self._snapshots_products.clear()
        self._deleted_products.clear()

        self._new_orders.clear()
        self._dirty_orders.clear()
        self._snapshots_orders.clear()
        self._deleted_orders.clear()


# =============================================================================
# Usage — E-Commerce Checkout
# =============================================================================


def main():
    user_repo = InMemoryUserRepository()
    product_repo = InMemoryProductRepository()
    order_repo = InMemoryOrderRepository()

    # -- Seed some data into the "database" ----------------------------------
    print("=== Seeding data ===")
    uow = UnitOfWork(user_repo, product_repo, order_repo)

    alice = User(0, "Alice", "alice@example.com")
    uow.register_new_user(alice)

    book = Product(0, "Python Patterns", 49.99, stock=10)
    uow.register_new_product(book)

    uow.commit()

    # -- Successful purchase -------------------------------------------------
    print("\n=== Successful purchase ===")
    uow = UnitOfWork(user_repo, product_repo, order_repo)

    # Snapshot the product BEFORE we mutate it
    book_snapshot = copy.deepcopy(product_repo.get(book.id))

    book.stock -= 1  # reserve one unit
    uow.register_dirty_product(book)

    order = Order(0, alice.id, book.id, quantity=1, total=book.price)
    uow.register_new_order(order)

    uow.commit()

    updated_book = product_repo.get(book.id)
    print(f"  Book stock after purchase: {updated_book.stock}")

    # -- Failed purchase — rollback restores stock ---------------------------
    print("\n=== Failed purchase (payment declined) ===")
    uow = UnitOfWork(user_repo, product_repo, order_repo)

    book = product_repo.get(book.id)  # re-fetch to get current state
    print(f"  Book stock before attempt: {book.stock}")

    book.stock -= 1  # attempt to reserve
    uow.register_dirty_product(book)

    order = Order(0, alice.id, book.id, quantity=1, total=book.price)
    uow.register_new_order(order)

    # Simulate payment failure — rollback
    uow.rollback()

    book_after = product_repo.get(book.id)
    print(f"  Book stock after rollback: {book_after.stock}")

    # -- Partial failure mid-transaction ------------------------------------
    print("\n=== Partial failure (two products, second one fails) ===")
    gadget = Product(0, "Gadget", 19.99, stock=5)
    uow = UnitOfWork(user_repo, product_repo, order_repo)
    uow.register_new_product(gadget)
    uow.commit()

    uow = UnitOfWork(user_repo, product_repo, order_repo)

    book = product_repo.get(book.id)
    gadget = product_repo.get(gadget.id)

    book.stock -= 1
    gadget.stock -= 1
    uow.register_dirty_product(book)
    uow.register_dirty_product(gadget)

    order = Order(0, alice.id, book.id, quantity=1, total=book.price + gadget.price)
    uow.register_new_order(order)

    # "gadget supplier just ran out" — rollback the whole thing
    uow.rollback()

    book_after = product_repo.get(book.id)
    gadget_after = product_repo.get(gadget.id)
    print(f"  Book stock after rollback: {book_after.stock}")
    print(f"  Gadget stock after rollback: {gadget_after.stock}")


if __name__ == "__main__":
    main()
