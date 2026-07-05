# Design Patterns - Singleton Pattern
# -----------------------------------------------------------------------------
# The Singleton Pattern ensures a class has only one instance and provides
# a global point of access to it.
#
# In Python, there are several ways to implement a Singleton:
# 1. Overriding the `__new__` method (Classic OOP).
# 2. Using a Metaclass (Cleanest, most reusable, and robust).
# 3. Using a Decorator.
# 4. Relying on Python's module caching (implicitly a singleton).
#
# This example demonstrates both the classic `__new__` approach and the
# metaclass approach.
#
# Benefits:
# - Controlled access to a single shared resource (e.g., Database pools, Logger, Configs).
# - Saves memory by not instantiating duplicate coordinator objects.
# - Ensures consistent state across the entire application lifetime.
#
# Real-world examples:
# - Database Connection Pools
# - Logger systems
# - Application Configuration managers
# - Thread Pools
# -----------------------------------------------------------------------------


# =============================================================================
# Implementation 1: Classic __new__ Method
# =============================================================================


class ConfigurationManager:
    """
    Singleton using the classic __new__ method.
    Stores and manages application configurations.
    """

    _instance = None
    settings = {}

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("[ConfigManager] Creating initial unique instance...")
            cls._instance = super().__new__(cls)
            cls._instance.settings = {}
        return cls._instance

    def set(self, key: str, value):
        self.settings[key] = value

    def get(self, key: str):
        return self.settings.get(key)


# =============================================================================
# Implementation 2: Reusable Metaclass (Recommended for Python)
# =============================================================================


class SingletonMeta(type):
    """
    A thread-safe-ready metaclass for implementing the Singleton pattern.
    Any class that uses metaclass=SingletonMeta will automatically be a singleton.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(f"[SingletonMeta] Instantiating new {cls.__name__}...")
            # Super call executes standard object instantiation
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DatabaseConnectionPool(metaclass=SingletonMeta):
    """
    A Database Pool class utilizing the Singleton metaclass.
    """

    def __init__(self):
        # This will only be run ONCE when the class is first instantiated.
        print("[DB Pool] Initializing pool connections...")
        self.connections = ["conn_1", "conn_2", "conn_3"]

    def get_connection(self):
        return self.connections.pop() if self.connections else "No connections left"


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Testing Configuration Manager (Classic Singleton) ===")
    config1 = ConfigurationManager()
    config1.set("theme", "dark")
    config1.set("port", 8080)

    config2 = ConfigurationManager()
    print(f"config2 'theme': {config2.get('theme')}")
    print(f"config2 'port': {config2.get('port')}")

    # Check if they are the exact same instance in memory
    print(f"Are config1 and config2 the same instance? {config1 is config2}")

    print("\n=== Testing Database Connection Pool (Metaclass Singleton) ===")
    pool1 = DatabaseConnectionPool()
    pool2 = DatabaseConnectionPool()

    print(f"Connection from pool1: {pool1.get_connection()}")
    print(
        f"Connection from pool2: {pool2.get_connection()}"
    )  # Pulls from the same pool

    # Check if they are the exact same instance in memory
    print(f"Are pool1 and pool2 the same instance? {pool1 is pool2}")


if __name__ == "__main__":
    main()
