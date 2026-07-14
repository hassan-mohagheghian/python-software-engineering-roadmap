# System Design - Circuit Breaker
# -----------------------------------------------------------------------------
# A Circuit Breaker is a fault tolerance pattern that prevents cascade
# failures when a downstream service is slow or unavailable.
#
# Without Circuit Breaker:
#
#   Service A → Service B (slow/down) → A waits → A's threads blocked
#                                           → A can't serve other clients
#                                           → Service A goes down too
#                                           → Cascade failure across system
#
# With Circuit Breaker:
#
#   Service A → [Circuit Breaker] → Service B
#                 │
#                 ├─ CLOSED (normal): requests go through
#                 ├─ OPEN (failing): requests fail immediately
#                 └─ HALF-OPEN (testing): limited requests to test recovery
#
# -----------------------------------------------------------------------------
# Three States:
#
#   CLOSED → Normal operation
#     - Requests pass through to the service
#     - Failures are counted
#     - If failures exceed threshold → transition to OPEN
#
#   OPEN → Circuit is broken
#     - Requests fail immediately (no call to service)
#     - After timeout → transition to HALF-OPEN
#
#   HALF-OPEN → Testing recovery
#     - Limited number of test requests go through
#     - If they succeed → transition to CLOSED
#     - If they fail → transition back to OPEN
#
# -----------------------------------------------------------------------------
# State Diagram:
#
#              failure threshold reached
#   CLOSED ──────────────────────────▶ OPEN
#     ▲                                  │
#     │          test succeeds           │ timeout expires
#     └────────────── ◀────────── HALF-OPEN
#                          │
#                          └── test fails ──▶ OPEN
#
# -----------------------------------------------------------------------------
# Key Configuration:
#
#   failure_threshold: Number of failures before opening circuit
#   recovery_timeout: Seconds to wait before trying again
#   success_threshold: Successes in half-open state to close circuit
#   timeout: Max wait time for a single request
#
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - Netflix Hystrix (pioneered the pattern, now deprecated)
# - Resilience4j (Java successor to Hystrix)
# - Polly (.NET resilience library)
# - Istio service mesh (automatic circuit breaking)
# - AWS ALB health checks (implicit circuit breaking)
# -----------------------------------------------------------------------------


import time
from enum import Enum
from typing import Any, Callable, Dict, Optional

# =============================================================================
# Circuit State
# =============================================================================


class CircuitState(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"


# =============================================================================
# Circuit Breaker
# =============================================================================


class CircuitBreaker:
    """
    Implements the Circuit Breaker pattern with three states:
    CLOSED (normal), OPEN (failing), HALF-OPEN (testing).
    """

    def __init__(
        self,
        name: str = "default",
        failure_threshold: int = 3,
        recovery_timeout: float = 5.0,
        success_threshold: int = 2,
    ):
        self.name = name
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.success_threshold = success_threshold

        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time: Optional[float] = None
        self.total_requests = 0
        self.total_failures = 0
        self.total_successes = 0
        self.total_rejected = 0

    def _log(self, message: str):
        print(f"    [{self.name}] {message}")

    def call(self, func: Callable, *args, **kwargs) -> Any:
        """
        Execute a function through the circuit breaker.
        Raises CircuitOpenError if circuit is open.
        """
        self.total_requests += 1

        # --- OPEN state: reject immediately ---
        if self.state == CircuitState.OPEN:
            if self._should_attempt_reset():
                self._log("Timeout expired → entering HALF-OPEN")
                self.state = CircuitState.HALF_OPEN
                self.success_count = 0
            else:
                self.total_rejected += 1
                raise CircuitOpenError(
                    f"Circuit '{self.name}' is OPEN — request rejected"
                )

        # --- HALF-OPEN state: allow limited requests ---
        if self.state == CircuitState.HALF_OPEN:
            self._log("HALF-OPEN — testing recovery...")

        # --- Execute the call ---
        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise

    def _on_success(self):
        self.total_successes += 1
        self.failure_count = 0

        if self.state == CircuitState.HALF_OPEN:
            self.success_count += 1
            if self.success_count >= self.success_threshold:
                self._log(
                    f"Recovery confirmed ({self.success_count} successes) → CLOSED"
                )
                self.state = CircuitState.CLOSED
        elif self.state == CircuitState.CLOSED:
            self._log("Request succeeded")

    def _on_failure(self):
        self.total_failures += 1
        self.failure_count += 1
        self.last_failure_time = time.time()

        if self.state == CircuitState.HALF_OPEN:
            self._log("Test failed in HALF-OPEN → back to OPEN")
            self.state = CircuitState.OPEN
        elif self.failure_count >= self.failure_threshold:
            self._log(
                f"Failure threshold reached ({self.failure_count}/{self.failure_threshold}) → OPEN"
            )
            self.state = CircuitState.OPEN
        else:
            self._log(f"Failure {self.failure_count}/{self.failure_threshold}")

    def _should_attempt_reset(self) -> bool:
        if self.last_failure_time is None:
            return True
        return (time.time() - self.last_failure_time) >= self.recovery_timeout

    def get_state(self) -> Dict[str, Any]:
        return {
            "state": self.state.value,
            "failure_count": self.failure_count,
            "success_count": self.success_count,
            "total_requests": self.total_requests,
            "total_successes": self.total_successes,
            "total_failures": self.total_failures,
            "total_rejected": self.total_rejected,
        }


class CircuitOpenError(Exception):
    pass


# =============================================================================
# External Service (simulated)
# =============================================================================


class ExternalService:
    """Simulates an external service that can be healthy or failing."""

    def __init__(self, name: str, fail_rate: float = 0.0):
        self.name = name
        self.fail_rate = fail_rate
        self.call_count = 0
        self._is_down = False

    def call(self, query: str) -> str:
        self.call_count += 1

        if self._is_down:
            raise ConnectionError(f"{self.name} is DOWN")

        import random

        if random.random() < self.fail_rate:
            raise ConnectionError(f"{self.name} timeout on query '{query}'")

        return f"{self.name} response for '{query}'"

    def set_down(self, is_down: bool):
        self._is_down = is_down


# =============================================================================
# Usage
# =============================================================================


def main():
    import random

    random.seed(42)

    print("=" * 65)
    print("CIRCUIT BREAKER — Preventing Cascade Failures")
    print("=" * 65)

    # --- 1. Normal operation (CLOSED) ---
    print("\n" + "-" * 65)
    print("1. NORMAL OPERATION — Circuit CLOSED")
    print("   All requests pass through")
    print("-" * 65)

    service = ExternalService("Payment-API", fail_rate=0.0)
    cb = CircuitBreaker("Payment", failure_threshold=3, recovery_timeout=2.0)

    for i in range(3):
        try:
            result = cb.call(service.call, "charge")
            print(f"  Request {i + 1}: {result}")
        except CircuitOpenError as e:
            print(f"  Request {i + 1}: REJECTED — {e}")

    # --- 2. Failures → OPEN ---
    print("\n" + "-" * 65)
    print("2. FAILURES — Circuit transitions to OPEN")
    print("   After 3 failures, circuit opens and rejects requests")
    print("-" * 65)

    service.set_down(True)
    for i in range(5):
        try:
            result = cb.call(service.call, "charge")
            print(f"  Request {i + 1}: {result}")
        except CircuitOpenError as e:
            print(f"  Request {i + 1}: REJECTED — {e}")
        except ConnectionError as e:
            print(f"  Request {i + 1}: FAILED — {e}")

    # --- 3. OPEN state rejects immediately ---
    print("\n" + "-" * 65)
    print("3. OPEN STATE — Requests rejected immediately (no call made)")
    print("-" * 65)

    for i in range(3):
        try:
            result = cb.call(service.call, "charge")
            print(f"  Request {i + 1}: {result}")
        except CircuitOpenError as e:
            print(f"  Request {i + 1}: REJECTED — {e}")

    # --- 4. Recovery → HALF-OPEN → CLOSED ---
    print("\n" + "-" * 65)
    print("4. RECOVERY — Service comes back, circuit tests and closes")
    print("-" * 65)

    print("\n  Waiting for recovery timeout...")
    time.sleep(2.1)
    service.set_down(False)

    for i in range(5):
        try:
            result = cb.call(service.call, "charge")
            print(f"  Request {i + 1}: {result}")
        except CircuitOpenError as e:
            print(f"  Request {i + 1}: REJECTED — {e}")
        except ConnectionError as e:
            print(f"  Request {i + 1}: FAILED — {e}")

    # --- 5. Stats ---
    print("\n" + "-" * 65)
    print("5. CIRCUIT BREAKER STATS")
    print("-" * 65)

    state = cb.get_state()
    for key, value in state.items():
        print(f"  {key}: {value}")

    # --- Summary ---
    print("\n" + "=" * 65)
    print("SUMMARY — Circuit Breaker")
    print("=" * 65)
    print("""
  State        Behavior                    Transition to
  -----        --------                    -------------
  CLOSED       Requests pass through       → OPEN (failure threshold)
  OPEN         Requests rejected           → HALF-OPEN (timeout)
  HALF-OPEN    Test requests pass through  → CLOSED (successes)
                                        → OPEN (failure)

  Configuration:
  - failure_threshold: failures before opening (default: 3-5)
  - recovery_timeout: seconds before testing (default: 10-60s)
  - success_threshold: successes to close (default: 1-3)

  Benefits:
  + Prevents cascade failures
  + Fails fast (no waiting on dead service)
  + Self-healing (automatic recovery)
  + Provides fallback opportunity

  Real-world: Hystrix, Resilience4j, Polly, Istio, Envoy
""")


if __name__ == "__main__":
    main()
