# Architectural Patterns - Data Mapper Pattern
# -----------------------------------------------------------------------------
# The Data Mapper Pattern separates the in-memory domain model from the database
# persistence layer. It moves data between objects and a database schema while
# keeping them entirely independent of each other and the mapper itself.
#
# Contrast with Active Record:
#
#   - Active Record: The domain class inherits database save/load operations.
#     It violates SRP (Single Responsibility Principle) because the class is
#     responsible for business rules AND database communication.
#
#   - Data Mapper: The domain class is a pure Python object (e.g., dataclass) with
#     zero database code or dependency. The Mapper class handles all database
#     operations (select, insert, update) mapping database rows to domain objects.
#
# Benefits:
# - True separation of concerns (domain models contain only business rules)
# - Loose coupling (database schema can change without altering domain logic)
# - Easier unit testing (mocking is easier since domain classes have no DB side effects)
#
# Real-world examples:
# - SQLAlchemy (Unit of Work + Data Mapper design)
# - Hibernate/Java Persistence API (JPA) in Java
# -----------------------------------------------------------------------------

from dataclasses import dataclass
from typing import Dict, List, Optional

# =============================================================================
# Domain Model (Pure, no DB dependencies or inheritance)
# =============================================================================


@dataclass
class User:
    user_id: int
    username: str
    email: str

    def change_email(self, new_email: str):
        # Pure business rule
        if "@" not in new_email:
            raise ValueError("Invalid email format")
        self.email = new_email


# =============================================================================
# Mock Database Schema
# =============================================================================


class MockDBTable:
    def __init__(self):
        # Simulated database rows: {id: {"id_col": 1, "username_col": "alice", "email_col": "..."}}
        self.rows: Dict[int, Dict[str, int | str]] = {}

    def insert(self, row_id: int, row_data: Dict[str, int | str]):
        self.rows[row_id] = row_data

    def select_by_id(self, row_id: int) -> Optional[Dict[str, int | str]]:
        return self.rows.get(row_id)

    def select_all(self) -> List[Dict[str, int | str]]:
        return list(self.rows.values())


# =============================================================================
# Data Mapper (Handles translation between DB row dict and User object)
# =============================================================================


class UserMapper:
    def __init__(self, db_table: MockDBTable):
        self.db_table = db_table

    def find_by_id(self, user_id: int) -> Optional[User]:
        print(f"[UserMapper] Finding User with ID {user_id} in Database...")
        row = self.db_table.select_by_id(user_id)
        if not row:
            print(f"[UserMapper] User with ID {user_id} not found.")
            return None

        # Map database row columns -> domain object attributes
        user = User(
            user_id=int(row["id_col"]),
            username=str(row["username_col"]),
            email=str(row["email_col"]),
        )
        print(f"[UserMapper] Successfully mapped DB columns to User({user.username}).")
        return user

    def save(self, user: User):
        print(f"[UserMapper] Saving User({user.username}) state to Database...")
        # Map domain object attributes -> database row columns
        row_data = {
            "id_col": user.user_id,
            "username_col": user.username,
            "email_col": user.email,
        }
        self.db_table.insert(user.user_id, row_data)
        print("[UserMapper] Save complete.")


# =============================================================================
# Active Record Contrast (Shown for comparison)
# =============================================================================


class ActiveRecordUser:
    """
    Active Record violation example:
    The model holds state, business rules AND SQL operations.
    """

    def __init__(self, user_id: int, username: str, email: str, db_table: MockDBTable):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.db_table = db_table

    def save(self):
        # Violation: domain object directly saves itself to database
        row_data = {
            "id_col": self.user_id,
            "username_col": self.username,
            "email_col": self.email,
        }
        self.db_table.insert(self.user_id, row_data)


# =============================================================================
# Execution
# =============================================================================

if __name__ == "__main__":
    # Create simulated database table
    user_db_table = MockDBTable()

    # 1. Store initial mock row directly in Database (simulating existing database rows)
    user_db_table.insert(
        1, {"id_col": 1, "username_col": "charlie", "email_col": "charlie@example.com"}
    )

    # 2. Instantiate the Data Mapper
    mapper = UserMapper(user_db_table)

    print("--- Reading via Data Mapper ---")
    # Fetch User 1. The domain object returned has no references to user_db_table or SQL columns.
    user = mapper.find_by_id(1)
    if user:
        print(f"Loaded User object: {user}")

        # 3. Change email using pure business logic
        print("\n--- Modifying domain object ---")
        user.change_email("charlie_new@example.com")
        print(f"Modified User object state: {user}")

        # Database table remains unchanged at this point
        print(f"Current DB Table row 1 before save: {user_db_table.select_by_id(1)}")

        # 4. Save modifications back via Data Mapper
        print("\n--- Saving via Data Mapper ---")
        mapper.save(user)
        print(f"Current DB Table row 1 after save: {user_db_table.select_by_id(1)}")

    # 5. Create and save a new user
    print("\n--- Creating and Saving New User ---")
    new_user = User(2, "david", "david@example.com")
    mapper.save(new_user)

    print(f"\nAll Database Rows: {user_db_table.select_all()}")
