# Python Basics - Dictionaries
# -----------------------------------------------------------------------------
# Dictionaries are unordered (Python 3.7+: ordered), mutable key-value pairs.
#
# Key concepts:
# 1. Creation — literal, dict(), fromkeys(), comprehension.
# 2. Accessing — get(), setdefault(), [].
# 3. Methods — keys(), values(), items(), update(), pop().
# 4. Iteration — looping over keys, values, items.
# 5. Nested dictionaries — dictionaries inside dictionaries.
# 6. Dictionary comprehension — creating dicts programmatically.
# -----------------------------------------------------------------------------


# =============================================================================
# Dictionary Creation
# =============================================================================


# Literal
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Constructor
settings = dict(theme="dark", font_size=14, auto_save=True)

# From keys
keys = ["a", "b", "c"]
from_keys_dict = dict.fromkeys(keys, 0)

# Comprehension
squares = {x: x**2 for x in range(1, 6)}

print(f"Person: {person}")
print(f"Settings: {settings}")
print(f"From_Keys: {from_keys_dict}")
print(f"Squares: {squares}")


# =============================================================================
# Accessing Values
# =============================================================================


config = {"host": "localhost", "port": 8080}

# Bracket notation (KeyError if missing)
print(f"\nHost: {config['host']}")

# .get() with default (safe)
print(f"Timeout: {config.get('timeout', 30)}")
print(f"Port: {config.get('port', 3000)}")

# setdefault — get or set if missing
config.setdefault("debug", False)
print(f"After setdefault: {config}")


# =============================================================================
# Modifying Dictionaries
# =============================================================================


data = {"a": 1, "b": 2}

# Add/Update
data["c"] = 3
data["a"] = 10
print(f"\nAfter add/update: {data}")

# update() — merge another dict
data.update({"d": 4, "e": 5})
print(f"After update: {data}")

# Remove
removed = data.pop("e")
print(f"After pop('e'): {data}, removed: {removed}")

del data["d"]
print(f"After del: {data}")

# clear()
copy = data.copy()
copy.clear()
print(f"After clear: {copy}")


# =============================================================================
# Dictionary Methods
# =============================================================================


user = {"name": "Bob", "age": 25, "role": "admin"}

print(f"\nKeys: {list(user.keys())}")
print(f"Values: {list(user.values())}")
print(f"Items: {list(user.items())}")

# Check existence
print(f"\n'name' in user: {'name' in user}")
print(f"'email' in user: {'email' in user}")

# Length
print(f"Length: {len(user)}")


# =============================================================================
# Iteration
# =============================================================================


scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

print("\n--- Loop over keys ---")
for name in scores:
    print(f"  {name}")

print("\n--- Loop over values ---")
for score in scores.values():
    print(f"  {score}")

print("\n--- Loop over items ---")
for name, score in scores.items():
    print(f"  {name}: {score}")


# =============================================================================
# Dictionary Comprehension
# =============================================================================


# Basic
word_lengths = {w: len(w) for w in ["hello", "world", "python"]}
print(f"\nWord lengths: {word_lengths}")

# With condition
passed = {name: score for name, score in scores.items() if score >= 80}
print(f"Passed: {passed}")

# Transform values
doubled = {k: v * 2 for k, v in scores.items()}
print(f"Doubled: {doubled}")

# Swap keys and values
swapped = {v: k for k, v in scores.items()}
print(f"Swapped: {swapped}")


# =============================================================================
# Nested Dictionaries
# =============================================================================


company = {
    "engineering": {"headcount": 50, "lead": "Alice"},
    "marketing": {"headcount": 30, "lead": "Bob"},
}

print(f"\nCompany: {company}")
print(f"Engineering lead: {company['engineering']['lead']}")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Dictionary Creation ===")
    a = {"x": 1, "y": 2, "z": 3}
    b = dict(name="Alice", age=30)
    c = {i: i**2 for i in range(5)}
    print(f"  a = {a}")
    print(f"  b = {b}")
    print(f"  c = {c}")

    print("\n=== Accessing ===")
    print(f"  a['x'] = {a['x']}")
    print(f"  a.get('w', 0) = {a.get('w', 0)}")

    print("\n=== Modifying ===")
    a["w"] = 4
    a.update({"v": 5})
    print(f"  After add: {a}")

    print("\n=== Iteration ===")
    for key, value in a.items():
        print(f"  {key}: {value}")

    print("\n=== Comprehension ===")
    names = ["alice", "bob", "charlie"]
    name_map = {name: name.upper() for name in names}
    print(f"  {name_map}")

    print("\n=== Nested ===")
    users = {
        "u1": {"name": "Alice", "age": 30},
        "u2": {"name": "Bob", "age": 25},
    }
    for uid, info in users.items():
        print(f"  {uid}: {info['name']} ({info['age']})")


if __name__ == "__main__":
    main()
