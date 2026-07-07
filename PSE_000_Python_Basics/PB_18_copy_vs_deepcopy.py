# Python Basics - Copy vs Deepcopy
# -----------------------------------------------------------------------------
# When copying mutable objects, shallow copy shares nested references while
# deep copy creates fully independent clones.
#
# Key concepts:
# 1. Assignment (=) — creates a new reference, NOT a copy
# 2. Shallow copy — copy.copy() or .copy() — one level deep
# 3. Deep copy — copy.deepcopy() — recursively independent
# 4. Nested objects — shallow copies share inner mutable objects
# 5. Custom copy — __copy__() and __deepcopy__() protocols
# -----------------------------------------------------------------------------

import copy
import time

# =============================================================================
# Assignment is NOT a Copy
# =============================================================================


original = [1, 2, [3, 4]]
reference = original  # just another name for the same object

reference.append(5)
reference[2][0] = 99

print(f"Original: {original}")  # [1, 2, [99, 4], 5]
print(f"Reference: {reference}")  # same thing
print(f"Same object: {original is reference}")  # True


# =============================================================================
# Shallow Copy
# =============================================================================


# Using copy.copy()
original = [1, 2, [3, 4]]
shallow = copy.copy(original)

# Using .copy() method
shallow2 = original.copy()

# Using slicing
shallow3 = original[:]

# Using list constructor
shallow4 = list(original)

print(f"\nOriginal: {original}")
print(f"Shallow: {shallow}")
print(f"Same object: {original is shallow}")  # False

# Modify outer — independent
shallow.append(5)
print("\nAfter shallow.append(5):")
print(f"  Original: {original}")  # [1, 2, [3, 4]] — unchanged
print(f"  Shallow:  {shallow}")  # [1, 2, [3, 4], 5]

# Modify inner — SHARED
shallow[2][0] = 99
print("\nAfter shallow[2][0] = 99:")
print(f"  Original: {original}")  # [1, 2, [99, 4]] — CHANGED!
print(f"  Shallow:  {shallow}")  # [1, 2, [99, 4], 5]


# =============================================================================
# Deep Copy
# =============================================================================


original = [1, 2, [3, 4]]
deep = copy.deepcopy(original)

print(f"\nOriginal: {original}")
print(f"Deep: {deep}")
print(f"Same object: {original is deep}")  # False

# Modify outer — independent
deep.append(5)
print("\nAfter deep.append(5):")
print(f"  Original: {original}")  # [1, 2, [3, 4]] — unchanged
print(f"  Deep:     {deep}")  # [1, 2, [3, 4], 5]

# Modify inner — INDEPENDENT
deep[2][0] = 99
print("\nAfter deep[2][0] = 99:")
print(f"  Original: {original}")  # [1, 2, [3, 4]] — unchanged!
print(f"  Deep:     {deep}")  # [1, 2, [99, 4], 5]


# =============================================================================
# Comparison: Assignment vs Shallow vs Deep
# =============================================================================


print("\n--- Side-by-side Comparison ---")
original = [1, 2, [3, 4]]

assigned = original
shallow = copy.copy(original)
deep = copy.deepcopy(original)

# Modify the nested list
original[2][0] = 99

print(f"Original: {original}")
print(f"Assigned: {assigned}")  # [1, 2, [99, 4]] — same reference
print(f"Shallow:  {shallow}")  # [1, 2, [99, 4]] — shares inner list
print(f"Deep:     {deep}")  # [1, 2, [3, 4]]  — fully independent


# =============================================================================
# Dictionaries
# =============================================================================


original = {"a": 1, "b": [2, 3]}
shallow = copy.copy(original)
deep = copy.deepcopy(original)

# Modify inner list
original["b"].append(4)

print(f"\nDict Original: {original}")
print(f"Dict Shallow:  {shallow}")  # b is [2, 3, 4]
print(f"Dict Deep:     {deep}")  # b is [2, 3]

# Add key — independent
shallow["c"] = 99
print("\nAfter shallow['c'] = 99:")
print(f"  'c' in original: {'c' in original}")  # False
print(f"  'c' in shallow:  {'c' in shallow}")  # True


# =============================================================================
# Copy for Different Types
# =============================================================================


# List
lst = [1, 2, 3]
print(f"\nlist.copy(): {lst.copy()}")
print(f"copy.copy(): {copy.copy(lst)}")
print(f"copy.deepcopy(): {copy.deepcopy(lst)}")

# Dict
d = {"a": 1, "b": 2}
print(f"\ndict.copy(): {d.copy()}")
print(f"copy.copy(): {copy.copy(d)}")

# Set
s = {1, 2, 3}
print(f"\nset.copy(): {s.copy()}")
print(f"copy.copy(): {copy.copy(s)}")

# Tuple (immutable — copy is same object)
t = (1, 2, [3, 4])
shallow = copy.copy(t)
deep = copy.deepcopy(t)
print(f"shallow is original: {shallow is t}")  # True
print(f"deep is original: {deep is t}")  # False
print(f"deep list is original list: {deep[2] is t[2]}")  # False


# =============================================================================
# Custom Copy Protocol
# =============================================================================


class Config:
    def __init__(self, settings, db_password):
        self.settings = settings
        self.db_password = db_password

    def __copy__(self):
        """Shallow copy — skip sensitive fields."""
        return Config(self.settings.copy(), "")

    def __deepcopy__(self, memo):
        """Deep copy — skip sensitive fields."""
        return Config(copy.deepcopy(self.settings, memo), "")

    def __repr__(self):
        return f"Config(settings={self.settings}, password='{self.db_password}')"


original = Config({"theme": "dark", "lang": "en"}, "s3cret")
shallow = copy.copy(original)
deep = copy.deepcopy(original)

print(f"\nOriginal: {original}")
print(f"Shallow:  {shallow}")
print(f"Deep:     {deep}")

# Modify original settings
original.settings["theme"] = "light"
print("\nAfter changing original theme:")
print(f"  Original: {original}")
print(f"  Shallow:  {shallow}")  # theme still dark
print(f"  Deep:     {deep}")  # theme still dark


# =============================================================================
# Performance Considerations
# =============================================================================


data = [[i] * 10 for i in range(1000)]

# Shallow copy
start = time.perf_counter()
for _ in range(1000):
    copy.copy(data)
shallow_time = time.perf_counter() - start

# Deep copy
start = time.perf_counter()
for _ in range(1000):
    copy.deepcopy(data)
deep_time = time.perf_counter() - start

print("\nPerformance (1000 copies of 1000x10 list):")
print(f"  Shallow: {shallow_time:.4f}s")
print(f"  Deep:    {deep_time:.4f}s")
print(f"  Ratio:   {deep_time / shallow_time:.1f}x slower")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Assignment (NOT a copy) ===")
    a = [1, 2, 3]
    b = a
    b.append(4)
    print(f"  a={a}, b={b} — same object!")

    print("\n=== Shallow Copy ===")
    original = [1, 2, [3, 4]]
    shallow = copy.copy(original)
    shallow[2][0] = 99
    print(f"  Original: {original}")
    print(f"  Shallow:  {shallow}")
    print(
        f"  Inner list shared: original[2] is shallow[2] = {original[2] is shallow[2]}"
    )

    print("\n=== Deep Copy ===")
    original = [1, 2, [3, 4]]
    deep = copy.deepcopy(original)
    deep[2][0] = 99
    print(f"  Original: {original}")
    print(f"  Deep:     {deep}")
    print(
        f"  Inner list independent: original[2] is deep[2] = {original[2] is deep[2]}"
    )

    print("\n=== When to Use What ===")
    print("  = (assignment):    When you want the same object")
    print("  copy (shallow):    For flat structures, speed matters")
    print("  deepcopy:          For nested structures, full independence")

    print("\n=== Quick Reference ===")
    lst = [1, [2, 3]]
    print(f"  .copy():    {lst.copy()}")
    print(f"  [:]:        {lst[:]}")
    print(f"  list():     {list(lst)}")
    print(f"  copy.copy(): {copy.copy(lst)}")

    main()
