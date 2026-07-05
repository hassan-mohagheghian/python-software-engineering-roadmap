class BankAccount:
    def __init__(self, owner: str, balance: int):
        # ENCAPSULATION PART 1: Hidden internals
        self.owner = owner  # public (less protected)
        self._pin = "1234"  # Protected (internal use)
        self.__balance = balance  # Private (hidden data)

    # ENCAPSULATION PART 2: Public API (Controlled Access)
    def deposit(self, amount: int):  # public methods
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):  # public methods
        if 0 < amount < self.__balance:
            self.__balance -= amount

    def get_balance(self):  # public method (read-only access)
        return self.__balance

    def verify_pin(self, pin):  # Public method for protected data
        return self._pin == pin


# Example 2:
class DatabaseConnection:
    # Encapsulation: Both hidden internals and public API

    def __init__(self, connection_string):
        self.__connection_string = connection_string
        self.__connection = None
        self._retry_count = 3

    # Public API - controlled access to hidden internals
    def connect(self):
        """Public method - hides complex connection logic"""
        if not self.__connection:
            self.__connection = self._establish_connection()
        return self.__connection

    def execute_query(self, query):
        """Public method - hides query execution details"""
        conn = self.connect()
        # Complex query execution hidden
        return conn.execute(query)

    def _establish_connection(self):
        """Protected method - internal use, but subclasses can override"""
        # Complex connection logic hidden
        pass
