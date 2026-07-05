# System Design - URL Shortener
# -----------------------------------------------------------------------------
# A URL Shortener converts long URLs into short, fixed-length aliases.
# When a user visits the short URL, the system redirects to the original.
#
# This is a classic system design problem that combines:
# - Hashing / ID generation
# - Database storage
# - Caching for hot URLs
# - Collision handling
#
# -----------------------------------------------------------------------------
# Core Flow:
#
#   Shorten:  Long URL → Generate Short Key → Store (key → url) → Return key
#   Redirect: Short Key → Lookup → Redirect to Long URL
#
# -----------------------------------------------------------------------------
# Key Design Decisions:
#
# 1. Key Generation
#    - Hash-based: MD5/SHA256 of URL, take first N chars
#    - Counter-based: auto-increment ID, encode in base62
#    - Random: generate random alphanumeric string
#
# 2. Collision Handling
#    - Check if key exists before storing
#    - Append a salt and re-hash if collision occurs
#
# 3. Read-Heavy System
#    - Reads (redirects) >> Writes (shorten)
#    - Cache popular URLs in memory
#
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - bit.ly, tinyurl.com, t.co (Twitter)
# - Short links in marketing campaigns
# - QR code friendly URLs
# -----------------------------------------------------------------------------

import string

# -----------------------------------------------------------------------------
# Base62 Encoding (a-z, A-Z, 0-9 = 62 characters)
# -----------------------------------------------------------------------------

BASE62_CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits


def encode_base62(num: int) -> str:
    """Convert an integer to a base62 string."""
    if num == 0:
        return BASE62_CHARS[0]

    result = []
    while num > 0:
        result.append(BASE62_CHARS[num % 62])
        num //= 62

    return "".join(reversed(result))


# -----------------------------------------------------------------------------
# Database (simulated)
# -----------------------------------------------------------------------------


class URLDatabase:
    def __init__(self):
        self._store: dict[str, str] = {}
        self._counter = 100000  # Starting counter for base62 encoding

    def save(self, short_key: str, long_url: str):
        self._store[short_key] = long_url
        print(f"  [DB] Stored: {short_key} → {long_url}")

    def get(self, short_key: str) -> str | None:
        return self._store.get(short_key)

    def exists(self, short_key: str) -> bool:
        return short_key in self._store

    def next_id(self) -> int:
        self._counter += 1
        return self._counter


# -----------------------------------------------------------------------------
# Cache (simulates Redis / Memcached)
# -----------------------------------------------------------------------------


class URLCache:
    def __init__(self, max_size: int = 100):
        self._store: dict[str, str] = {}
        self._hits = 0
        self._misses = 0
        self._max_size = max_size

    def get(self, key: str) -> str | None:
        value = self._store.get(key)
        if value:
            self._hits += 1
            print(f"  [CACHE] Hit for: {key}")
        else:
            self._misses += 1
        return value

    def set(self, key: str, value: str):
        if len(self._store) >= self._max_size:
            # Evict oldest entry (simple FIFO for demo)
            oldest = next(iter(self._store))
            del self._store[oldest]
        self._store[key] = value

    def stats(self) -> dict:
        total = self._hits + self._misses
        rate = (self._hits / total * 100) if total > 0 else 0
        return {"hits": self._hits, "misses": self._misses, "hit_rate": f"{rate:.1f}%"}


# -----------------------------------------------------------------------------
# URL Shortener Service
# -----------------------------------------------------------------------------


class URLShortener:
    def __init__(
        self, db: URLDatabase, cache: URLCache, base_url: str = "https://sho.rt"
    ):
        self.db = db
        self.cache = cache
        self.base_url = base_url

    def shorten(self, long_url: str) -> str:
        """Create a short URL for the given long URL."""
        # Generate short key using counter-based approach
        url_id = self.db.next_id()
        short_key = encode_base62(url_id)

        # Handle collision (unlikely with counter, but shown for completeness)
        while self.db.exists(short_key):
            url_id = self.db.next_id()
            short_key = encode_base62(url_id)

        # Store in database
        self.db.save(short_key, long_url)

        # Pre-populate cache
        self.cache.set(short_key, long_url)

        return f"{self.base_url}/{short_key}"

    def redirect(self, short_url: str) -> str | None:
        """Resolve a short URL to its original long URL."""
        # Extract key from URL
        short_key = short_url.split("/")[-1]

        # 1. Check cache first
        long_url = self.cache.get(short_key)
        if long_url:
            return long_url

        # 2. Query database
        print(f"  [CACHE] Miss for: {short_key}")
        long_url = self.db.get(short_key)
        if long_url:
            # Populate cache for future lookups
            self.cache.set(short_key, long_url)

        return long_url


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    db = URLDatabase()
    cache = URLCache()
    shortener = URLShortener(db, cache)

    # Shorten some URLs
    print("--- Shortening URLs ---")
    urls = [
        "https://www.example.com/very/long/path/to/resource?id=12345",
        "https://docs.python.org/3/library/hashlib.html",
        "https://github.com/user/repo/blob/main/src/long_file_name.py",
    ]

    short_urls = []
    for url in urls:
        short = shortener.shorten(url)
        short_urls.append(short)
        print(f"  {url}\n  → {short}\n")

    # Redirect (lookup)
    print("--- Redirecting ---")
    for short_url in short_urls:
        original = shortener.redirect(short_url)
        print(f"  {short_url}\n  → {original}\n")

    # Cache hit on second lookup
    print("--- Second Lookup (cache hit) ---")
    shortener.redirect(short_urls[0])

    # Cache stats
    print("\n--- Cache Stats ---")
    stats = cache.stats()
    print(
        f"  Hits: {stats['hits']}, Misses: {stats['misses']}, Hit Rate: {stats['hit_rate']}"
    )


if __name__ == "__main__":
    main()
