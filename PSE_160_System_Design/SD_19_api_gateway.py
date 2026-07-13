# System Design - API Gateway
# -----------------------------------------------------------------------------
# An API Gateway is a single entry point for all client requests in a
# microservices architecture. It handles cross-cutting concerns like
# routing, authentication, rate limiting, and request transformation.
#
# Without API Gateway:
#
#   Client → Auth Service
#          → User Service
#          → Order Service
#          → Payment Service
#
#   Problems: Client must know every service address, handles auth itself,
#             no centralized rate limiting, tight coupling.
#
# With API Gateway:
#
#   Client → API Gateway → Auth Service
#                        → User Service
#                        → Order Service
#                        → Payment Service
#
#   Benefits: Single entry point, centralized auth, rate limiting,
#             request aggregation, protocol translation.
#
# -----------------------------------------------------------------------------
# Key Responsibilities:
#
# 1. Request Routing
#    - Maps external URLs to internal service endpoints
#    - /api/users → user-service:8080/users
#    - /api/orders → order-service:8080/orders
#
# 2. Authentication & Authorization
#    - Validates JWT tokens before forwarding
#    - Injects user context into downstream requests
#
# 3. Rate Limiting
#    - Protects backend services from overload
#    - Per-user, per-IP, or per-API-key limits
#
# 4. Request/Response Transformation
#    - Aggregates multiple service calls into one response
#    - Translates protocols (HTTP ↔ gRPC)
#    - Renames fields for API versioning
#
# 5. Load Balancing
#    - Distributes requests across service instances
#
# 6. Circuit Breaking
#    - Prevents cascade failures when a service is down
#
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - AWS API Gateway, Kong, Zuul, Envoy
# - Nginx as API Gateway (with Lua scripting)
# - Cloudflare Workers (edge API Gateway)
# - Netflix Zuul (pioneered the pattern)
# -----------------------------------------------------------------------------


import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

# =============================================================================
# Request / Response
# =============================================================================


@dataclass
class Request:
    method: str
    path: str
    headers: Dict[str, str] = field(default_factory=dict)
    body: str = ""
    user_id: Optional[str] = None


@dataclass
class Response:
    status_code: int
    body: Any
    headers: Dict[str, str] = field(default_factory=dict)


# =============================================================================
# Route
# =============================================================================


@dataclass
class Route:
    method: str
    path_prefix: str
    target_service: str
    target_path: str
    requires_auth: bool = True
    rate_limit: Optional[int] = None  # requests per minute


# =============================================================================
# Service Registry
# =============================================================================


class ServiceRegistry:
    """
    Tracks available services and their instances.
    In production this would be Consul, etcd, or Eureka.
    """

    def __init__(self):
        self._services: Dict[str, List[str]] = {}

    def register(self, service_name: str, address: str):
        if service_name not in self._services:
            self._services[service_name] = []
        self._services[service_name].append(address)
        print(f"  [Registry] Registered {service_name} → {address}")

    def get_instances(self, service_name: str) -> List[str]:
        return self._services.get(service_name, [])

    def deregister(self, service_name: str, address: str):
        if service_name in self._services:
            self._services[service_name].remove(address)


# =============================================================================
# JWT Token Validator (simplified)
# =============================================================================


class TokenValidator:
    """Simplified JWT validation — checks token presence and extracts user_id."""

    def __init__(self):
        self.valid_tokens: Dict[str, str] = {}  # token → user_id

    def issue_token(self, user_id: str) -> str:
        token = f"jwt_{user_id}_{int(time.time())}"
        self.valid_tokens[token] = user_id
        return token

    def validate(self, token: str) -> Optional[str]:
        """Returns user_id if valid, None otherwise."""
        return self.valid_tokens.get(token)


# =============================================================================
# Rate Limiter
# =============================================================================


class RateLimiter:
    """
    Token bucket rate limiter. Each key gets a fixed number of tokens
    that replenish over time.
    """

    def __init__(self, max_tokens: int = 100, refill_rate: float = 10.0):
        self.max_tokens = max_tokens
        self.refill_rate = refill_rate  # tokens per second
        self._buckets: Dict[str, Dict[str, Any]] = {}

    def allow(self, key: str) -> bool:
        now = time.time()
        if key not in self._buckets:
            self._buckets[key] = {"tokens": self.max_tokens, "last_refill": now}

        bucket = self._buckets[key]
        elapsed = now - bucket["last_refill"]
        bucket["tokens"] = min(
            self.max_tokens, bucket["tokens"] + elapsed * self.refill_rate
        )
        bucket["last_refill"] = now

        if bucket["tokens"] >= 1:
            bucket["tokens"] -= 1
            return True
        return False


# =============================================================================
# API Gateway
# =============================================================================


class APIGateway:
    """
    Central API Gateway that routes requests to backend services.
    Handles auth, rate limiting, routing, and load balancing.
    """

    def __init__(self, registry: ServiceRegistry):
        self.registry = registry
        self.routes: List[Route] = []
        self.auth = TokenValidator()
        self.rate_limiter = RateLimiter(max_tokens=10, refill_rate=2.0)
        self.request_count = 0

    def add_route(self, route: Route):
        self.routes.append(route)

    def _match_route(self, method: str, path: str) -> Optional[Route]:
        for route in self.routes:
            if route.method == method and path.startswith(route.path_prefix):
                return route
        return None

    def _load_balance(self, service_name: str) -> Optional[str]:
        instances = self.registry.get_instances(service_name)
        if not instances:
            return None
        # Simple round-robin
        self.request_count += 1
        return instances[self.request_count % len(instances)]

    def handle(self, request: Request) -> Response:
        """Process a request through the gateway."""
        print(f"\n  [Gateway] {request.method} {request.path}")

        # 1. Match route
        route = self._match_route(request.method, request.path)
        if not route:
            print(f"  [Gateway] 404 — no route for {request.method} {request.path}")
            return Response(404, {"error": "Route not found"})

        # 2. Authenticate if required
        if route.requires_auth:
            token = request.headers.get("Authorization", "")
            user_id = self.auth.validate(token)
            if not user_id:
                print("  [Gateway] 401 — invalid or missing token")
                return Response(401, {"error": "Unauthorized"})
            request.user_id = user_id
            print(f"  [Gateway] Auth OK — user={user_id}")

        # 3. Rate limit
        if route.rate_limit:
            key = request.user_id or "anonymous"
            if not self.rate_limiter.allow(key):
                print(f"  [Gateway] 429 — rate limit exceeded for {key}")
                return Response(429, {"error": "Rate limit exceeded"})

        # 4. Load balance
        instance = self._load_balance(route.target_service)
        if not instance:
            print(f"  [Gateway] 503 — no instances for {route.target_service}")
            return Response(503, {"error": "Service unavailable"})

        # 5. Forward to service (simulated)
        target_path = route.target_path + request.path[len(route.path_prefix) :]
        print(f"  [Gateway] Forwarding → {instance}{target_path}")
        return Response(
            200,
            {
                "service": route.target_service,
                "instance": instance,
                "path": target_path,
                "user": request.user_id,
            },
        )


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=" * 65)
    print("API GATEWAY — Central Entry Point for Microservices")
    print("=" * 65)

    # Setup
    registry = ServiceRegistry()
    registry.register("user-service", "10.0.1.1:8080")
    registry.register("user-service", "10.0.1.2:8080")
    registry.register("order-service", "10.0.2.1:8080")
    registry.register("payment-service", "10.0.3.1:8080")

    gateway = APIGateway(registry)
    gateway.add_route(Route("GET", "/api/users", "user-service", "/users"))
    gateway.add_route(Route("POST", "/api/orders", "order-service", "/orders"))
    gateway.add_route(
        Route("POST", "/api/payments", "payment-service", "/payments", rate_limit=5)
    )

    # Issue tokens
    alice_token = gateway.auth.issue_token("alice")
    bob_token = gateway.auth.issue_token("bob")

    # --- 1. Authenticated request ---
    print("\n" + "-" * 65)
    print("1. Authenticated request (Alice → users)")
    print("-" * 65)
    resp = gateway.handle(
        Request("GET", "/api/users/42", {"Authorization": alice_token})
    )
    print(f"  Response: {resp.status_code} {resp.body}")

    # --- 2. Unauthenticated request ---
    print("\n" + "-" * 65)
    print("2. Unauthenticated request (no token)")
    print("-" * 65)
    resp = gateway.handle(Request("GET", "/api/users/42"))
    print(f"  Response: {resp.status_code} {resp.body}")

    # --- 3. Rate limiting ---
    print("\n" + "-" * 65)
    print("3. Rate limiting (Bob hits payment endpoint rapidly)")
    print("-" * 65)
    for i in range(4):
        resp = gateway.handle(
            Request("POST", "/api/payments", {"Authorization": bob_token})
        )
        print(f"  Request {i + 1}: {resp.status_code}")

    # --- 4. Load balancing ---
    print("\n" + "-" * 65)
    print("4. Load balancing (multiple requests to user-service)")
    print("-" * 65)
    for i in range(4):
        resp = gateway.handle(
            Request("GET", "/api/users", {"Authorization": alice_token})
        )
        print(f"  Request {i + 1}: instance={resp.body.get('instance')}")

    # --- 5. Unknown route ---
    print("\n" + "-" * 65)
    print("5. Unknown route")
    print("-" * 65)
    resp = gateway.handle(Request("GET", "/api/unknown"))
    print(f"  Response: {resp.status_code} {resp.body}")

    # --- Summary ---
    print("\n" + "=" * 65)
    print("SUMMARY — API Gateway Responsibilities")
    print("=" * 65)
    print("""
  Responsibility        What it does
  ----------------      ------------
  Routing               Maps external paths to internal services
  Authentication        Validates tokens before forwarding
  Rate Limiting         Protects services from overload
  Load Balancing        Distributes across service instances
  Request Transformation Aggregates, renames, translates protocols
  Circuit Breaking      Prevents cascade failures

  Trade-offs:
  + Single entry point simplifies client code
  + Centralized cross-cutting concerns (auth, logging)
  + Decouples clients from service topology
  - Single point of failure (must be highly available)
  - Adds latency (extra hop)
  - Can become a bottleneck if not scaled properly

  Real-world: Kong, AWS API Gateway, Netflix Zuul, Envoy, Nginx
""")


if __name__ == "__main__":
    main()
