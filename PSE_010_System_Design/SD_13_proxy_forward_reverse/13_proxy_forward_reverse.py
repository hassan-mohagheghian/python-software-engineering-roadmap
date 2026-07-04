# System Design: Proxy Patterns — Forward (Outbound) vs Reverse (Inbound)
# -----------------------------------------------------------------------------
# A proxy is an intermediary server that sits between clients and backend
# servers, forwarding requests and responses.
#
# -----------------------------------------------------------------------------
# Forward Proxy (Client-Side Proxy):
#
#   Client → Forward Proxy → Internet → Server
#
#   - Client knows it's using a proxy
#   - Server doesn't know the real client
#   - Used for: anonymity, access control, caching, logging
#
# -----------------------------------------------------------------------------
# Reverse Proxy (Server-Side Proxy):
#
#   Client → Internet → Reverse Proxy → Backend Servers
#
#   - Client doesn't know about backend servers
#   - Server knows the proxy, not the real client (usually)
#   - Used for: load balancing, SSL termination, caching, security
#
# -----------------------------------------------------------------------------
# Key differences:
#
#                    Forward Proxy          Reverse Proxy
#   Protects:        Client                 Server
#   Client aware:    Yes                    No
#   Server aware:    No (usually)           Yes
#   Location:        Client side            Server side
#
# -----------------------------------------------------------------------------
# Real-world examples:
#
# Forward Proxy:
#   - Corporate proxy for internet access
#   - VPN services
#   - Content filtering
#
# Reverse Proxy:
#   - Nginx, HAProxy, Traefik
#   - AWS ALB / Cloudflare
#   - API Gateway
# -----------------------------------------------------------------------------

import time
from dataclasses import dataclass, field

# -----------------------------------------------------------------------------
# Request / Response Models
# -----------------------------------------------------------------------------


@dataclass
class Request:
    method: str
    path: str
    headers: dict[str, str] = field(default_factory=dict)
    body: str = ""
    client_ip: str = "unknown"


@dataclass
class Response:
    status: int
    body: str
    headers: dict[str, str] = field(default_factory=dict)


# -----------------------------------------------------------------------------
# Backend Server
# -----------------------------------------------------------------------------


class BackendServer:
    def __init__(self, name: str, host: str):
        self.name = name
        self.host = host
        self.request_count = 0

    def handle(self, request: Request) -> Response:
        self.request_count += 1
        return Response(
            status=200,
            body=f"Hello from {self.name} | Path: {request.path} | "
            f"Total requests: {self.request_count}",
            headers={"X-Backend": self.name},
        )


# -----------------------------------------------------------------------------
# Forward Proxy
# -----------------------------------------------------------------------------


class ForwardProxy:
    """
    Sits between client and internet.
    Hides client identity from the server.
    Can log, filter, or cache requests.
    """

    def __init__(self):
        self.access_log: list[dict] = []
        self.blocked_domains: set[str] = set()

    def block_domain(self, domain: str):
        self.blocked_domains.add(domain)

    def forward(self, request: Request, target_server: BackendServer) -> Response:
        # Log the request
        self.access_log.append(
            {
                "client": request.client_ip,
                "path": request.path,
                "time": time.time(),
            }
        )

        # Check if domain is blocked
        for domain in self.blocked_domains:
            if domain in request.path:
                return Response(status=403, body=f"Blocked: {domain}")

        # Hide client identity
        anonymized_request = Request(
            method=request.method,
            path=request.path,
            headers={**request.headers, "X-Forwarded-For": "hidden"},
            body=request.body,
            client_ip="proxy-anonymous",
        )

        print(
            f"  [ForwardProxy] {request.client_ip} → {target_server.name}: {request.path}"
        )
        return target_server.handle(anonymized_request)


# -----------------------------------------------------------------------------
# Reverse Proxy with Load Balancing
# -----------------------------------------------------------------------------


class ReverseProxy:
    """
    Sits in front of backend servers.
    Client doesn't know which backend handles the request.
    Provides load balancing, caching, and security.
    """

    def __init__(self):
        self.backends: list[BackendServer] = []
        self._current = 0  # Round-robin counter
        self._cache: dict[str, Response] = {}
        self.cache_enabled = True

    def add_backend(self, server: BackendServer):
        self.backends.append(server)

    def _select_backend(self) -> BackendServer:
        """Round-robin load balancing."""
        server = self.backends[self._current]
        self._current = (self._current + 1) % len(self.backends)
        return server

    def handle(self, request: Request) -> Response:
        # Check cache for GET requests
        if self.cache_enabled and request.method == "GET":
            cache_key = f"{request.method}:{request.path}"
            if cache_key in self._cache:
                print(f"  [ReverseProxy] Cache hit: {request.path}")
                return self._cache[cache_key]

        # Select backend (load balancing)
        backend = self._select_backend()
        print(f"  [ReverseProxy] Routing to {backend.name}: {request.path}")

        # Add proxy headers
        proxied_request = Request(
            method=request.method,
            path=request.path,
            headers={
                **request.headers,
                "X-Real-IP": request.client_ip,
                "X-Forwarded-Host": request.headers.get("Host", "unknown"),
            },
            body=request.body,
            client_ip=request.client_ip,
        )

        # Forward to backend
        response = backend.handle(proxied_request)

        # Add proxy headers to response
        response.headers["X-Proxy"] = "ReverseProxy"
        response.headers["X-Backend"] = backend.name

        # Cache GET responses
        if self.cache_enabled and request.method == "GET":
            cache_key = f"{request.method}:{request.path}"
            self._cache[cache_key] = response

        return response


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    # --- Forward Proxy ---
    print("=" * 60)
    print("FORWARD PROXY")
    print("=" * 60)

    proxy = ForwardProxy()
    proxy.block_domain("ads.example.com")

    server = BackendServer("WebServer", "example.com")

    # Normal request
    req1 = Request(method="GET", path="/api/data", client_ip="192.168.1.10")
    resp1 = proxy.forward(req1, server)
    print(f"  Response: {resp1.body}\n")

    # Blocked request
    req2 = Request(
        method="GET", path="https://ads.example.com/banner", client_ip="192.168.1.10"
    )
    resp2 = proxy.forward(req2, server)
    print(f"  Response: [{resp2.status}] {resp2.body}\n")

    print(f"  Access log: {len(proxy.access_log)} entries")

    # --- Reverse Proxy ---
    print("\n" + "=" * 60)
    print("REVERSE PROXY WITH LOAD BALANCING")
    print("=" * 60)

    reverse_proxy = ReverseProxy()
    reverse_proxy.add_backend(BackendServer("Backend-1", "10.0.0.1"))
    reverse_proxy.add_backend(BackendServer("Backend-2", "10.0.0.2"))
    reverse_proxy.add_backend(BackendServer("Backend-3", "10.0.0.3"))

    # Multiple requests show round-robin distribution
    for i in range(3):
        req = Request(
            method="GET",
            path=f"/api/users/{i + 1}",
            headers={"Host": "api.example.com"},
            client_ip="203.0.113.50",
        )
        resp = reverse_proxy.handle(req)
        print(f"  Response: {resp.body}")
        print(f"  Headers: {resp.headers}\n")

    for i in range(6):
        req = Request(
            method="GET",
            path=f"/api/users/{i + 1}",
            headers={"Host": "api.example.com"},
            client_ip="203.0.113.50",
        )
        resp = reverse_proxy.handle(req)
        print(f"  Response: {resp.body}")
        print(f"  Headers: {resp.headers}\n")


if __name__ == "__main__":
    main()
