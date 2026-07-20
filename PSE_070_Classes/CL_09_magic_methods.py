# Classes - Magic Methods
# -----------------------------------------------------------------------------
# Magic methods (dunder methods) let classes integrate with Python's
# built-in operations like printing, comparison, and arithmetic.
#
# Key concepts:
# 1. __str__ and __repr__ — string representation
# 2. __len__, __getitem__ — container protocol
# 3. __eq__, __lt__ — comparison operators
# 4. __add__, __mul__ — arithmetic operators
# 5. __enter__, __exit__ — context manager protocol
# -----------------------------------------------------------------------------
# Why magic methods matter:
#
# - Make custom objects work with built-in functions
# - Enable natural, Pythonic syntax (len(), print(), +, ==)
# - Support protocols (context manager, iterator, container)
# - Integrate seamlessly with Python's ecosystem
# -----------------------------------------------------------------------------
# High-level flow:
#
# Built-in operation → Python calls magic method → Custom behavior executes
#     (len(obj))           (__len__)                  (returns length)
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - __repr__ for debugging: Point(3, 4)
# - __str__ for display: (3, 4)
# - __eq__ for comparison: user1 == user2
# - __add__ for combining: vector1 + vector2
# - __len__ for containers: len(playlist)
# - __enter__/__exit__ for context managers: with open() as f:
# -----------------------------------------------------------------------------


# =============================================================================
# String Representation
# =============================================================================


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """Developer representation."""
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        """User-friendly representation."""
        return f"({self.x}, {self.y})"


p = Point(3, 4)
print(f"repr: {repr(p)}")
print(f"str: {str(p)}")


# =============================================================================
# Comparison Operators
# =============================================================================


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __eq__(self, other):
        return self.celsius == other.celsius

    def __lt__(self, other):
        return self.celsius < other.celsius

    def __le__(self, other):
        return self.celsius <= other.celsius

    def __repr__(self):
        return f"Temperature({self.celsius}C)"


t1 = Temperature(20)
t2 = Temperature(30)
print(f"t1 == t2: {t1 == t2}")
print(f"t1 < t2: {t1 < t2}")


# =============================================================================
# Arithmetic Operators
# =============================================================================


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 * 3 = {v1 * 3}")
print(f"|v1| = {abs(v1):.2f}")


# =============================================================================
# Container Protocol
# =============================================================================


class Playlist:
    def __init__(self, songs):
        self._songs = list(songs)

    def __len__(self):
        return len(self._songs)

    def __getitem__(self, index):
        return self._songs[index]

    def __contains__(self, song):
        return song in self._songs


playlist = Playlist(["Song A", "Song B", "Song C"])
print(f"Length: {len(playlist)}")
print(f"First: {playlist[0]}")
print(f"Has B: {'Song B' in playlist}")


def main():
    print("=== Magic Methods ===")
    p = Vector(3, 4)
    print(f"Vector: {p}, magnitude: {abs(p):.2f}")
    t1 = Temperature(37)
    t2 = Temperature(40)
    print(f"Fever: {t2 > t1}")


if __name__ == "__main__":
    main()
