# Advanced Patterns - CQRS (Command Query Responsibility Segregation)
# -------------------------------------------------------------------------
# CQRS splits a system into two separate models:
#
#   Command side  — handles writes (create, update, delete)
#   Query side    — handles reads (fetch, list, search)
#
# Instead of one model doing everything, each side is optimized for its
# job. Commands mutate state; queries return data without side effects.
#
# Why separate them?
#
# - Writes and reads have different performance needs
#   (writes need consistency, reads need speed)
# - Scaling reads is cheaper than scaling writes
# - Read models can be denormalized for fast lookups
# - Write models stay clean and focused on business rules
#
# Benefits:
# - Independent scaling of reads and writes
# - Optimized data models for each side
# - Clear separation of concerns
# - Pairs naturally with Event Sourcing
#
# Real-world examples:
# - E-commerce: write orders, query product catalogs
# - Social media: write posts, read timelines
# - Banking: execute transfers, query balances
# - Any system where read patterns differ from write patterns
#
# Relationship to OOP Concepts:
#
# - Encapsulation:
#     Command and query models are encapsulated separately,
#     each with its own interface.
#
# - Separation of Concerns:
#     Write logic never pollutes read logic and vice versa.
#
# - Polymorphism:
#     Different read models can serve the same data in
#     different shapes (list view, detail view, search view).
#
# Relationship to SOLID:
#
# - SRP:
#     Command handler has one job: process a command.
#     Query handler has one job: return data.
#
# - OCP:
#     New read models can be added without touching the write side.
#
# - DIP:
#     Both sides depend on abstractions (interfaces), not
#     concrete storage implementations.
# -------------------------------------------------------------------------


from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List

# =============================================================================
# Commands (Write Side)
# =============================================================================


class Command:
    pass


@dataclass
class CreateProduct(Command):
    product_id: str = ""
    name: str = ""
    price: float = 0.0
    category: str = ""


@dataclass
class UpdatePrice(Command):
    product_id: str = ""
    new_price: float = 0.0


@dataclass
class ArchiveProduct(Command):
    product_id: str = ""


# =============================================================================
# Queries (Read Side)
# =============================================================================


class Query:
    pass


@dataclass
class GetProductById(Query):
    product_id: str = ""


@dataclass
class ListProductsByCategory(Query):
    category: str = ""


@dataclass
class SearchProducts(Query):
    keyword: str = ""


# =============================================================================
# Write Model — the source of truth
# =============================================================================


@dataclass
class Product:
    product_id: str
    name: str
    price: float
    category: str
    archived: bool = False
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())


class ProductWriteStore:
    """Write-optimized store. Holds authoritative product state."""

    def __init__(self):
        self._products: Dict[str, Product] = {}

    def save(self, product: Product):
        self._products[product.product_id] = product
        print(f"    [WriteDB] Saved product '{product.name}' (id={product.product_id})")

    def get(self, product_id: str) -> Product | None:
        return self._products.get(product_id)

    def exists(self, product_id: str) -> bool:
        return product_id in self._products


# =============================================================================
# Read Models — optimized for specific query patterns
# =============================================================================


@dataclass
class ProductSummary:
    product_id: str
    name: str
    price: float
    category: str


class ProductReadStore:
    """Read-optimized store. Denormalized views for fast queries."""

    def __init__(self):
        self._by_id: Dict[str, ProductSummary] = {}
        self._by_category: Dict[str, List[ProductSummary]] = {}
        self._all: List[ProductSummary] = []

    def add(self, product: Product):
        summary = ProductSummary(
            product_id=product.product_id,
            name=product.name,
            price=product.price,
            category=product.category,
        )
        self._by_id[product.product_id] = summary
        self._by_category.setdefault(product.category, []).append(summary)
        self._all.append(summary)
        print(f"    [ReadDB] Indexed product '{product.name}' for queries")

    def update(self, product: Product):
        if product.product_id in self._by_id:
            summary = self._by_id[product.product_id]
            summary.price = product.price
            summary.name = product.name
            print(f"    [ReadDB] Updated read model for '{product.name}'")

    def remove(self, product_id: str):
        summary = self._by_id.pop(product_id, None)
        if summary:
            self._all = [s for s in self._all if s.product_id != product_id]
            cat_list = self._by_category.get(summary.category, [])
            self._by_category[summary.category] = [
                s for s in cat_list if s.product_id != product_id
            ]
            print(f"    [ReadDB] Removed '{summary.name}' from read models")

    def find_by_id(self, product_id: str) -> ProductSummary | None:
        return self._by_id.get(product_id)

    def find_by_category(self, category: str) -> List[ProductSummary]:
        return self._by_category.get(category, [])

    def search(self, keyword: str) -> List[ProductSummary]:
        kw = keyword.lower()
        return [
            s for s in self._all if kw in s.name.lower() or kw in s.category.lower()
        ]

    def list_all(self) -> List[ProductSummary]:
        return list(self._all)


# =============================================================================
# Command Handlers (Write Side)
# =============================================================================


class CommandHandler:
    def __init__(self, write_store: ProductWriteStore, read_store: ProductReadStore):
        self.write_store = write_store
        self.read_store = read_store

    def handle(self, command: Command):
        if isinstance(command, CreateProduct):
            self._create_product(command)
        elif isinstance(command, UpdatePrice):
            self._update_price(command)
        elif isinstance(command, ArchiveProduct):
            self._archive_product(command)
        else:
            raise ValueError(f"Unknown command: {type(command).__name__}")

    def _create_product(self, cmd: CreateProduct):
        if self.write_store.exists(cmd.product_id):
            print(f"  [Command] Error: product {cmd.product_id} already exists")
            return
        product = Product(
            product_id=cmd.product_id,
            name=cmd.name,
            price=cmd.price,
            category=cmd.category,
        )
        self.write_store.save(product)
        # Sync to read side
        self.read_store.add(product)

    def _update_price(self, cmd: UpdatePrice):
        product = self.write_store.get(cmd.product_id)
        if not product:
            print(f"  [Command] Error: product {cmd.product_id} not found")
            return
        product.price = cmd.new_price
        self.write_store.save(product)
        self.read_store.update(product)

    def _archive_product(self, cmd: ArchiveProduct):
        product = self.write_store.get(cmd.product_id)
        if not product:
            print(f"  [Command] Error: product {cmd.product_id} not found")
            return
        product.archived = True
        self.write_store.save(product)
        self.read_store.remove(cmd.product_id)


# =============================================================================
# Query Handlers (Read Side)
# =============================================================================


class QueryHandler:
    def __init__(self, read_store: ProductReadStore):
        self.read_store = read_store

    def handle(self, query: Query) -> Any:
        if isinstance(query, GetProductById):
            return self.read_store.find_by_id(query.product_id)
        elif isinstance(query, ListProductsByCategory):
            return self.read_store.find_by_category(query.category)
        elif isinstance(query, SearchProducts):
            return self.read_store.search(query.keyword)
        else:
            raise ValueError(f"Unknown query: {type(query).__name__}")


# =============================================================================
# Facade — ties command and query sides together
# =============================================================================


class ProductCQRS:
    """Public API — callers send commands or queries through this."""

    def __init__(self):
        self._write_store = ProductWriteStore()
        self._read_store = ProductReadStore()
        self._command_handler = CommandHandler(self._write_store, self._read_store)
        self._query_handler = QueryHandler(self._read_store)

    def execute(self, command: Command):
        self._command_handler.handle(command)

    def query(self, query: Query) -> Any:
        return self._query_handler.handle(query)


# =============================================================================
# Usage
# =============================================================================


def main():
    cqrs = ProductCQRS()

    # --- Commands (Write Side) ---
    print("=== Creating products ===")
    cqrs.execute(CreateProduct("P001", "Mechanical Keyboard", 149.99, "electronics"))
    cqrs.execute(CreateProduct("P002", "Ergonomic Mouse", 79.99, "electronics"))
    cqrs.execute(CreateProduct("P003", "Standing Desk", 499.99, "furniture"))
    cqrs.execute(CreateProduct("P004", "USB-C Hub", 39.99, "electronics"))

    print("\n=== Updating prices ===")
    cqrs.execute(UpdatePrice("P002", 69.99))

    print("\n=== Archiving a product ===")
    cqrs.execute(ArchiveProduct("P004"))

    # --- Queries (Read Side) ---
    print("\n=== Query: Get product by ID ===")
    product = cqrs.query(GetProductById("P001"))
    print(f"  {product}")

    print("\n=== Query: List by category ===")
    electronics = cqrs.query(ListProductsByCategory("electronics"))
    for p in electronics:
        print(f"  {p.name} — ${p.price}")

    print("\n=== Query: Search ===")
    results = cqrs.query(SearchProducts("desk"))
    for p in results:
        print(f"  Found: {p.name} (${p.price})")

    print("\n=== Query: List all ===")
    all_products = cqrs.query(ListProductsByCategory("electronics"))
    furniture = cqrs.query(ListProductsByCategory("furniture"))
    print(f"  Electronics: {[p.name for p in all_products]}")
    print(f"  Furniture: {[p.name for p in furniture]}")


if __name__ == "__main__":
    main()
