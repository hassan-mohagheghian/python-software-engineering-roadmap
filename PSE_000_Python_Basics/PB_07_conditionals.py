# Python Basics - Conditionals
# -----------------------------------------------------------------------------
# Conditionals control the flow of execution based on boolean expressions.
#
# Key concepts:
# 1. if / elif / else — standard conditional branching.
# 2. Ternary operator — inline conditional expression.
# 3. match / case — structural pattern matching (Python 3.10+).
# 4. Logical operators — and, or, not for combining conditions.
# 5. Chained comparisons — Pythonic way to check ranges.
# -----------------------------------------------------------------------------


# =============================================================================
# Basic if / elif / else
# =============================================================================


def grade_score(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# =============================================================================
# Ternary Operator
# =============================================================================


def check_parity(n: int) -> str:
    return "even" if n % 2 == 0 else "odd"


# =============================================================================
# Logical Operators
# =============================================================================


def check_eligibility(age: int, has_id: bool) -> bool:
    return age >= 18 and has_id


def get_discount(member: bool, senior: bool) -> float:
    if member or senior:
        return 0.20
    return 0.0


# =============================================================================
# Chained Comparisons
# =============================================================================


def classify_age(age: int) -> str:
    if 0 <= age < 13:
        return "child"
    elif 13 <= age < 18:
        return "teenager"
    elif 18 <= age < 65:
        return "adult"
    elif age >= 65:
        return "senior"
    return "invalid"


def in_range(value: int, low: int, high: int) -> bool:
    return low <= value <= high


# =============================================================================
# Match / Case (Python 3.10+)
# =============================================================================


def http_status_message(status: int) -> str:
    match status:
        case 200:
            return "OK"
        case 301:
            return "Moved Permanently"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"


def describe_type(value) -> str:
    match value:
        case int():
            return f"Integer: {value}"
        case str():
            return f"String: '{value}'"
        case list():
            return f"List with {len(value)} items"
        case dict():
            return f"Dict with keys: {list(value.keys())}"
        case _:
            return f"Other: {type(value).__name__}"


# =============================================================================
# Nested Conditionals (with early returns)
# =============================================================================


def process_order(quantity: int, in_stock: bool, is_member: bool) -> str:
    if quantity <= 0:
        return "Invalid quantity"

    if not in_stock:
        return "Out of stock"

    if quantity > 100:
        return "Exceeds maximum order limit"

    discount = 0.1 if is_member else 0.0
    return f"Order placed with {discount:.0%} discount"


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Grading ===")
    for score in [95, 82, 67, 45]:
        print(f"Score {score} -> Grade {grade_score(score)}")

    print("\n=== Ternary ===")
    for n in [4, 7, 0, 11]:
        print(f"{n} is {check_parity(n)}")

    print("\n=== Logical Operators ===")
    print(f"Age 20, has_id=True: {check_eligibility(20, True)}")
    print(f"Age 16, has_id=True: {check_eligibility(16, True)}")
    print(f"Member, not senior: {get_discount(True, False)}")
    print(f"Not member, senior: {get_discount(False, True)}")

    print("\n=== Chained Comparisons ===")
    for age in [5, 15, 30, 70]:
        print(f"Age {age} -> {classify_age(age)}")
    print(f"5 in [1, 10]? {in_range(5, 1, 10)}")

    print("\n=== Match/Case ===")
    for status in [200, 404, 500, 418]:
        print(f"HTTP {status}: {http_status_message(status)}")

    print("\n=== Type Matching ===")
    test_values = [42, "hello", [1, 2, 3], {"a": 1}, 3.14]
    for v in test_values:
        print(f"{str(v):>15} -> {describe_type(v)}")

    print("\n=== Order Processing ===")
    cases = [(5, True, True), (0, True, False), (10, False, True), (200, True, True)]
    for qty, stock, member in cases:
        result = process_order(qty, stock, member)
        print(f"qty={qty}, stock={stock}, member={member} -> {result}")


if __name__ == "__main__":
    main()
