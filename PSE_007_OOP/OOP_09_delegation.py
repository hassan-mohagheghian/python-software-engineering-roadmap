# OOP in Python - Delegation
# ----------------------------------------------------------------------------
# Delegation is a design pattern where an object handles a request by delegating it to a
# second object (the delegate). This allows for flexible code reuse and separation of concerns.
# ----------------------------------------------------------------------------
# In this example, the Car class delegates the start action to the Engine class. The Car
# class does not need to know the details of how the Engine starts; it simply calls the start
# method on the Engine instance. This promotes loose coupling and makes the code easier to
# maintain and extend.


class Engine:
    def start(self):
        raise NotImplementedError()


class ElectricEngine(Engine):
    def start(self):
        print("Electric engine started.")


class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        self.engine.start()


if __name__ == "__main__":
    electric_engine = ElectricEngine()
    car = Car(engine=electric_engine)
    car.start()
