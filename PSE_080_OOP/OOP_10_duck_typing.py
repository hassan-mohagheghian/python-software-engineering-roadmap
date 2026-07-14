# OOP in Python - Duck Typing
# ---------------------------------------------
# Duck typing is a programming concept that allows for more flexible and dynamic code.
# It is based on the principle of "if it looks like a duck and quacks like a duck, then it is a duck."
# In Python, we can use duck typing to write code that works with any object that
# has the required methods or attributes, regardless of its type.

# ----------------------------------------------
# In this example, process_data() works with any object that has a read() method.


class FileReader:
    def read(self):
        return "Reading data from a file."


class DatabaseReader:
    def read(self):
        return "Reading data from a database."


def process_data(reader):
    print(reader.read())


# We can use the process_data function with any object that has a read() method.
file_reader = FileReader()
database_reader = DatabaseReader()
process_data(file_reader)  # Output: Reading data from a file.
process_data(database_reader)  # Output: Reading data from a database.


# ----------------- classic example of duck typing -----------------
class Duck:
    def quack(self):
        return "Quack!"


class Person:
    def quack(self):
        return "I'm a person, but I can quack like a duck!"


def make_it_quack(duck):
    print(duck.quack())


duck = Duck()
person = Person()
make_it_quack(duck)  # Output: Quack!
make_it_quack(person)  # Output: I'm a person, but I can quack like a duck!


# ------------------------ another example: barking ------------------------
class Dog:
    def bark(self):
        return "Woof!"


class RobotDog:
    def bark(self):
        return "Beep boop, I can bark like a dog!"


def make_it_bark(dog):
    print(dog.bark())


dog = Dog()
robot_dog = RobotDog()
make_it_bark(dog)  # Output: Woof!
make_it_bark(robot_dog)  # Output: Beep boop, I can bark like a dog!
