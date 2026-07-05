# Functions - *args and **kwargs
# -----------------------------------------------------------------------------
# *args lets a function accept any number of positional arguments as a tuple.
# **kwargs lets a function accept any number of keyword arguments as a dict.
#
# You can combine required parameters, *args, and **kwargs in one signature.
# -----------------------------------------------------------------------------


# =============================================================================
# *args — variable positional arguments
# =============================================================================


def sum_all(*args: int) -> int:
    return sum(args)


def average(*values: float) -> float:
    return sum(values) / len(values)


# =============================================================================
# **kwargs — variable keyword arguments
# =============================================================================


def print_info(**kwargs) -> None:
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


def build_profile(name: str, **details) -> dict:
    profile = {"name": name}
    profile.update(details)
    return profile


# =============================================================================
# Combining required, *args, and **kwargs
# =============================================================================


def combined(required: str, *args, **kwargs):
    print(f"  Required: {required}")
    print(f"  Args: {args}")
    print(f"  Kwargs: {kwargs}")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== *args ===")
    print(f"sum_all(1, 2, 3, 4, 5): {sum_all(1, 2, 3, 4, 5)}")
    print(f"average(10, 20, 30): {average(10, 20, 30)}")

    print("\n=== **kwargs ===")
    print("print_info(name='Alice', age=30):")
    print_info(name="Alice", age=30)
    print(f"build_profile('Bob', role='dev'): {build_profile('Bob', role='dev')}")

    print("\n=== Combined ===")
    print("combined('hello', 1, 2, key='val'):")
    combined("hello", 1, 2, key="val")


if __name__ == "__main__":
    main()
