# Design Patterns - Composite Pattern
# -----------------------------------------------------------------------------
# The Composite Pattern is a structural design pattern that allows individual
# objects and groups of objects to be treated uniformly.
#
# It organizes objects into a tree structure where both a single object (Leaf)
# and a collection of objects (Composite) implement the same interface.
#
# -----------------------------------------------------------------------------
# When to use:
#
# - You need to represent hierarchical (tree-like) structures.
# - Clients should treat single objects and groups identically.
# - You want recursive operations over a hierarchy.
# j
# -----------------------------------------------------------------------------
# Key Idea:
#
#                Component
#                /       \
#            Leaf     Composite
#                          |
#                 +--------+--------+
#                 |        |        |
#               Leaf     Leaf     Composite
#
# Every object exposes the same interface.
#
# -----------------------------------------------------------------------------
# Benefits:
#
# - Treats individual objects and collections uniformly.
# - Simplifies client code.
# - Makes recursive tree operations easy.
# - Follows the Open/Closed Principle (OCP).
#
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - File systems (File and Folder)
# - Organization charts (Employee and Department)
# - HTML DOM trees
# - GUI components (Button, Panel, Window)
# - Product categories
# -----------------------------------------------------------------------------


from abc import ABC, abstractmethod

# -----------------------------------------------------------------------------
# Component
# -----------------------------------------------------------------------------


class FileSystemItem(ABC):
    @abstractmethod
    def show(self, indent: int = 0):
        pass


# -----------------------------------------------------------------------------
# Leaf
# -----------------------------------------------------------------------------


class File(FileSystemItem):
    def __init__(self, name: str):
        self.name = name

    def show(self, indent: int = 0):
        print(" " * indent + f"📄 {self.name}")


# -----------------------------------------------------------------------------
# Composite
# -----------------------------------------------------------------------------


class Folder(FileSystemItem):
    def __init__(self, name: str):
        self.name = name
        self.children: list[FileSystemItem] = []

    def add(self, item: FileSystemItem):
        self.children.append(item)

    def remove(self, item: FileSystemItem):
        self.children.remove(item)

    def show(self, indent: int = 0):
        print(" " * indent + f"📁 {self.name}")

        for child in self.children:
            child.show(indent + 4)


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    # Individual files (Leaf objects)
    readme = File("README.md")
    license_file = File("LICENSE")
    app = File("app.py")
    utils = File("utils.py")
    test_app = File("test_app.py")

    # Folders (Composite objects)
    src = Folder("src")
    tests = Folder("tests")
    root = Folder("project")

    # Build hierarchy
    src.add(app)
    src.add(utils)

    tests.add(test_app)

    root.add(readme)
    root.add(license_file)
    root.add(src)
    root.add(tests)

    # Client treats both files and folders the same
    root.show()


if __name__ == "__main__":
    main()
