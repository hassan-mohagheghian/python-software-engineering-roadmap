# Polymorphism - Same method name, different behaviors across classes

# ===========================================
# Example1: Method Polymorphism (Most Common)
# -------------------------------------------


class Dog:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f"{self.name} says: Woof! Woof!"

    def move(self):
        return f"{self.name} runs on 4 legs"


class Cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f"{self.name} says: Meow! Meow!"

    def move(self):
        return f"{self.name} pounces silently"


class Bird:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f"{self.name} says: Chirp! Chirp!"

    def move(self):
        return f"{self.name} flies through the air"


class Fish:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f"{self.name} makes: Blub! Blub!"

    def move(self):
        return f"{self.name} swims in water"


# Polymorphic function - works with ANY animal that has sound() and move()
def animal_interaction(animal):
    """This function doesn't cate what type of animal it gets"""
    print(animal.sound())
    print(animal.move())
    print("-" * 30)


# Same function call - completely different behaviors
animals = [Dog("Rex"), Cat("Whiskers"), Bird("Tweety"), Fish("Nemo")]

for animal in animals:
    animal_interaction(animal)
#  Output:
# Rex says: Woof! Woof!
# Rex runs on 4 legs
# ------------------------------
# Whiskers says: Meow! Meow!
# Whiskers pounces silently
# ------------------------------
# Tweety says: Chirp! Chirp!
# Tweety flies through the air
# ------------------------------
# Nemo makes: Blub! Blub!
# Nemo swims in water
# ------------------------------


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Example 2: Polymorphism with inheritance (Most Common Pattern)
# ==============================================================


class Shape:
    """Parent class defining the polymorphic inheritance"""

    def area(self):
        """Common interface - to be overridden"""
        pass

    def perimeter(self):
        "Common interface - to be overridden"
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.width

    def perimeter(self):
        return 2 * (self.width * self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math

        return math.pi * self.radius**2

    def perimeter(self):
        import math

        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        def area(self):
            # Heron's formula
            s = self.perimeter() / 2
            return (
                s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)
            ) ** 0.5

        def perimeter(self):
            return self.side_a + self.side_b + self.side_c


def print_shape_into(shape: Shape):
    "works with ANY shape, doesn't need to know the type"
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter:.2f}")
    print("-" * 30)


# Same function, different behaviors

shapes = [Rectangle(5, 3), Circle(4), Triangle(3, 4, 5)]


for shape in shapes:
    print_shape_into(shape)

# Output:
# Area: 15.00
# Perimeter: 16.00
# ------------------------------
# Area: 50.27
# Perimeter: 25.13
# ------------------------------
# Area: 6.00
# Perimeter: 12.00
# ------------------------------
