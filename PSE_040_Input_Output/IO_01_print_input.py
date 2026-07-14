# Input/Output - print() and input()
# -----------------------------------------------------------------------------
# print() outputs text to stdout; input() reads from stdin.
# Both support formatting options for clean console output.
#
# Key concepts:
# 1. print() with sep, end, file
# 2. f-string formatting
# 3. input() with prompt
# 4. String formatting methods
# -----------------------------------------------------------------------------


# =============================================================================
# print() Basics
# =============================================================================


print("Hello, World!")
print("Multiple", "arguments", "joined by space")
print("No newline", end="")
print(" — same line")


# =============================================================================
# Separator
# =============================================================================


print("a", "b", "c", sep=", ")
print("2026", "07", "05", sep="-")


# =============================================================================
# Formatting
# =============================================================================


name = "Alice"
age = 30
height = 5.7

# f-strings (preferred)
print(f"{name} is {age} years old, {height:.1f}ft tall")

# format method
print("{} is {} years old".format(name, age))

# % formatting (old style)
print("%s is %d years old" % (name, age))


# =============================================================================
# Number Formatting
# =============================================================================


pi = 3.14159265
print(f"Pi: {pi:.2f}")
print(f"Pi: {pi:.4f}")
print(f"Comma: {1000000:,}")
print(f"Percent: {0.85:.1%}")
print(f"Zero-padded: {42:05d}")


# =============================================================================
# input()
# =============================================================================


name = input("Enter your name: ")
print(f"Hello, {name}!")

age = int(input("Enter your age: "))
print(f"You are {age} years old.")


# =============================================================================
# Alignment
# =============================================================================


items = [("Apple", 1.50), ("Banana", 0.75), ("Cherry", 3.25)]
for name, price in items:
    print(f"{name:<10} ${price:>6.2f}")


def main():
    print("=== print() and input() ===")
    print()

    name = input("Enter your name: ")
    item = input("Enter an item name: ")
    price = float(input("Enter the item price: "))

    print()
    print(f"Hello, {name}!")
    print(f"{'Item':<10} {'Price':>8}")
    print("-" * 20)
    print(f"{item:<10} ${price:>6.2f}")


if __name__ == "__main__":
    main()
