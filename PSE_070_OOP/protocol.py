# OOP in Python - Protocols
# ------------------------------------------------------------
# A Protocol defines a *contract* (methods/attributes required) without forcing inheritance.
# This enables "structural typing"; If a class has the required methods, it automatically matches.
# Protocols is a form of duck typing, but with explicit type checking at compile time (using type hints).


# ------------------------------------------------------------
# In this example, we define a protocol for "Readable" objects that require a read() method.
from typing import Protocol


class Readable(Protocol):
    def read(self) -> str: ...


class FileReader:
    def read(self) -> str:
        return "Reading data from a file."


class DatabaseReader:
    def read(self) -> str:
        return "Reading data from a database."


def process_data(reader: Readable) -> None:
    print(reader.read())


# Both FileReader and DatabaseReader match the Readable protocol, so we can use them with process_data.
file_reader = FileReader()
database_reader = DatabaseReader()
process_data(file_reader)  # Output: Reading data from a file.
process_data(database_reader)  # Output: Reading data from a database.
