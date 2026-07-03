# System Design - Database Indexing
# -----------------------------------------------------------------------------
# A database index is a data structure that improves the speed of data retrieval
# operations on a database table at the cost of additional storage and write
# overhead.
#
# Without an index, the database must scan every row (full table scan).
# With an index, it can jump directly to the relevant rows.
#
# -----------------------------------------------------------------------------
# How it works:
#
#   Table: users (id, name, email, age)
#
#   Without index on 'email':
#     SELECT * FROM users WHERE email = 'alice@example.com'
#     → Scans ALL rows (O(n))
#
#   With index on 'email':
#     → Looks up in index first (O(log n) for B-tree)
#     → Jumps directly to the row
#
# -----------------------------------------------------------------------------
# Common Index Types:
#
# 1. B-Tree Index (default in most databases)
#    - Balanced tree, good for range queries and equality
#    - WHERE age > 25, WHERE name = 'Alice'
#
# 2. Hash Index
#    - Only for equality comparisons
#    - Faster than B-Tree for exact matches
#    - Cannot do range queries
#
# 3. Composite Index
#    - Index on multiple columns (name, age)
#    - Best when queries filter on the leftmost columns
#
# -----------------------------------------------------------------------------
# Trade-offs:
#
#   Benefit: Faster reads (SELECT)
#   Cost:    Slower writes (INSERT, UPDATE, DELETE)
#            Additional storage space
#
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - Primary key index (automatic)
# - Unique index on email
# - Composite index on (user_id, created_at)
# - Full-text index for search
# -----------------------------------------------------------------------------

import bisect
import time
from dataclasses import dataclass
from typing import Optional

# -----------------------------------------------------------------------------
# Data Model
# -----------------------------------------------------------------------------


@dataclass
class User:
    id: int
    name: str
    email: str
    age: int


# -----------------------------------------------------------------------------
# FULL TABLE SCAN (Baseline - Always Correct)
# -----------------------------------------------------------------------------


class TableScan:
    def __init__(self):
        self.rows: list[User] = []
        self.scan_count = 0

    def insert(self, user: User):
        self.rows.append(user)

    def find_by_email(self, email: str) -> Optional[User]:
        self.scan_count = 0
        for row in self.rows:
            self.scan_count += 1
            if row.email == email:
                return row
        return None

    def find_by_age_range(self, min_age: int, max_age: int) -> list[User]:
        self.scan_count = 0
        result = []
        for row in self.rows:
            self.scan_count += 1
            if min_age <= row.age <= max_age:
                result.append(row)
        return result


# -----------------------------------------------------------------------------
# CONSISTENT INDEX (Simulated B-Tree)
# -----------------------------------------------------------------------------


class BTreeIndex:
    """
    Corrected index simulation:
    - Uses (key, row_id) fully
    - Guarantees same results as table scan
    - Uses bisect for range correctness
    """

    def __init__(self):
        self.entries: list[tuple] = []  # (key, row_id)
        self.ops = 0

    def insert(self, key, row_id: int):
        bisect.insort(self.entries, (key, row_id))

    # -------------------------
    # Equality search
    # -------------------------
    def find(self, key) -> list[int]:
        self.ops = 0

        start = bisect.bisect_left(self.entries, (key, -float("inf")))
        end = bisect.bisect_right(self.entries, (key, float("inf")))

        self.ops += 2  # two binary searches

        return [row_id for _, row_id in self.entries[start:end]]

    # -------------------------
    # Range search (FIXED)
    # -------------------------
    def find_range(self, min_key, max_key) -> list[int]:
        self.ops = 0

        start = bisect.bisect_left(self.entries, (min_key, -float("inf")))
        end = bisect.bisect_right(self.entries, (max_key, float("inf")))

        self.ops += 2  # binary searches only

        return [row_id for _, row_id in self.entries[start:end]]


# -----------------------------------------------------------------------------
# INDEXED TABLE (Correct Behavior)
# -----------------------------------------------------------------------------


class IndexedTable:
    def __init__(self):
        self.rows: dict[int, User] = {}
        self.email_index = BTreeIndex()
        self.age_index = BTreeIndex()
        self._next_id = 0

    def insert(self, user: User):
        user.id = self._next_id
        self.rows[user.id] = user

        self.email_index.insert(user.email, user.id)
        self.age_index.insert(user.age, user.id)

        self._next_id += 1

    def find_by_email(self, email: str) -> Optional[User]:
        ids = self.email_index.find(email)
        return self.rows[ids[0]] if ids else None

    def find_by_age_range(self, min_age: int, max_age: int) -> list[User]:
        ids = self.age_index.find_range(min_age, max_age)
        return [self.rows[i] for i in ids]


# -----------------------------------------------------------------------------
# DATA (deterministic)
# -----------------------------------------------------------------------------


def generate_users(n: int) -> list[User]:
    users = []
    for i in range(n):
        users.append(
            User(
                id=i,
                name=f"User_{i:04d}",
                email=f"user{i}@example.com",
                age=18 + (i % 50),
            )
        )
    return users


# -----------------------------------------------------------------------------
# VALIDATION (VERY IMPORTANT PART)
# -----------------------------------------------------------------------------


def assert_same_results(a: list[User], b: list[User]):
    assert sorted([u.id for u in a]) == sorted([u.id for u in b]), (
        "Mismatch between scan and index results!"
    )


# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------


def main():
    users = generate_users(10000)

    # ------------------ TABLE SCAN ------------------
    print("=" * 60)
    print("WITHOUT INDEX (Full Scan)")
    print("=" * 60)

    table = TableScan()
    for u in users:
        table.insert(u)

    start = time.perf_counter()
    r1 = table.find_by_email("user5000@example.com")
    t = time.perf_counter() - start

    print("\nEmail search:")
    print(f"Found: {r1.name}" if r1 else "Not Found")
    print("Rows scanned:", table.scan_count)
    print("Time ms:", round(t * 1000, 4))

    start = time.perf_counter()
    scan_age = table.find_by_age_range(25, 30)
    t = time.perf_counter() - start

    print("\nAge range search:")
    print("Results:", len(scan_age))
    print("Rows scanned:", table.scan_count)
    print("Time ms:", round(t * 1000, 4))

    # ------------------ INDEX ------------------
    print("\n" + "=" * 60)
    print("WITH INDEX (B-Tree)")
    print("=" * 60)

    indexed = IndexedTable()
    for u in users:
        indexed.insert(u)

    start = time.perf_counter()
    r2 = indexed.find_by_email("user5000@example.com")
    t = time.perf_counter() - start

    print("\nEmail search:")
    print(f"Found: {r2.name}" if r2 else "Not Found")
    print("Index ops:", indexed.email_index.ops)
    print("Time ms:", round(t * 1000, 4))

    start = time.perf_counter()
    idx_age = indexed.find_by_age_range(25, 30)
    t = time.perf_counter() - start

    print("\nAge range search:")
    print("Results:", len(idx_age))
    print("Index ops:", indexed.age_index.ops)
    print("Time ms:", round(t * 1000, 4))

    # ------------------ CONSISTENCY CHECK ------------------
    assert_same_results(scan_age, idx_age)

    print("\n" + "=" * 60)
    print("CONSISTENCY CHECK: PASSED")
    print("=" * 60)

    # ------------------ SUMMARY ------------------
    print("\nSummary:")
    print("Scan = O(n)")
    print("Index = O(log n + k)")
    print("Results are identical, only speed differs")


if __name__ == "__main__":
    main()
