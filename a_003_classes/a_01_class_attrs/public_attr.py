class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I'm {self.name}")


# Usage: direct access is perfectly fine
# Ok
p = Person("Alice", 30)
print(p.name)  # Alice

# Ok
p.name = "Bob"
print(p.name)  # Bob
