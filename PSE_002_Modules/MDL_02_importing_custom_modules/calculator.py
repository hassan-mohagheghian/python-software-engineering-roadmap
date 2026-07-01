# Module - Calculator
# -----------------------------------------------------------------------------
# A module is a Python file that can expose variables, functions, and classes to
# other Python files.
#
# This file is imported by main.py.
# -----------------------------------------------------------------------------


DEFAULT_TAX_RATE = 0.09


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def calculate_total(price: float, tax_rate: float = DEFAULT_TAX_RATE) -> float:
    return price + (price * tax_rate)


def main():
    print("This runs only when calculator.py is executed directly.")
    print(calculate_total(100))


if __name__ == "__main__":
    main()
