# Design Patterns - Builder Pattern
# -----------------------------------------------------------------------------
# The Builder Pattern is a creational design pattern that separates the
# construction of a complex object from its representation.
#
# It allows you to build objects step-by-step instead of creating them
# in a single constructor call with many parameters.
#
# -----------------------------------------------------------------------------
# When to use:
#
# - Object has many optional parameters
# - Object construction is complex
# - You want readable and maintainable object creation
#
# -----------------------------------------------------------------------------
# Key Idea:
#
# Director (optional) → Builder → Product
#
# You construct an object step by step:
#
#   build_part_a()
#   build_part_b()
#   build_part_c()
#
# -----------------------------------------------------------------------------
# Benefits:
#
# - Improves readability
# - Avoids telescoping constructors
# - Supports immutable final objects
# - Encapsulates construction logic
#
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - Building HTTP requests
# - Creating complex SQL queries
# - Configuring Docker containers
# - Constructing UI forms
# - FastAPI request models setup
# -----------------------------------------------------------------------------


from abc import ABC, abstractmethod

from typing_extensions import Self

# -----------------------------------------------------------------------------
# Product
# -----------------------------------------------------------------------------


class Computer:
    def __init__(self):
        self.cpu: str | None = None
        self.ram: str | None = None
        self.storage: str | None = None
        self.gpu: str | None = None

    def __str__(self):
        return (
            f"Computer(cpu={self.cpu}, "
            f"ram={self.ram}, "
            f"storage={self.storage}, "
            f"gpu={self.gpu})"
        )


# -----------------------------------------------------------------------------
# Builder Interface
# -----------------------------------------------------------------------------


class ComputerBuilder(ABC):
    @abstractmethod
    def set_cpu(self) -> Self:
        pass

    @abstractmethod
    def set_ram(self) -> Self:
        pass

    @abstractmethod
    def set_storage(self) -> Self:
        pass

    @abstractmethod
    def set_gpu(self) -> Self:
        pass

    @abstractmethod
    def get_result(self) -> Computer:
        pass


# -----------------------------------------------------------------------------
# Concrete Builder
# -----------------------------------------------------------------------------


class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self):
        self.computer.cpu = "Intel i9"
        return self

    def set_ram(self):
        self.computer.ram = "32GB"
        return self

    def set_storage(self):
        self.computer.storage = "1TB SSD"
        return self

    def set_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4090"
        return self

    def get_result(self) -> Computer:
        return self.computer


# -----------------------------------------------------------------------------
# Director (optional)
# -----------------------------------------------------------------------------


class Director:
    """
    Defines construction order.
    """

    def build_gaming_pc(self, builder: ComputerBuilder):
        return builder.set_cpu().set_ram().set_storage().set_gpu().get_result()


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    director = Director()

    builder = GamingComputerBuilder()

    computer = director.build_gaming_pc(builder)

    print(computer)


if __name__ == "__main__":
    main()
