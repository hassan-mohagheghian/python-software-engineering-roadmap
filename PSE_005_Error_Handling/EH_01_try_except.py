# Error Handling - try / except
# -----------------------------------------------------------------------------
# Errors happen when a program receives unexpected input or reaches an invalid
# state.
#
# A try / except block lets the program handle an error instead of crashing.
#
# -----------------------------------------------------------------------------
# Key ideas:
#
# - Put risky code inside try.
# - Catch specific exceptions with except.
# - Keep normal logic outside the except block when possible.
# - Avoid broad except blocks unless you have a clear reason.
#
# -----------------------------------------------------------------------------


def divide_numbers(a: str, b: str):
    try:
        number_a = float(a)
        number_b = float(b)
        result = number_a / number_b
    except ValueError:
        print("Invalid input: both values must be numbers.")
        return None
    except ZeroDivisionError:
        print("Invalid operation: cannot divide by zero.")
        return None

    return result


def main():
    print("===== Valid Input =====")
    print(divide_numbers("10", "2"))

    print("\n===== Invalid Number =====")
    print(divide_numbers("ten", "2"))

    print("\n===== Division By Zero =====")
    print(divide_numbers("10", "0"))


if __name__ == "__main__":
    main()
