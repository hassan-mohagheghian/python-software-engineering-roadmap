# System Design - Caching System
# -----------------------------------------------------------------------------
# A caching system stores frequently accessed data in fast storage (memory)
# to reduce database load and improve response time.
#
# -----------------------------------------------------------------------------
# Why caching is used:
#
# - Reduce latency (faster responses)
# - Reduce database load
# - Improve scalability
#
# -----------------------------------------------------------------------------
# High-level flow:
#
# Client → Cache → Database (if cache miss)
#
# -----------------------------------------------------------------------------

import time

# -----------------------------------------------------------------------------
# Database (slow storage simulation)
# -----------------------------------------------------------------------------


class Database:
    def __init__(self):
        self.storage = {
            "user:1": {"id": 1, "name": "Alice"},
            "user:2": {"id": 2, "name": "Bob"},
        }

    def get(self, key: str):
        print("[DB] Querying database...")
        time.sleep(1)  # simulate slow DB
        return self.storage.get(key)


# -----------------------------------------------------------------------------
# Cache (fast in-memory storage)
# -----------------------------------------------------------------------------


class Cache:
    def __init__(self):
        self.store = {}

    def get(self, key: str):
        return self.store.get(key)

    def set(self, key: str, value):
        self.store[key] = value


# -----------------------------------------------------------------------------
# Application Service (Cache-Aside Pattern)
# -----------------------------------------------------------------------------


class UserService:
    def __init__(self, cache: Cache, db: Database):
        self.cache = cache
        self.db = db

    def get_user(self, user_id: int):
        key = f"user:{user_id}"

        # 1. Check cache first
        cached = self.cache.get(key)
        if cached:
            print("[CACHE] Hit")
            return cached

        print("[CACHE] Miss")

        # 2. Fetch from database
        user = self.db.get(key)

        if user:
            # 3. Store in cache for future requests
            self.cache.set(key, user)

        return user


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    cache = Cache()
    db = Database()

    service = UserService(cache, db)

    print(service.get_user(1))  # cache miss → DB
    print(service.get_user(1))  # cache hit → fast
    print(service.get_user(2))  # cache miss → DB


if __name__ == "__main__":
    main()
