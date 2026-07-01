# Classes - Dataclass
# -----------------------------------------------------------------------------
# A dataclass is a class designed mainly to store data.
#
# The @dataclass decorator automatically creates common methods such as:
#
# - __init__
# - __repr__
# - __eq__
#
# This keeps simple data-focused classes short and readable.
# -----------------------------------------------------------------------------

from dataclasses import dataclass, field


@dataclass
class User:
    id: int
    name: str
    email: str
    is_active: bool = True


@dataclass
class Order:
    order_id: int
    user: User
    items: list[str] = field(default_factory=list)

    def add_item(self, item: str):
        self.items.append(item)


def main():
    user = User(1, "Alice", "alice@example.com")

    order = Order(order_id=1001, user=user)
    order.add_item("Keyboard")
    order.add_item("Mouse")

    same_user = User(1, "Alice", "alice@example.com")

    print("===== Dataclass repr =====")
    print(user)
    print(order)

    print("\n===== Dataclass equality =====")
    print(user == same_user)

    print("\n===== Field access =====")
    print(order.user.name)
    print(order.items)


if __name__ == "__main__":
    main()
