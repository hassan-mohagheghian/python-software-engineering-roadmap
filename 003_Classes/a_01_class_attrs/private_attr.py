class BankAccount:
    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


# Usage
account = BankAccount("Alice", 1000)

# Direct access fails
# print(account.__balance)

# But it's not truly hidden - name mangling reveals it.
print(account._BankAccount__balance)  # 1000 (works but don't do this)


# Name mangling makes it harder to accidentally access
# But determined developers can still get to it


# How name mangling works
print(account.__dict__)
# it create an attribute in the dict
# {'owner': 'Alice', '_BankAccount__balance': 1000}


# -----------------------------------------
# When protected prevent accidental override
# -----------------------------------------


class Parent:
    def __init__(self):
        self.value = 10
        self.__secret = 20  # _Parent__secret

    def get_secret(self):
        return self.__secret


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__secret = 99  # _Child__secret - different!
        # This doesn't override parent's __secret


c = Child()
print(c.get_secret())  # 20 (parent's __secret unchanged)
print(c.__dict__)  # It has both _Child__secret and _Parent__secret
# {'value': 10, '_Parent__secret': 20, '_Child__secret': 99}
