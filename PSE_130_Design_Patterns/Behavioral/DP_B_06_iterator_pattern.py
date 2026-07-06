# Design Patterns - Iterator Pattern
# -----------------------------------------------------------------------------
# The Iterator Pattern is a behavioral design pattern that provides a way to
# access the elements of a collection sequentially without exposing its
# underlying representation.
#
# It separates the traversal logic from the collection itself.
#
# -----------------------------------------------------------------------------
# When to use:
#
# - You need to traverse a collection without exposing its internal structure.
# - You want multiple simultaneous traversals of the same collection.
# - You want a uniform interface for different collection types.
# - You need lazy evaluation (generate elements on demand).
#
# -----------------------------------------------------------------------------
# Key Idea:
#
#   Iterable (collection) -> __iter__() -> Iterator
#   Iterator              -> __next__() -> element or StopIteration
#
#   Python's for loop calls these dunder methods automatically.
#
# -----------------------------------------------------------------------------
# Benefits:
#
# - Single Responsibility: collection stores data, iterator traverses.
# - Open/Closed: new iterators without modifying the collection.
# - Supports multiple concurrent traversals.
# - Can implement lazy evaluation for large datasets.
#
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - Iterating over database query results.
# - Walking a tree/graph structure (DFS, BFS).
# - Paginating through API responses.
# - Streaming lines from a large file.
# -----------------------------------------------------------------------------

from __future__ import annotations
from typing import Any


# -----------------------------------------------------------------------------
# Iterator
# -----------------------------------------------------------------------------


class BookIterator:
    """Iterates over books in a library one at a time."""

    def __init__(self, books: list[dict[str, Any]]):
        self._books = books
        self._index = 0

    def __iter__(self) -> BookIterator:
        return self

    def __next__(self) -> dict[str, Any]:
        if self._index >= len(self._books):
            raise StopIteration
        book = self._books[self._index]
        self._index += 1
        return book


class ReverseBookIterator:
    """Iterates over books in reverse order."""

    def __init__(self, books: list[dict[str, Any]]):
        self._books = books
        self._index = len(books) - 1

    def __iter__(self) -> ReverseBookIterator:
        return self

    def __next__(self) -> dict[str, Any]:
        if self._index < 0:
            raise StopIteration
        book = self._books[self._index]
        self._index -= 1
        return book


# -----------------------------------------------------------------------------
# Iterable Collection
# -----------------------------------------------------------------------------


class Library:
    """A collection that provides multiple iterators."""

    def __init__(self):
        self._books: list[dict[str, Any]] = []

    def add_book(self, title: str, author: str, year: int):
        self._books.append({"title": title, "author": author, "year": year})

    def __iter__(self) -> BookIterator:
        return BookIterator(self._books)

    def reverse(self) -> ReverseBookIterator:
        return ReverseBookIterator(self._books)

    def __len__(self):
        return len(self._books)


# -----------------------------------------------------------------------------
# Custom Iterator: Filter by Author
# -----------------------------------------------------------------------------


class AuthorFilterIterator:
    """Iterates only over books by a specific author."""

    def __init__(self, books: list[dict[str, Any]], author: str):
        self._books = books
        self._author = author
        self._index = 0

    def __iter__(self) -> AuthorFilterIterator:
        return self

    def __next__(self) -> dict[str, Any]:
        while self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            if book["author"] == self._author:
                return book
        raise StopIteration


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    library = Library()
    library.add_book("The Hobbit", "Tolkien", 1937)
    library.add_book("1984", "Orwell", 1949)
    library.add_book("Fellowship of the Ring", "Tolkien", 1954)
    library.add_book("Animal Farm", "Orwell", 1945)
    library.add_book("The Two Towers", "Tolkien", 1954)

    # Forward iteration
    print("--- All Books (forward) ---")
    for book in library:
        print(f"  {book['title']} by {book['author']} ({book['year']})")

    # Reverse iteration
    print("\n--- All Books (reverse) ---")
    for book in library.reverse():
        print(f"  {book['title']} by {book['author']} ({book['year']})")

    # Filtered iteration
    print("\n--- Tolkien Books ---")
    for book in AuthorFilterIterator(list(library), "Tolkien"):
        print(f"  {book['title']} ({book['year']})")

    # Multiple simultaneous traversals
    print("\n--- Simultaneous Traversals ---")
    forward = iter(library)
    backward = iter(library.reverse())
    for _ in range(3):
        f = next(forward)
        b = next(backward)
        print(f"  Forward: {f['title']:40s} Backward: {b['title']}")


if __name__ == "__main__":
    main()
