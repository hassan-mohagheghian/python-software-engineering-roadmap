# Advanced Patterns - Repository Pattern
# -------------------------------------------------------------------------
# The Repository Pattern mediates between the domain and data mapping layers.
# It acts as an in-memory collection of domain objects, hiding the details of
# data storage (database, API, file system) behind a clean interface.
#
# Benefits:
# - Decouples domain logic from persistence logic
# - Easier to test (swap in a fake/in-memory repository)
# - Centralizes data access logic
#
# Real-world examples:
# - Database access layers in web applications
# - Caching layers that abstract away cache vs database
# - API clients that present a collection-like interface
#
# Relationship to OOP Concepts:
#
# - Abstraction:
#     Repository defines a contract (find, add, remove) that concrete
#     repositories implement for different storage backends.
#
# - Separation of Concerns:
#     Domain objects don't know how they're stored. The repository
#     handles persistence independently.
#
# - Dependency Inversion:
#     The application depends on the repository abstraction, not on
#     a specific database or ORM.
#
# Relationship to SOLID:
#
# - SRP:
#     Domain objects handle business rules; repositories handle storage.
#
# - DIP:
#     High-level modules depend on the repository interface, not
#     concrete storage implementations.
# -------------------------------------------------------------------------


from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Optional

# =============================================================================
# Domain Model
# =============================================================================


@dataclass
class User:
    id: int
    name: str
    email: str


# =============================================================================
# Repository Interface
# =============================================================================


class UserRepository(ABC):
    @abstractmethod
    def find_by_id(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def find_all(self) -> List[User]:
        pass

    @abstractmethod
    def add(self, user: User) -> User:
        pass

    @abstractmethod
    def remove(self, user_id: int) -> bool:
        pass


# =============================================================================
# Concrete Repository — In-Memory
# =============================================================================


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._users: Dict[int, User] = {}
        self._next_id = 1

    def find_by_id(self, user_id: int) -> Optional[User]:
        return self._users.get(user_id)

    def find_by_email(self, email: str) -> Optional[User]:
        for user in self._users.values():
            if user.email == email:
                return user
        return None

    def find_all(self) -> List[User]:
        return list(self._users.values())

    def add(self, user: User) -> User:
        user.id = self._next_id
        self._next_id += 1
        self._users[user.id] = user
        return user

    def remove(self, user_id: int) -> bool:
        if user_id in self._users:
            del self._users[user_id]
            return True
        return False


# =============================================================================
# Usage
# =============================================================================


def main():
    repo = InMemoryUserRepository()

    # Add users
    alice = repo.add(User(id=0, name="Alice", email="alice@example.com"))
    bob = repo.add(User(id=0, name="Bob", email="bob@example.com"))
    print(f"Added: {alice}")
    print(f"Added: {bob}")

    # Find by ID
    print(f"\nFind by ID 1: {repo.find_by_id(1)}")

    # Find by email
    print(f"Find by email: {repo.find_by_email('bob@example.com')}")

    # Find all
    print(f"All users: {repo.find_all()}")

    # Remove
    repo.remove(1)
    print(f"\nAfter removing ID 1: {repo.find_all()}")


if __name__ == "__main__":
    main()
