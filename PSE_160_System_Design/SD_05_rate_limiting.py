# System Design - Rate Limiting System
# -----------------------------------------------------------------------------
# A rate limiting system controls how many requests a user can send
# within a specific time window.
#
# -----------------------------------------------------------------------------
# Why it is used:
#
# - Prevent API abuse
# - Protect backend services from overload
# - Ensure fair usage across users
#
# -----------------------------------------------------------------------------

import time
from collections import defaultdict

# -----------------------------------------------------------------------------
# Token Bucket (simple implementation)
# -----------------------------------------------------------------------------


class TokenBucket:
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_time = time.time()

    def _refill(self):
        now = time.time()
        elapsed = now - self.last_time

        # refill tokens based on time passed
        self.tokens += elapsed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens)

        self.last_time = now

    def allow_request(self) -> bool:
        self._refill()

        if self.tokens >= 1:
            self.tokens -= 1
            return True

        return False


# -----------------------------------------------------------------------------
# Rate Limiter (per user)
# -----------------------------------------------------------------------------


class RateLimiter:
    def __init__(self, capacity: int, refill_rate: float):
        self.users = defaultdict(lambda: TokenBucket(capacity, refill_rate))

    def allow(self, user_id: str) -> bool:
        return self.users[user_id].allow_request()


# -----------------------------------------------------------------------------
# Usage Example
# -----------------------------------------------------------------------------


def main():
    limiter = RateLimiter(capacity=3, refill_rate=1)  # burst=3, refill=1/sec

    user_id = "user_1"

    for i in range(10):
        if limiter.allow(user_id):
            print(f"[ALLOWED] request {i+1}")
        else:
            print(f"[BLOCKED] request {i+1}")

        time.sleep(0.3)


if __name__ == "__main__":
    main()
