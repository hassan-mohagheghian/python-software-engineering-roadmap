# OOP in Python - Dependency Injection (DI)
# ----------------------------------------------------------------------------
# Dependency Injection is a design pattern that allows a class to receive its dependencies
# from an external source rather than creating them internally. This promotes loose coupling
# and makes the code more flexible and easier to test.
# ----------------------------------------------------------------------------
# In this example, the Car class depends on the Engine class. Instead of creating an instance
# of the Engine class inside the Car class, we inject the dependency through the constructor.
# This allows us to easily swap out the Engine implementation (e.g., for testing or using
# different types of engines) without modifying the Car class, adhering to the Dependency
# Inversion Principle.


class Engine:
    def start(self):
        raise NotImplementedError()


class ElectricEngine(Engine):
    def start(self):
        print("Eclectic engine started.")


# Usage: COMPOSITION
# the creation of object is inside the consumer class
class Car:
    def __init__(self):
        self.engine = ElectricEngine()


# Usage: Dependency Injections
class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        self.engine.start()


if __name__ == "__main__":
    electric_engine = ElectricEngine()
    car = Car(engine=ElectricEngine())
    car.start()
