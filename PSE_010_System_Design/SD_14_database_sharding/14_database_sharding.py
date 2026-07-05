# System Design - Database Sharding
# -----------------------------------------------------------------------------
# Database Sharding is a technique for horizontal partitioning where data is
# split across multiple database instances (shards), each holding a subset
# of the total data.
#
# Unlike vertical partitioning (splitting columns), sharding splits ROWS
# across databases.
#
# -----------------------------------------------------------------------------
# Why shard:
#
# - Single database can't handle the data volume
# - Single database can't handle the write throughput
# - Need to distribute load across machines
#
# -----------------------------------------------------------------------------
# Sharding Strategies:
#
# 1. Hash-Based Sharding
#    - shard = hash(key) % num_shards
#    - Even distribution, but hard to add/remove shards
#
# 2. Range-Based Sharding
#    - shard by value range (e.g., user IDs 1-1000 → shard A)
#    - Easy to understand, but can create hotspots
#
# 3. Directory-Based Sharding
#    - Lookup table maps keys to shards
#    - Flexible, but adds a lookup step
#
# -----------------------------------------------------------------------------
# Challenges:
#
# - Cross-shard queries (joins across shards)
# - Rebalancing when adding/removing shards
# - Maintaining referential integrity
# - Hotspots if distribution is uneven
#
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - User data split by user_id
# - Orders split by region
# - Messages split by conversation_id
# - Multi-tenant SaaS (one shard per tenant)
# -----------------------------------------------------------------------------

import hashlib
from dataclasses import dataclass

# -----------------------------------------------------------------------------
# Data Model
# -----------------------------------------------------------------------------


@dataclass
class User:
    id: int
    name: str
    email: str
    region: str


# -----------------------------------------------------------------------------
# Individual Shard (simulates a separate database)
# -----------------------------------------------------------------------------


class Shard:
    def __init__(self, name: str):
        self.name = name
        self.data: dict[int, User] = {}
        self.query_count = 0

    def insert(self, user: User):
        self.data[user.id] = user
        print(f"    [{self.name}] Inserted user {user.id}: {user.name}")

    def get(self, user_id: int) -> User | None:
        self.query_count += 1
        return self.data.get(user_id)

    def count(self) -> int:
        return len(self.data)

    def get_all(self) -> list[User]:
        self.query_count += 1
        return list(self.data.values())


# -----------------------------------------------------------------------------
# Strategy 1: Hash-Based Sharding
# -----------------------------------------------------------------------------


class HashShardRouter:
    """
    Routes requests based on hash(key) % num_shards.
    Provides even distribution but resharding is expensive.
    """

    def __init__(self, shards: list[Shard]):
        self.shards = shards

    def _get_shard(self, key: int) -> Shard:
        hash_val = int(hashlib.md5(str(key).encode()).hexdigest(), 16)
        return self.shards[hash_val % len(self.shards)]

    def insert(self, user: User):
        shard = self._get_shard(user.id)
        shard.insert(user)

    def get(self, user_id: int) -> User | None:
        shard = self._get_shard(user_id)
        return shard.get(user_id)


# -----------------------------------------------------------------------------
# Strategy 2: Range-Based Sharding
# -----------------------------------------------------------------------------


class RangeShardRouter:
    """
    Routes based on value ranges.
    Easy to understand but can create uneven distribution.
    """

    def __init__(self, ranges: list[tuple[int, int, Shard]]):
        # List of (min_id, max_id, shard)
        self.ranges = ranges

    def _get_shard(self, user_id: int) -> Shard:
        for min_id, max_id, shard in self.ranges:
            if min_id <= user_id <= max_id:
                return shard
        raise ValueError(f"No shard for user_id: {user_id}")

    def insert(self, user: User):
        shard = self._get_shard(user.id)
        shard.insert(user)

    def get(self, user_id: int) -> User | None:
        shard = self._get_shard(user_id)
        return shard.get(user_id)


# -----------------------------------------------------------------------------
# Strategy 3: Directory-Based Sharding
# -----------------------------------------------------------------------------


class DirectoryShardRouter:
    """
    Uses a lookup table to map keys to shards.
    Most flexible but adds an extra lookup step.
    """

    def __init__(self, shards: list[Shard]):
        self.shards = {s.name: s for s in shards}
        self.directory: dict[int, str] = {}  # user_id → shard_name

    def _select_shard(self, user: User) -> Shard:
        """Select shard based on region (directory logic)."""
        region_to_shard = {
            "us": "Shard-US",
            "eu": "Shard-EU",
            "asia": "Shard-Asia",
        }
        shard_name = region_to_shard.get(user.region, "Shard-US")
        return self.shards[shard_name]

    def insert(self, user: User):
        shard = self._select_shard(user)
        self.directory[user.id] = shard.name
        shard.insert(user)

    def get(self, user_id: int) -> User | None:
        shard_name = self.directory.get(user_id)
        if not shard_name:
            return None
        return self.shards[shard_name].get(user_id)


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    users = [
        User(1, "Alice", "alice@example.com", "us"),
        User(2, "Bob", "bob@example.com", "eu"),
        User(3, "Charlie", "charlie@example.com", "us"),
        User(4, "Diana", "diana@example.com", "asia"),
        User(5, "Eve", "eve@example.com", "eu"),
        User(6, "Frank", "frank@example.com", "us"),
        User(7, "Grace", "grace@example.com", "asia"),
        User(8, "Hank", "hank@example.com", "eu"),
    ]

    # --- Hash-Based Sharding ---
    print("=" * 60)
    print("HASH-BASED SHARDING")
    print("=" * 60)

    shards = [Shard("Shard-0"), Shard("Shard-1"), Shard("Shard-2")]
    router = HashShardRouter(shards)

    print("\nInserting users:")
    for user in users:
        router.insert(user)

    print(
        f"\nShard distribution: {', '.join(f'{s.name}: {s.count()}' for s in shards)}"
    )

    print(f"\nLookup user 1: {router.get(1)}")
    print(f"Lookup user 5: {router.get(5)}")

    # --- Range-Based Sharding ---
    print("\n" + "=" * 60)
    print("RANGE-BASED SHARDING")
    print("=" * 60)

    range_shards = [Shard("Shard-A"), Shard("Shard-B")]
    range_router = RangeShardRouter(
        ranges=[
            (1, 4, range_shards[0]),  # IDs 1-4
            (5, 100, range_shards[1]),  # IDs 5-100
        ]
    )

    print("\nInserting users:")
    for user in users:
        range_router.insert(user)

    print(
        f"\nShard distribution: {', '.join(f'{s.name}: {s.count()}' for s in range_shards)}"
    )

    # --- Directory-Based Sharding ---
    print("\n" + "=" * 60)
    print("DIRECTORY-BASED SHARDING (by region)")
    print("=" * 60)

    dir_shards = [Shard("Shard-US"), Shard("Shard-EU"), Shard("Shard-Asia")]
    dir_router = DirectoryShardRouter(dir_shards)

    print("\nInserting users:")
    for user in users:
        dir_router.insert(user)

    print(
        f"\nShard distribution: {', '.join(f'{s.name}: {s.count()}' for s in dir_shards)}"
    )

    print(f"\nLookup user 1 (US): {dir_router.get(1)}")
    print(f"Lookup user 2 (EU): {dir_router.get(2)}")
    print(f"Lookup user 4 (Asia): {dir_router.get(4)}")


if __name__ == "__main__":
    main()
