# Functions - Basic Functions
# -----------------------------------------------------------------------------
# A function is a reusable block of code.
#
# Functions help you:
#
# - Give a name to a small task
# - Avoid repeating the same code
# - Accept input through parameters
# - Return output with return
#
# -----------------------------------------------------------------------------


def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


def calculate_total(price: float, tax_rate: float = 0.09) -> float:
    return price + (price * tax_rate)


def print_invoice(customer_name: str, total: float):
    print(f"Customer: {customer_name}")
    print(f"Total: ${total:.2f}")


def main():
    print(greet("Alice"))
    print(add(10, 5))

    default_total = calculate_total(100)
    custom_total = calculate_total(price=100, tax_rate=0.2)

    print_invoice("Alice", default_total)
    print_invoice(customer_name="Bob", total=custom_total)


if __name__ == "__main__":
    main()
