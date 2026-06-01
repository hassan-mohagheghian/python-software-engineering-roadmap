# protected attribute are for internal usage only


class BankAccount:
    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self._pin = "123"
        self._balance = balance

    def deposit(self, amount: int):
        if amount > 0:
            self._balance += amount
            self._log_transaction(amount)

    def get_balance(self):
        return self._balance

    def _log_transaction(self, amount: int):
        print(f"Transition: {amount}")


account = BankAccount("Alice", 8000)

# this works but underscore warns you not to use
print(account._pin)  # 123, works but discouraged
account._balance = 9000  # works but you're being naughty

# better practice: use public methods
print(account.get_balance())


# ---------------------------
# section 2: with subclasses
# ---------------------------


class Vehicle:
    def __init__(self):
        self._engine_status = "off"

    def _start_engine(self):
        self._engine_status = "on"
        print("Engine started")


class Car(Vehicle):
    def derive(self):
        self._start_engine()  # OK, subclass can use protected
        print(f"Driving with engine {self._engine_status}")
