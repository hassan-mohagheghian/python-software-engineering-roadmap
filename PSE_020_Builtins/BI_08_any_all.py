# Builtins - any() and all()
# -----------------------------------------------------------------------------
# any() returns True if at least one element is truthy.
# all() returns True if all elements are truthy.
# Both short-circuit (stop early when possible).
#
# Key concepts:
# 1. any() — exists / at least one
# 2. all() — for all / every single
# 3. Short-circuit evaluation
# 4. Common patterns with generator expressions
# -----------------------------------------------------------------------------


# =============================================================================
# any()
# =============================================================================


numbers = [0, 0, 0, 1, 0]
print(f"any(numbers): {any(numbers)}")

empty = [0, False, None, ""]
print(f"any(empty): {any(empty)}")


# =============================================================================
# all()
# =============================================================================


all_positive = [1, 2, 3, 4, 5]
print(f"all positive: {all_positive}: {all(all_positive)}")

mixed = [1, 2, 0, 4]
print(f"all mixed: {mixed}: {all(mixed)}")


# =============================================================================
# With Generator Expressions
# =============================================================================


words = ["hello", "world", "python"]
print(f"any long: {any(len(w) > 5 for w in words)}")
print(f"all non-empty: {all(w for w in words)}")


# =============================================================================
# Practical Patterns
# =============================================================================


# Check if any element matches condition
def has_even(numbers):
    return any(n % 2 == 0 for n in numbers)


def all_even(numbers):
    return all(n % 2 == 0 for n in numbers)


print(f"[1,3,5] has even: {has_even([1, 3, 5])}")
print(f"[2,4,6] all even: {all_even([2, 4, 6])}")


# Validate data
def validate_age(ages):
    """Check all ages are between 0 and 150."""
    return all(0 <= age <= 150 for age in ages)


print(f"Valid ages: {validate_age([25, 30, 45])}")
print(f"Invalid ages: {validate_age([25, -5, 200])}")


# Check permissions
def has_permission(user, required, permissions):
    """Check if user has any of the required permissions."""
    return any(p in permissions for p in required)


user_perms = ["read", "write"]
print(f"Can edit: {has_permission('user', ['read', 'write'], user_perms)}")
print(f"Can admin: {has_permission('user', ['admin'], user_perms)}")


def main():
    print("=== any() and all() ===")
    nums = [2, 4, 6, 8]
    print(f"All even: {all(n % 2 == 0 for n in nums)}")
    print(f"Any > 5: {any(n > 5 for n in nums)}")


if __name__ == "__main__":
    main()
