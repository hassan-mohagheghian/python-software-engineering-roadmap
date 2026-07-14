# Single Responsibility Principle (SRP)
# A class should only have one reason to change.
# In other words, a class should have only one job or responsibility.
# Despite this principle often be used for classes it can be applied in other places for example for functions


# ------------------- Wrong Usage --------------------
# Problem: if each one of  email format, logging, email service, database
# or event info format changes, this class needs to be changed.
# this possibility to multiple request to change violate only one reason to change
class User:
    """This class has TOO MANY responsibilities"""

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    # Responsibility 1 : User Data Management
    def get_user_info(self):
        return f"{self.name} ({self.email})"

    # Responsibility 2: Database Operations
    def save_to_database(self):
        print(f"Saving {self.name} to database")
        # Some Stuffs related to Database: connection, query, commit, ...

    # Responsibility 3: Email sending
    def send_welcome_email(self):
        print(f"Seining email to {self.email}")
        # Some actions related to send email: SMTP settings, connection, email template, ...s

    # Responsibility 4: Logging
    def log_activity(self, action: str):
        print(f"[LOG] User {self.name} performed: {action}")
        # Somethings about logs: file writing, log rotations, ...

    # Responsibility 5: Logging
    def validate_email(self):
        return "@" in self.email and "." in self.email


# --------------- Right Usage -----------------------
# Each class has ONE responsibility


# Responsibility 1: User Data Management
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def get_user_info(self):
        return f"{self.name} ({self.email})"


# Responsibility 2: Database Operations
class UserRepository:
    def save(self, user: User):
        print(f"Saving {user.name} to database")
        # Database specific code here

    def find_by_email(self, email: str):
        print(f"Finding user with email {email}")
        return "User info from database"  # in reality an user object


# Responsibility 3: Email Sending
class EmailService:
    def send_welcome_email(self, user: User):
        print(f"Sending welcome email to {user.email}")
        # Email Specific code here


# Responsibility 4: Logging
class Logger:
    def log_activity(self, user: User, action: str):
        print(f"[LOG] User {user.name} performed: {action}")
        # Logging specific code here


# Responsibility 5: Validation
class UserValidator:
    def validate_email(self, user: User):
        return "@" in user.email and "." in user.email


# Usage - each class handles its own responsibility
user = User("Alice", "alice@example.com")
validator = (
    UserValidator()
)  # just for simplicity is used here but can be used as a dependency or composition in User class
if validator.validate_email(user=user):
    repo = UserRepository()
    repo.save(user=user)
    email_service = EmailService()
    email_service.send_welcome_email(user)
    logger = Logger()
    logger.log_activity(user, "registered")
