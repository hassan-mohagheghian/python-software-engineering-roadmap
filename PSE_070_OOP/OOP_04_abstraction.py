from abc import ABC, abstractmethod


# Abstract part 1: Abstraction interface (defines WHAT)
class DataStorage(ABC):
    """Abstract Class - defines the contract, not the implementation"""

    @abstractmethod
    def save(self, data):
        """save data - HOW is not specified her"""
        pass

    @abstractmethod
    def load(self, id):
        """Load data - HOW is not specified here. only WHAT"""
        pass


# Abstraction part 2: Concrete implementation (hide HOW)
class DatabaseStorage(DataStorage):
    """Hides complex SQL/database logic"""

    def save(self, data):
        print(f"saving to postgresql: {data}")
        # 50 lines of logic

    def load(self, id):
        print(f"loading from PostgreSQL: {id}")
        return {"id": id, "data": "from db"}


class FileStorage(DataStorage):
    "Hide complex file system operations"

    def save(self, data):
        # File handling, serialization, permissions HIDDEN
        print(f"Saving to file: {data}")

    def load(self, id):
        # File reading, parsing, error handling HIDDEN
        print(f"Loading, from file: {id}")
        return {"id": id, "data": "from file"}


class CloudStorage(DataStorage):
    "Hides complex network/API calls"

    def save(self, data):
        # HTTP requests, authentication, retry logic HIDDEN
        print(f"Saving to AWS S3: {data}")

    def load(self, id):
        # API calls, pagination, caching HIDDEN
        print(f"loading from s3: {id}")
        return {"id": id, "data": "from cloud"}


# User only sees the simple interface, not the complexity
def process_data(storage: DataStorage):
    """Works with ANY storage - doesn't need to know HOT"""
    storage.save("user data")
    result = storage.load(123)
    return result


# same interface, completely different hidden complexity
process_data(DatabaseStorage())  # Hides SQL complexity
process_data(FileStorage())  # Hides file I/O complexity
process_data(CloudStorage())  # Hides network complexity
