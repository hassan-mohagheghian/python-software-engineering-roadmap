# Algorithms - Big-O Complexity
# -----------------------------------------------------------------------------
# Big-O notation describes how runtime or memory usage grows as input size (n)
# increases. It answers: "If I double the data, how much slower does this get?"
#
# Common complexities (fastest → slowest):
#
#   O(1)       — constant: dict lookup, index access
#   O(log n)   — logarithmic: binary search, balanced tree ops
#   O(n)       — linear: scan a list once
#   O(n log n) — linearithmic: efficient sorting (Timsort)
#   O(n²)      — quadratic: nested loops over the same data
#
# Space complexity uses the same notation for extra memory used.
# -----------------------------------------------------------------------------


import time

# =============================================================================
# O(1) — Constant Time
# =============================================================================


def get_first(items: list) -> object | None:
    """Index access does not depend on list length."""
    return items[0] if items else None


def lookup_user(users: dict, user_id: str) -> str | None:
    """Hash map lookup is O(1) on average."""
    return users.get(user_id)


# =============================================================================
# O(n) — Linear Time
# =============================================================================


def linear_search(items: list, target) -> int:
    """Scan until found — worst case visits every element."""
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


def sum_values(numbers: list[int]) -> int:
    """One pass over the input."""
    total = 0
    for n in numbers:
        total += n
    return total


# =============================================================================
# O(log n) — Logarithmic Time
# =============================================================================


def binary_search(sorted_items: list[int], target: int) -> int:
    """Each step halves the search space."""
    left, right = 0, len(sorted_items) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_items[mid] == target:
            return mid
        if sorted_items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# =============================================================================
# O(n²) — Quadratic Time
# =============================================================================


def has_duplicate_naive(items: list) -> bool:
    """Compare every pair — O(n²)."""
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False


def has_duplicate_set(items: list) -> bool:
    """Single pass with a set — O(n) time, O(n) space."""
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False


# =============================================================================
# O(n log n) — Linearithmic Time
# =============================================================================


def top_scores_naive(scores: list[int], k: int) -> list[int]:
    """Sort entire list then slice — O(n log n)."""
    return sorted(scores, reverse=True)[:k]


def top_scores_heap(scores: list[int], k: int) -> list[int]:
    """heapq.nlargest — O(n log k), better when k << n."""
    import heapq

    return heapq.nlargest(k, scores)


# =============================================================================
# Timing Demo (illustrative, not a formal benchmark)
# =============================================================================


def scaling_demo():
    """Show how O(n²) grows faster than O(n) as n increases."""
    print("  Size   | O(n) linear scan | O(n²) nested loops")
    print("  -------|------------------|-------------------")
    for n in [1_000, 5_000, 10_000]:
        data = list(range(n))
        start = time.perf_counter()
        linear_search(data, n - 1)
        t_linear = time.perf_counter() - start

        start = time.perf_counter()
        has_duplicate_naive(list(range(n)))
        t_quad = time.perf_counter() - start

        print(f"  {n:6} | {t_linear:.6f}s         | {t_quad:.6f}s (n={n})")


# =============================================================================
# Usage
# =============================================================================


def main():
    users = {"u1": "Alice", "u2": "Bob"}
    scores = [88, 42, 95, 71, 63, 99, 54]
    sorted_scores = sorted(scores)

    print("=== O(1) — Constant ===")
    print(f"  First score: {get_first(scores)}")
    print(f"  User u1: {lookup_user(users, 'u1')}")

    print("\n=== O(n) — Linear Search ===")
    print(f"  Find 71 at index: {linear_search(scores, 71)}")
    print(f"  Sum: {sum_values(scores)}")

    print("\n=== O(log n) — Binary Search ===")
    print(f"  Find 63 at index: {binary_search(sorted_scores, 63)}")
    print(f"  Find 100 at index: {binary_search(sorted_scores, 100)}")

    print("\n=== O(n²) vs O(n) — Duplicate Detection ===")
    sample = [1, 2, 3, 4, 2]
    print(f"  Naive O(n²): {has_duplicate_naive(sample)}")
    print(f"  Set O(n):    {has_duplicate_set(sample)}")

    print("\n=== O(n log n) — Top K ===")
    print(f"  Sort slice: {top_scores_naive(scores, 3)}")
    print(f"  Heap:       {top_scores_heap(scores, 3)}")

    print("\n=== Scaling Demo ===")
    scaling_demo()

    print("\n=== Space Complexity ===")
    print("  O(1) space: binary_search — only uses a few variables")
    print("  O(n) space: has_duplicate_set — stores up to n items in a set")


if __name__ == "__main__":
    main()
