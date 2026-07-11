# System Design - Content Delivery Network (CDN)
# -----------------------------------------------------------------------------
# A CDN is a distributed network of servers that delivers content to users
# from the server closest to them (edge server), reducing latency and
# offloading traffic from the origin server.
#
# Without CDN:
#
#   User (Tokyo) → Origin Server (New York) → Content
#   Latency: ~200ms+
#
# With CDN:
#
#   User (Tokyo) → Edge Server (Tokyo) → Content
#   Latency: ~20ms
#
# -----------------------------------------------------------------------------
# How It Works:
#
#   1. User requests a URL (e.g., image.png)
#   2. DNS resolves to the nearest CDN edge server
#   3. Edge server checks its cache (HIT or MISS)
#   4. HIT  → serve cached content immediately
#   5. MISS → fetch from origin, cache it, then serve
#
# -----------------------------------------------------------------------------
# Key Concepts:
#
# 1. Edge Server
#    - Sits close to users in different geographic regions
#    - Caches static content (images, CSS, JS, videos)
#
# 2. Cache Invalidation
#    - TTL (Time To Live): content expires after N seconds
#    - Purge: manually remove cached content
#    - Versioned URLs: static content gets a hash in the filename
#
# 3. Cache Hit Ratio
#    - % of requests served from cache vs origin
#    - Good CDNs target 90%+ hit ratio
#
# 4. Origin Server
#    - The source of truth for all content
#    - Only contacted on cache misses
#
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - Cloudflare, AWS CloudFront, Akamai, Fastly
# - Netflix (video CDN)
# - GitHub Pages (static site CDN)
# - Any website serving static assets at scale
# -----------------------------------------------------------------------------


import time
from dataclasses import dataclass, field
from typing import Any, Dict, Optional

# =============================================================================
# Content Object
# =============================================================================


@dataclass
class Content:
    url: str
    body: bytes
    content_type: str = "application/octet-stream"
    cached_at: float = field(default_factory=time.time)
    ttl: float = 3600.0  # seconds

    @property
    def is_expired(self) -> bool:
        return (time.time() - self.cached_at) > self.ttl


# =============================================================================
# Origin Server
# =============================================================================


class OriginServer:
    """
    Simulates the origin server that holds the actual content.
    In production this would be your S3 bucket, web server, etc.
    """

    def __init__(self):
        self._storage: Dict[str, Content] = {}
        self.request_count = 0

    def store(self, url: str, body: bytes, content_type: str = "text/html"):
        self._storage[url] = Content(url=url, body=body, content_type=content_type)

    def fetch(self, url: str) -> Optional[Content]:
        self.request_count += 1
        content = self._storage.get(url)
        if content:
            print(f"    [Origin] Serving '{url}' (request #{self.request_count})")
        else:
            print(f"    [Origin] 404 — '{url}' not found")
        return content


# =============================================================================
# Edge Server (CDN Cache Node)
# =============================================================================


class EdgeServer:
    """
    A single edge server that caches content and serves it to nearby users.
    """

    def __init__(self, region: str, origin: OriginServer):
        self.region = region
        self.origin = origin
        self._cache: Dict[str, Content] = {}
        self.hits = 0
        self.misses = 0

    def serve(self, url: str) -> Optional[Content]:
        # Check cache
        cached = self._cache.get(url)
        if cached and not cached.is_expired:
            self.hits += 1
            print(f"    [Edge:{self.region}] CACHE HIT for '{url}'")
            return cached

        # Cache miss — fetch from origin
        self.misses += 1
        print(f"    [Edge:{self.region}] CACHE MISS for '{url}' — fetching from origin")
        content = self.origin.fetch(url)
        if content:
            self._cache[url] = content
        return content

    def invalidate(self, url: str):
        if url in self._cache:
            del self._cache[url]
            print(f"    [Edge:{self.region}] Invalidated '{url}'")

    @property
    def hit_ratio(self) -> float:
        total = self.hits + self.misses
        return self.hits / total if total > 0 else 0.0


# =============================================================================
# CDN — manages multiple edge servers
# =============================================================================


class CDN:
    """
    Routes requests to the nearest edge server based on user region.
    Simulates DNS-based geographic routing.
    """

    def __init__(self, origin: OriginServer):
        self.origin = origin
        self.edges: Dict[str, EdgeServer] = {}

    def add_edge(self, region: str):
        self.edges[region] = EdgeServer(region, self.origin)
        print(f"  [CDN] Added edge server in '{region}'")

    def get_edge(self, region: str) -> EdgeServer:
        # Simple routing: return exact match or closest available
        if region in self.edges:
            return self.edges[region]
        # Fallback to first available edge
        return next(iter(self.edges.values()))

    def fetch(self, url: str, user_region: str) -> Optional[Content]:
        edge = self.get_edge(user_region)
        print(f"  [CDN] Routing user in '{user_region}' to edge '{edge.region}'")
        return edge.serve(url)

    def purge(self, url: str):
        for edge in self.edges.values():
            edge.invalidate(url)
        print(f"  [CDN] Purged '{url}' from all edges")

    def get_stats(self) -> Dict[str, Any]:
        stats = {}
        total_hits = 0
        total_misses = 0
        for region, edge in self.edges.items():
            stats[region] = {
                "hits": edge.hits,
                "misses": edge.misses,
                "hit_ratio": f"{edge.hit_ratio:.1%}",
            }
            total_hits += edge.hits
            total_misses += edge.misses
        total = total_hits + total_misses
        stats["overall"] = {
            "total_hits": total_hits,
            "total_misses": total_misses,
            "hit_ratio": f"{total_hits / total:.1%}" if total > 0 else "N/A",
            "origin_requests": self.origin.request_count,
        }
        return stats


# =============================================================================
# Usage
# =============================================================================


def main():
    # Setup origin
    origin = OriginServer()
    origin.store("/", b"<html>Home Page</html>", "text/html")
    origin.store("/style.css", b"body { margin: 0; }", "text/css")
    origin.store("/app.js", b"console.log('hello')", "application/javascript")
    origin.store("/logo.png", b"\x89PNG...", "image/png")

    # Setup CDN with regional edges
    cdn = CDN(origin)
    cdn.add_edge("us-east")
    cdn.add_edge("eu-west")
    cdn.add_edge("ap-south")

    # --- First request (cold cache) ---
    print("\n=== First request from Tokyo ===")
    cdn.fetch("/", "ap-south")

    print("\n=== First request from London ===")
    cdn.fetch("/", "eu-west")

    # --- Second request (cache warm) ---
    print("\n=== Second request from Tokyo (should hit cache) ===")
    cdn.fetch("/", "ap-south")

    print("\n=== Request different content ===")
    cdn.fetch("/style.css", "ap-south")
    cdn.fetch("/app.js", "eu-west")
    cdn.fetch("/logo.png", "us-east")

    # --- Repeat requests (all should hit cache) ---
    print("\n=== Repeated requests ===")
    cdn.fetch("/", "ap-south")
    cdn.fetch("/", "eu-west")
    cdn.fetch("/", "us-east")
    cdn.fetch("/style.css", "ap-south")

    # --- Cache purge ---
    print("\n=== Purge /style.css and re-fetch ===")
    cdn.purge("/style.css")
    cdn.fetch("/style.css", "ap-south")

    # --- Stats ---
    print("\n=== CDN Stats ===")
    stats = cdn.get_stats()
    for region, info in stats.items():
        if region == "overall":
            print("\n  Overall:")
            print(f"    Cache hits:   {info['total_hits']}")
            print(f"    Cache misses: {info['total_misses']}")
            print(f"    Hit ratio:    {info['hit_ratio']}")
            print(f"    Origin requests: {info['origin_requests']}")
        else:
            print(f"\n  {region}:")
            print(
                f"    Hits: {info['hits']}, Misses: {info['misses']}, Ratio: {info['hit_ratio']}"
            )


if __name__ == "__main__":
    main()
