# Open Closed Principle (OCP)
# Software entities (classes, modules, functions) should bee open for extension but closed for modification.
# You should be able to add new functionality without changing existing code.


# --------------- Wrong Usage ----------------
# Adding new discount type - MUST change the class!s
class DiscountCalculator:
    "Every time we ad a new customer type, we MUST modify this class"

    def calculate(self, customer_type: str, amount: int) -> float:
        if customer_type == "regular":
            return amount * 0.95  # 5% discount
        elif customer_type == "premium":
            return amount * 0.85  # 15% discount
        elif customer_type == "vip":
            return amount * 0.70  # 30% discount

        # Problem:
        # Adding "employee" discount requires modifying this method!
        # Adding "seasonal" discount requires modifying this method!
        # This class i NOT closed for modification.
        else:
            return amount


# Usage
calculator = DiscountCalculator()
print(calculator.calculate("regular", 100))  # 95.0
print(calculator.calculate("premium", 100))  # 85.0
print(calculator.calculate("vip", 100))  # 70.0


# --------------------- Right Usage -------------
from abc import ABC, abstractmethod


# Open for extension: create new discount strategies
class DiscountStrategy(ABC):
    """Abstract interface - open for extension"""

    @abstractmethod
    def calculate(self, amount: int):
        pass


# Closed for modification: Existing strategies don't (need to) change
class RegularDiscount(DiscountStrategy):
    """5% discount"""

    def calculate(self, amount: int):
        return amount * 0.95


class PremiumDiscount(DiscountStrategy):
    """15% discount"""

    def calculate(self, amount: int):
        return amount * 0.85


class VIPDiscount(DiscountStrategy):
    """30% discount"""

    def calculate(self, amount: int):
        return amount * 0.70


# NEW: Adding employee discount - EXTEND, don't modify
class EmployeeDiscount(DiscountStrategy):
    """40% discounts"""

    def calculate(self, amount: int):
        return amount * 0.60


# NEW: Adding seasonal discount - EXTEND, don't modify
class SeasonalDiscount(DiscountStrategy):
    """20% discounts"""

    def calculate(self, amount: int):
        return amount * 0.80


# The calculator is CLOSED for modification - it never changes!
class DiscountCalculator:
    def calculate(self, strategy: DiscountStrategy, amount: int):
        return strategy.calculate(amount=amount)


# Usage: extend behavior by adding new classes, not modifying existing ones

calculator = DiscountCalculator()
print(calculator.calculate(RegularDiscount(), 100))  # 95.0
print(calculator.calculate(PremiumDiscount(), 100))  # 85.0
print(calculator.calculate(VIPDiscount(), 100))  # 70.0
print(calculator.calculate(EmployeeDiscount(), 100))  # 60.0 (NEW - no modification!)
print(calculator.calculate(SeasonalDiscount(), 100))  # 80.0 (NEW - no modification!)
