# Builtins - zip()
# -----------------------------------------------------------------------------
# zip() combines multiple iterables into tuples, stopping at the shortest.
# It is useful for parallel iteration over related sequences.
#
# Key concepts:
# 1. Basic zip — pair elements from two iterables
# 2. Multiple iterables
# 3. zip_longest — fill missing values
# 4. Unzipping with zip(*...)
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Zip
# =============================================================================


names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]

for name, score in zip(names, scores):
    print(f"  {name}: {score}")


# =============================================================================
# Multiple Iterables
# =============================================================================


ids = [1, 2, 3]
names = ["Alice", "Bob", "Charlie"]
roles = ["admin", "user", "viewer"]

for id_, name, role in zip(ids, names, roles):
    print(f"  #{id_} {name} ({role})")


# =============================================================================
# Converting to List/Dict
# =============================================================================


pairs = list(zip(names, scores))
print(f"Pairs: {pairs}")

mapping = dict(zip(names, scores))
print(f"Dict: {mapping}")


# =============================================================================
# Unzipping
# =============================================================================


pairs = [("a", 1), ("b", 2), ("c", 3)]
letters, numbers = zip(*pairs)
print(f"Letters: {letters}")
print(f"Numbers: {numbers}")


# =============================================================================
# Practical: Parallel Processing
# =============================================================================


def calculate_grades(names, scores):
    """Create formatted grade report."""
    results = []
    for name, score in zip(names, scores):
        grade = "A" if score >= 90 else "B" if score >= 80 else "C"
        results.append(f"{name}: {score} ({grade})")
    return results


print("Grades:")
for line in calculate_grades(names, scores):
    print(f"  {line}")


def main():
    print("=== zip() ===")
    keys = ["a", "b", "c"]
    values = [1, 2, 3]
    print(f"Zipped: {list(zip(keys, values))}")
    print(f"Unzipped: {list(zip(*[(1, 'a'), (2, 'b')]))}")


if __name__ == "__main__":
    main()
