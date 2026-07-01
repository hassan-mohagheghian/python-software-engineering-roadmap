# Modules - Importing Custom Modules
# -----------------------------------------------------------------------------
# Python code can be split into multiple files.
#
# A file can import another file as a module and reuse its functions,
# constants, and classes.
#
# In this example:
#
# - calculator.py defines reusable functions.
# - main.py imports calculator.py and uses those functions.
# - calculator.py has a __name__ guard so demo code does not run on import.
# -----------------------------------------------------------------------------

import calculator
from calculator import calculate_total


def main():
    print("===== Import whole module =====")
    print(calculator.add(10, 5))
    print(calculator.subtract(10, 5))

    print("\n===== Import one function =====")
    print(calculate_total(100))

    print("\n===== Import one constant through module =====")
    print(calculator.DEFAULT_TAX_RATE)


if __name__ == "__main__":
    main()
