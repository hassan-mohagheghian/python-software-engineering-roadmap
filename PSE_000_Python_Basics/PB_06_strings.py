# Python Basics - Strings
# -----------------------------------------------------------------------------
# Strings are immutable sequences of Unicode characters.
#
# Key concepts:
# 1. Creation — single, double, triple quotes, raw strings.
# 2. Indexing and Slicing — accessing characters and substrings.
# 3. Methods — common string operations.
# 4. Formatting — f-strings, .format(), % formatting.
# 5. Escape characters — special characters in strings.
# -----------------------------------------------------------------------------


# =============================================================================
# String Creation
# =============================================================================


single = 'Hello'
double = "World"
triple = """Multi-line
string"""
raw = r"C:\new\folder"  # backslashes treated literally
byte = b"hello"  # bytes object

print(f"Single: {single}")
print(f"Double: {double}")
print(f"Raw: {raw}")
print(f"Bytes: {byte}")


# =============================================================================
# Indexing and Slicing
# =============================================================================


text = "Python"

# Indexing (0-based)
print(f"\nFirst char: {text[0]}")
print(f"Last char: {text[-1]}")

# Slicing [start:stop:step]
print(f"Slice [0:3]: {text[0:3]}")
print(f"Slice [2:]: {text[2:]}")
print(f"Slice [:-2]: {text[:-2]}")
print(f"Reverse: {text[::-1]}")


# =============================================================================
# Common Methods
# =============================================================================


s = "  Hello, World!  "

print(f"\nOriginal: '{s}'")
print(f"strip(): '{s.strip()}'")
print(f"lower(): '{s.lower()}'")
print(f"upper(): '{s.upper()}'")
print(f"title(): '{s.strip().title()}'")
print(f"replace(): '{s.replace('World', 'Python')}'")
print(f"split(','): {s.strip().split(',')}")

# Check methods
print(f"\n'hello'.isalpha(): {'hello'.isalpha()}")
print(f"'123'.isdigit(): {'123'.isdigit()}")
print(f"'hello123'.isalnum(): {'hello123'.isalnum()}")
print(f"'hello'.startswith('he'): {'hello'.startswith('he')}")
print(f"'hello'.endswith('lo'): {'hello'.endswith('lo')}")
print(f"'hello'.find('ll'): {'hello'.find('ll')}")
print(f"'hello'.count('l'): {'hello'.count('l')}")


# =============================================================================
# String Formatting
# =============================================================================


name = "Alice"
age = 30
score = 95.678

# f-strings (Python 3.6+, recommended)
print(f"\nf-string: {name} is {age} years old")
print(f"f-string with formatting: {score:.2f}")
print(f"f-string with expression: {2 + 2 = }")
print(f"f-string with alignment: |{name:>10}|{name:<10}|{name:^10}|")
print(f"f-string with padding: {42:05d}")

# .format() method
print(".format(): {} is {} years old".format(name, age))
print(".format() with index: {0} is {1}".format(name, age))
print(".format() with names: {n} is {a}".format(n=name, a=age))

# % formatting (old style)
print("%% formatting: %s is %d years old" % (name, age))


# =============================================================================
# String Joining and Splitting
# =============================================================================


words = ["Python", "is", "awesome"]

# Join
sentence = " ".join(words)
print(f"\nJoin: {sentence}")
print(f"Join with dash: {'-'.join(words)}")

# Split
csv_data = "apple,banana,cherry"
print(f"Split: {csv_data.split(',')}")
print(f"Splitlines: {'line1\nline2\nline3'.splitlines()}")


# =============================================================================
# Escape Characters
# =============================================================================


print("\nNewline:\\n -> 'Hello\nWorld'")
print("Tab:\\t -> 'Hello\tWorld'")
print("Backslash: \\\\ -> This is Backslash \\")
print("Quote: \\' and \\\" -> For ' and \" ")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== String Basics ===")
    text = "Hello, Python World!"
    print(f"Original: {text}")
    print(f"Length: {len(text)}")
    print(f"Uppercase: {text.upper()}")
    print(f"Lowercase: {text.lower()}")

    print("\n=== Slicing ===")
    print(f"First 5: {text[:5]}")
    print(f"Last 6: {text[-6:]}")
    print(f"Every 2nd: {text[::2]}")
    print(f"Reversed: {text[::-1]}")

    print("\n=== Searching ===")
    print(f"Find 'Python': {text.find('Python')}")
    print(f"Count 'l': {text.count('l')}")
    print(f"Starts with 'Hello': {text.startswith('Hello')}")
    print(f"Ends with '!': {text.endswith('!')}")

    print("\n=== Formatting ===")
    for i in range(1, 4):
        print(f"Item {i:>2}: {'*' * i}")

    print("\n=== Split and Join ===")
    csv = "name,age,city"
    fields = csv.split(",")
    print(f"Split: {fields}")
    print(f"Join: {' | '.join(fields)}")

    print("\n=== Validation ===")
    tests = ["hello", "123", "hello123", "hello 123", ""]
    for t in tests:
        print(f"  '{t}': alpha={t.isalpha()}, digit={t.isdigit()}, alnum={t.isalnum()}")


if __name__ == "__main__":
    main()
