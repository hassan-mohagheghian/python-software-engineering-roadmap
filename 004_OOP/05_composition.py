# Composition: Has-a relationship


# ----------------- Wrong Usage -------------------
# Problem: Inheritance models is-a relationship and is not appropriate for each cases


class Engine:
    def start(self):
        print("engin started")


# Bad: A Car is not a Engine
class Car(Engine):
    def drive(self):
        print("Driving")


car = Car()
car.start()  # Works, but conceptually wrongs
car.drive()

# --------------------- Right Usage ---------------
# A Car has an engine so we can use composition


class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def drive(self):
        self.engine.start()
        print("Driving")


engine = Engine()
car = Car(engine=Engine())
car.drive

# Also with composition we can benefit from OCP principle
# And substitute the engine with a more concrete one


class ElectricEngine(Engine):
    def start(self):
        print("Electric Engine activated")


car = Car(ElectricEngine())
car.drive()
