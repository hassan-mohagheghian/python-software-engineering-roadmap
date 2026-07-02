# System Design - Pagination
# -----------------------------------------------------------------------------
# Pagination is the practice of dividing large datasets into discrete pages
# so clients can fetch data in manageable chunks instead of loading everything
# at once.
#
# -----------------------------------------------------------------------------
# Why pagination matters:
#
# - Reduces memory usage (server and client)
# - Decreases response time
# - Reduces network bandwidth
# - Improves user experience (progressive loading)
#
# -----------------------------------------------------------------------------
# Common Strategies:
#
# 1. Offset-Based (LIMIT/OFFSET)
#    - Simple: SELECT * FROM users LIMIT 10 OFFSET 20
#    - Problem: inconsistent results if data changes between pages
#
# 2. Cursor-Based (Keyset Pagination)
#    - Uses a pointer (ID, timestamp) to mark position
#    - WHERE id > last_seen_id LIMIT 10
#    - Consistent even when data changes
#
# 3. Page Token (Opaque Token)
#    - Server encodes position into an opaque token
#    - Client passes token to get next page
#    - Used by APIs like YouTube, Twitter
#
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - SQL LIMIT/OFFSET queries
# - API pagination (GitHub, Twitter, YouTube)
# - Infinite scroll in web/mobile apps
# - Search result pages
# -----------------------------------------------------------------------------

from dataclasses import dataclass
from typing import Any

# -----------------------------------------------------------------------------
# Data Model
# -----------------------------------------------------------------------------


@dataclass
class User:
    id: int
    name: str
    email: str


# -----------------------------------------------------------------------------
# Simulated Database with Users
# -----------------------------------------------------------------------------


class UserDatabase:
    def __init__(self):
        self.users: list[User] = [
            User(id=i, name=f"User_{i:03d}", email=f"user{i}@example.com")
            for i in range(1, 101)  # 100 users
        ]

    def get_all(self) -> list[User]:
        return self.users


# -----------------------------------------------------------------------------
# Strategy 1: Offset-Based Pagination
# -----------------------------------------------------------------------------


class OffsetPaginator:
    """
    Uses LIMIT and OFFSET to paginate.
    Simple but can return duplicate/missing items if data changes.
    """

    def __init__(self, data: list[Any], page_size: int = 10):
        self.data = data
        self.page_size = page_size

    def get_page(self, page_number: int) -> dict:
        """
        page_number is 1-based.
        """
        offset = (page_number - 1) * self.page_size
        items = self.data[offset : offset + self.page_size]

        total_items = len(self.data)
        total_pages = (total_items + self.page_size - 1) // self.page_size

        return {
            "page": page_number,
            "page_size": self.page_size,
            "total_items": total_items,
            "total_pages": total_pages,
            "has_next": page_number < total_pages,
            "has_prev": page_number > 1,
            "items": items,
        }


# -----------------------------------------------------------------------------
# Strategy 2: Cursor-Based Pagination (Keyset)
# -----------------------------------------------------------------------------


class CursorPaginator:
    """
    Uses the last item's ID as a cursor.
    Consistent results even when data changes between requests.
    """

    def __init__(self, data: list[User], page_size: int = 10):
        self.data = sorted(data, key=lambda u: u.id)
        self.page_size = page_size

    def get_page(self, after_id: int | None = None) -> dict:
        """
        Returns items after the given ID.
        If after_id is None, returns the first page.
        """
        if after_id is None:
            items = self.data[: self.page_size]
        else:
            items = [u for u in self.data if u.id > after_id][: self.page_size]

        next_cursor = items[-1].id if items else None
        has_next = any(u.id > next_cursor for u in self.data) if next_cursor else False

        return {
            "cursor": after_id,
            "next_cursor": next_cursor,
            "has_next": has_next,
            "page_size": self.page_size,
            "items": items,
        }


# -----------------------------------------------------------------------------
# Strategy 3: Page Token (Opaque Token)
# -----------------------------------------------------------------------------


class PageTokenPaginator:
    """
    Encodes the offset into an opaque base64-like token.
    Client doesn't know the internal position.
    """

    def __init__(self, data: list[Any], page_size: int = 10):
        self.data = data
        self.page_size = page_size

    def _encode_token(self, offset: int) -> str:
        """Encode offset into an opaque token."""
        import base64

        return base64.b64encode(str(offset).encode()).decode()

    def _decode_token(self, token: str) -> int:
        """Decode token back to offset."""
        import base64

        return int(base64.b64decode(token).decode())

    def get_first_page(self) -> dict:
        return self._get_page(0)

    def get_page(self, token: str) -> dict:
        offset = self._decode_token(token)
        return self._get_page(offset)

    def _get_page(self, offset: int) -> dict:
        items = self.data[offset : offset + self.page_size]
        next_offset = offset + self.page_size
        has_next = next_offset < len(self.data)

        return {
            "token": self._encode_token(offset),
            "next_token": self._encode_token(next_offset) if has_next else None,
            "has_next": has_next,
            "page_size": self.page_size,
            "items": items,
        }


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    db = UserDatabase()
    users = db.get_all()

    # --- Offset-Based ---
    print("=" * 60)
    print("OFFSET-BASED PAGINATION")
    print("=" * 60)

    paginator = OffsetPaginator(users, page_size=5)

    for page_num in [1, 2, 3]:
        result = paginator.get_page(page_num)
        names = [u.name for u in result["items"]]
        print(
            f"  Page {result['page']}: {names} "
            f"(has_next={result['has_next']}, has_prev={result['has_prev']})"
        )

    # --- Cursor-Based ---
    print("\n" + "=" * 60)
    print("CURSOR-BASED PAGINATION")
    print("=" * 60)

    cursor_paginator = CursorPaginator(users, page_size=5)

    cursor = None
    page_num = 1
    while True:
        result = cursor_paginator.get_page(after_id=cursor)
        names = [u.name for u in result["items"]]
        print(f"  Page {page_num}: {names} (cursor={cursor})")

        if not result["has_next"]:
            break
        cursor = result["next_cursor"]
        page_num += 1

        if page_num > 5:  # Limit for demo
            print("  ... (truncated)")
            break

    # --- Page Token ---
    print("\n" + "=" * 60)
    print("PAGE TOKEN PAGINATION")
    print("=" * 60)

    token_paginator = PageTokenPaginator(users, page_size=5)

    result = token_paginator.get_first_page()
    names = [u.name for u in result["items"]]
    print(f"  First page: {names}")
    print(f"  Next token: {result['next_token']}")

    if result["next_token"]:
        result2 = token_paginator.get_page(result["next_token"])
        names = [u.name for u in result2["items"]]
        print(f"  Second page: {names}")


if __name__ == "__main__":
    main()
