# Design Patterns - Factory Method Pattern
# -----------------------------------------------------------------------------
# The Factory Method Pattern defines an interface for creating objects while
# allowing subclasses to decide which concrete object should be created.
#
# The primary goal is NOT object creation itself.
#
# The primary goal is to separate:
#
#     Object Creation
#               from
#     Object Usage
#
# Without Factory Method:
#
#     service = S3Storage()
#
# The client becomes tightly coupled to a specific implementation.
#
# With Factory Method:
#
#     storage = factory.create_storage()
#
# The client only depends on abstractions and does not need to know
# which storage implementation is being used.
#
# Benefits:
#
# - Follows the Open/Closed Principle (OCP)
#   New storage providers can be added without modifying client code.
#
# - Reduces coupling
#   Client code depends on abstractions rather than concrete classes.
#
# - Centralizes object creation
#   Construction logic lives in one place.
#
# - Supports Dependency Injection
#   Factories can be injected into services.
#
# Real-world examples:
#
# - AWS S3 vs Azure Blob vs Local Storage
# - PostgreSQL vs MySQL vs SQLite
# - RabbitMQ vs Kafka
# - Stripe vs PayPal
# - Google OAuth vs GitHub OAuth
# -----------------------------------------------------------------------------


# -------------------------------Example----------------------------------------

from abc import ABC, abstractmethod

# -----------------------------------------------------------------------------
# Product Interface
# -----------------------------------------------------------------------------
# Every storage provider must support the upload() operation.
# -----------------------------------------------------------------------------


class Storage(ABC):
    @abstractmethod
    def upload(self, file_name: str):
        pass


# -----------------------------------------------------------------------------
# Concrete Products
# -----------------------------------------------------------------------------


class LocalStorage(Storage):
    def upload(self, file_name: str):
        print(f"Uploading '{file_name}' to local storage")


class S3Storage(Storage):
    def upload(self, file_name: str):
        print(f"Uploading '{file_name}' to AWS S3")


class AzureBlobStorage(Storage):
    def upload(self, file_name: str):
        print(f"Uploading '{file_name}' to Azure Blob Storage")


# -----------------------------------------------------------------------------
# Creator Interface
# -----------------------------------------------------------------------------
# Every factory knows how to create one type of Storage.
# -----------------------------------------------------------------------------


class StorageFactory(ABC):
    @abstractmethod
    def create_storage(self) -> Storage:
        pass


# -----------------------------------------------------------------------------
# Concrete Factories
# -----------------------------------------------------------------------------


class LocalStorageFactory(StorageFactory):
    def create_storage(self) -> Storage:
        return LocalStorage()


class S3StorageFactory(StorageFactory):
    def create_storage(self) -> Storage:
        return S3Storage()


class AzureBlobStorageFactory(StorageFactory):
    def create_storage(self) -> Storage:
        return AzureBlobStorage()


# -----------------------------------------------------------------------------
# Client
# -----------------------------------------------------------------------------
# The client depends only on abstractions:
#
#     StorageFactory
#     Storage
#
# The client never directly creates:
#
#     S3Storage()
#     AzureBlobStorage()
#     LocalStorage()
#
# This means new storage providers can be added without changing
# FileUploadService.
# -----------------------------------------------------------------------------


class FileUploadService:
    def __init__(self, storage_factory: StorageFactory):
        self.storage_factory = storage_factory

    def upload_file(self, file_name: str):
        storage = self.storage_factory.create_storage()
        storage.upload(file_name)


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    print("=== Local Storage ===")
    service = FileUploadService(storage_factory=LocalStorageFactory())
    service.upload_file("profile.jpg")

    print("\n=== AWS S3 ===")
    service = FileUploadService(storage_factory=S3StorageFactory())
    service.upload_file("profile.jpg")

    print("\n=== Azure Blob ===")
    service = FileUploadService(storage_factory=AzureBlobStorageFactory())
    service.upload_file("profile.jpg")


if __name__ == "__main__":
    main()
