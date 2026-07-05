# Functions - Lambda Functions
# -----------------------------------------------------------------------------
# A lambda is a small anonymous function defined inline.
# Lambdas are limited to a single expression — no statements, no assignments.
#
# Common uses:
# - Short callbacks for sorted(), map(), filter()
# - Small one-off functions that don't need a name
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Lambda
# =============================================================================

square = lambda x: x ** 2
add_lambda = lambda a, b: a + b
is_even = lambda x: x % 2 == 0


# =============================================================================
# Lambda with sorted, map, filter
# =============================================================================


def demonstrate_lambdas():
    # sorted with a key lambda
    words = ["cherry", "apple", "banana"]
    by_length = sorted(words, key=lambda w: len(w))
    print(f"  Sorted by length: {by_length}")

    # map — apply a function to every item
    numbers = [1, 2, 3, 4]
    squared = list(map(lambda x: x ** 2, numbers))
    print(f"  Squared: {squared}")

    # filter — keep items where the lambda returns True
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"  Evens: {evens}")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Basic Lambda ===")
    print(f"square(5): {square(5)}")
    print(f"add_lambda(3, 4): {add_lambda(3, 4)}")
    print(f"is_even(4): {is_even(4)}")

    print("\n=== Lambda with collections ===")
    demonstrate_lambdas()


if __name__ == "__main__":
    main()
