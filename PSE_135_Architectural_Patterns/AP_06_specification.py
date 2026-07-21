# Advanced Patterns - Specification Pattern
# -----------------------------------------------------------------------------
# The Specification Pattern is a design pattern that encapsulates business
# rules into distinct, reusable objects. These objects define query or validation
# criteria that can be combined using boolean operations (AND, OR, NOT).
#
# By representing rules as specifications, we keep domain entities free of
# validation/filtering logic and gain the ability to chain criteria dynamically.
#
# Benefits:
# - Highly reusable: Combine small, simple rules to construct complex rules.
# - Promotes SRP (Single Responsibility Principle) by separating logic check
#   from entities.
# - Easily testable rules in isolation.
#
# Real-world examples:
# - E-commerce shopping cart coupon eligibility (e.g. Total > $100 AND customer is Premium)
# - Loan qualification engines (e.g. Credit score > 700 AND salary > $50k)
# - Search/filter UI criteria construction
#
# Relationship to SOLID:
# - Single Responsibility Principle (SRP): Each specification checks one rule.
# - Open/Closed Principle (OCP): New business rules can be added by creating
#   new specifications without modifying existing logic.
# -----------------------------------------------------------------------------

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar

# =============================================================================
# Entities
# =============================================================================


@dataclass
class Product:
    name: str
    price: float
    stock_count: int
    category: str


@dataclass
class Customer:
    name: str
    is_premium: bool
    total_orders_count: int


# =============================================================================
# Specification Base class
# =============================================================================

T = TypeVar("T")


class Specification(ABC, Generic[T]):
    @abstractmethod
    def is_satisfied_by(self, candidate: T) -> bool:
        pass

    def __and__(self, other: "Specification[T]") -> "AndSpecification[T]":
        return AndSpecification(self, other)

    def __or__(self, other: "Specification[T]") -> "OrSpecification[T]":
        return OrSpecification(self, other)

    def __invert__(self) -> "NotSpecification[T]":
        return NotSpecification(self)


# =============================================================================
# Composite Specifications (Combinators)
# =============================================================================


class AndSpecification(Specification[T], Generic[T]):
    def __init__(self, left: Specification[T], right: Specification[T]):
        self.left = left
        self.right = right

    def is_satisfied_by(self, candidate: T) -> bool:
        return self.left.is_satisfied_by(candidate) and self.right.is_satisfied_by(
            candidate
        )


class OrSpecification(Specification[T], Generic[T]):
    def __init__(self, left: Specification[T], right: Specification[T]):
        self.left = left
        self.right = right

    def is_satisfied_by(self, candidate: T) -> bool:
        return self.left.is_satisfied_by(candidate) or self.right.is_satisfied_by(
            candidate
        )


class NotSpecification(Specification[T], Generic[T]):
    def __init__(self, spec: Specification[T]):
        self.spec = spec

    def is_satisfied_by(self, candidate: T) -> bool:
        return not self.spec.is_satisfied_by(candidate)


# =============================================================================
# Concrete Specifications (Rules)
# =============================================================================


class HasStockSpecification(Specification[Product]):
    def is_satisfied_by(self, candidate: Product) -> bool:
        return candidate.stock_count > 0


class PriceBelowSpecification(Specification[Product]):
    def __init__(self, max_price: float):
        self.max_price = max_price

    def is_satisfied_by(self, candidate: Product) -> bool:
        return candidate.price < self.max_price


class CategorySpecification(Specification[Product]):
    def __init__(self, category: str):
        self.category = category

    def is_satisfied_by(self, candidate: Product) -> bool:
        return candidate.category == self.category


class IsPremiumCustomerSpecification(Specification[Customer]):
    def is_satisfied_by(self, candidate: Customer) -> bool:
        return candidate.is_premium


class HasOrderHistorySpecification(Specification[Customer]):
    def __init__(self, min_orders: int):
        self.min_orders = min_orders

    def is_satisfied_by(self, candidate: Customer) -> bool:
        return candidate.total_orders_count >= self.min_orders


# =============================================================================
# Execution
# =============================================================================

if __name__ == "__main__":
    # 1. Setup test data
    laptop = Product("Laptop", 1200.0, 5, "Electronics")
    phone = Product("Phone", 800.0, 0, "Electronics")
    book = Product("Python Guide", 30.0, 20, "Books")

    alice = Customer("Alice", is_premium=True, total_orders_count=10)
    bob = Customer("Bob", is_premium=False, total_orders_count=2)

    # 2. Define Product Selection Rules
    # We want affordable electronic products that are currently in stock.
    in_stock = HasStockSpecification()
    electronics = CategorySpecification("Electronics")
    affordable = PriceBelowSpecification(1000.0)

    # Combine specifications using operators: AND (&), OR (|), NOT (~)
    target_promo_spec = in_stock & electronics & affordable

    print("--- Evaluating Product Specifications ---")
    for prod in [laptop, phone, book]:
        satisfied = target_promo_spec.is_satisfied_by(prod)
        print(f"Product '{prod.name}' eligible for promo? {satisfied}")
        # Explanations:
        # Laptop: In stock (Yes), Electronics (Yes), Affordable (No: $1200 > $1000) -> False
        # Phone: In stock (No: 0 items), Electronics (Yes), Affordable (Yes: $800 < $1000) -> False
        # Book: In stock (Yes), Electronics (No: Books), Affordable (Yes: $30 < $1000) -> False

    # Let's adjust rule to include all affordable items OR in-stock electronics:
    flexible_rule = affordable | (in_stock & electronics)
    print(
        "\n--- Evaluating Product with Flexible Rule (Affordable OR In-Stock Electronics) ---"
    )
    for prod in [laptop, phone, book]:
        print(f"Product '{prod.name}': {flexible_rule.is_satisfied_by(prod)}")

    # 3. Define Customer Promo eligibility
    # Customer qualifies for discount if they are Premium OR have placed at least 5 orders,
    # and they are NOT named Bob (just for testing NOT spec).
    is_premium = IsPremiumCustomerSpecification()
    has_5_orders = HasOrderHistorySpecification(5)

    promo_eligibility_spec = is_premium | has_5_orders

    print("\n--- Evaluating Customer Specifications ---")
    for cust in [alice, bob]:
        print(
            f"Customer '{cust.name}' eligible for discount? {promo_eligibility_spec.is_satisfied_by(cust)}"
        )
