# Design Patterns - Abstract Factory Pattern
# -----------------------------------------------------------------------------
# The Abstract Factory Pattern provides an interface for creating families
# of related objects without specifying their concrete classes.
#
# In this example:
#
# - Storage and Cache are product interfaces.
# - AWSStorage and AWSCache belong to the AWS family.
# - AzureStorage and AzureCache belong to the Azure family.
# - CloudFactory is the abstract factory.
# - AWSFactory and AzureFactory are concrete factories.
#
# The application does not need to know whether it is using AWS or Azure.
# It only depends on abstractions.
#
# This differs from Factory Method because we are creating multiple
# related objects (Storage + Cache) instead of a single object.
# -----------------------------------------------------------------------------


from abc import ABC, abstractmethod

# -----------------------------------------------------------------------------
# Product Interfaces
# -----------------------------------------------------------------------------


class Storage(ABC):
    @abstractmethod
    def upload(self, file_name: str):
        pass


class Cache(ABC):
    @abstractmethod
    def set(self, key: str, value: str):
        pass


# -----------------------------------------------------------------------------
# AWS Family
# -----------------------------------------------------------------------------


class AWSStorage(Storage):
    def upload(self, file_name: str):
        print(f"Uploading '{file_name}' to AWS S3")


class AWSCache(Cache):
    def set(self, key: str, value: str):
        print(f"Saving '{key}' in AWS ElastiCache")


# -----------------------------------------------------------------------------
# Azure Family
# -----------------------------------------------------------------------------


class AzureStorage(Storage):
    def upload(self, file_name: str):
        print(f"Uploading '{file_name}' to Azure Blob Storage")


class AzureCache(Cache):
    def set(self, key: str, value: str):
        print(f"Saving '{key}' in Azure Cache for Redis")


# -----------------------------------------------------------------------------
# Abstract Factory
# -----------------------------------------------------------------------------
# Defines how to create a family of related objects.
# -----------------------------------------------------------------------------


class CloudFactory(ABC):
    @abstractmethod
    def create_storage(self) -> Storage:
        pass

    @abstractmethod
    def create_cache(self) -> Cache:
        pass


# -----------------------------------------------------------------------------
# Concrete Factories
# -----------------------------------------------------------------------------
# Each factory creates a compatible family of objects.
# -----------------------------------------------------------------------------


class AWSFactory(CloudFactory):
    def create_storage(self) -> Storage:
        return AWSStorage()

    def create_cache(self) -> Cache:
        return AWSCache()


class AzureFactory(CloudFactory):
    def create_storage(self) -> Storage:
        return AzureStorage()

    def create_cache(self) -> Cache:
        return AzureCache()


# -----------------------------------------------------------------------------
# Client
# -----------------------------------------------------------------------------
# The client only depends on abstractions.
#
# It does not know:
# - AWSStorage
# - AWSCache
# - AzureStorage
# - AzureCache
#
# It only knows:
# - Storage
# - Cache
# - CloudFactory
# -----------------------------------------------------------------------------


class FileService:
    def __init__(self, factory: CloudFactory):
        self.storage = factory.create_storage()
        self.cache = factory.create_cache()

    def process_file(self, file_name: str):
        self.storage.upload(file_name)
        self.cache.set("last_uploaded_file", file_name)


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    print("=== AWS Environment ===")
    service = FileService(factory=AWSFactory())
    service.process_file("profile.jpg")

    print("\n=== Azure Environment ===")
    service = FileService(factory=AzureFactory())
    service.process_file("profile.jpg")


if __name__ == "__main__":
    main()
