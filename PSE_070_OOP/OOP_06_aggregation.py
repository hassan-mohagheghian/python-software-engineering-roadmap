# OOP in Python - Aggregation
# -----------------------------------------------------------------------------
# Aggregation is a type of association that represents a "has-a" relationship
# between two classes. It is a weaker form of composition where the lifetime
# of the contained object is not tied to the lifetime of the container object.
# -----------------------------------------------------------------------------
# In this example, the Library class has an aggregation relationship with the Book class.
# The Library class can contain multiple Book objects, but the Book objects can exist
# independently of the Library. The lifetime of the Book objects is not tied to the lifetime
# of the Library object, meaning that the Book objects can exist without the Library and
# vice versa.


class Book:
    def __init__(self, title: str):
        self.title = title


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"'{book.title}' has been added to the library.")


if __name__ == "__main__":
    library = Library()
    book1 = Book(title="The Great Gatsby")
    book2 = Book(title="To Kill a Mockingbird")

    library.add_book(book1)
    library.add_book(book2)

    # The books can exist independently of the library
    print(f"Book 1 title: {book1.title}")
    print(f"Book 2 title: {book2.title}")
    # The library can exist without the books
    print(f"Library has {len(library.books)} books.")
