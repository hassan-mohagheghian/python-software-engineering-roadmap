# Dependency Injection (DI)
# we can classify it as a type of composition in which injected object is created in the side of caller and outside of the consumer class


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


electric_engine = ElectricEngine()
car = Car(engine=ElectricEngine())
car.start()
