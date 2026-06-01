# Inheritance - Child class reuses and extends parent class


class Vehicle:
    "Parent/Base/Super Class"

    def __init(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self._engin_running = False  # Protected Attribute

    def start_engine(self):
        """Method inherited by all children"""
        self._engin_running = True
        return f"{self.brand} {self.model} engine started."

    def stop_engine(self):
        """Method inherited by all children"""
        self._engin_running = False
        return f"{self.brand} {self.model} engine stopped"

    def get_info(self):
        "Method inherited by all children"
        return f"{self.year} {self.brand} {self.model}"


class Car(Vehicle):
    """Child/Derived class - inherits from vehicle"""

    def __init(self, brand, model, year, doors):
        super().__init(brand, model, year)
        self.doors = doors  # New attribute specified to Car

    # New method specified to Car
    def honk(self):
        return "Beep Beep!"

    # new method specified to Car
    def open_trunk(self):
        return "Trunk opened"

    # Override parent method (polymorphism)
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} with {self.doors} doors"


class MotorCycle(Vehicle):
    """Another child class - inherits from Vehicle"""

    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    # New method specific to Motorcycle
    def wheelie(self):
        return "doing a wheelie!"

    # Override parent method
    def start_engine(self):
        return f"{self.brand} {self.model} revs loudly!"

    def get_info(self):
        base_info = super().get_info()
        sidecar_info = "with sidecar" if self.has_sidecar else "without sidecar"
        return f"{base_info} {sidecar_info}"


class ElectricCar(Car):
    "Multilevel inheritance - inherits from Car, which inherits from Vehicle"

    def __init__(self, brand, model, year, doors, battery_capacity):
        super().__init__(brand, model, year, doors)
        self.battery_capacity = battery_capacity

    # Override start_engine (electric cars don't have traditional engines)
    def start_engine(self):
        self._engin_running = True
        return f"{self.brand} {self.model} powers on silently"

    def charge_battery(self):
        return f"charging {self.battery_capacity}kWh battery"


# Usage examples

if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2022, 4)
    bike = MotorCycle("Harley", "Davidson", 2021, False)
    tesla = ElectricCar("Tesla", "Model 3", 2023, 4, 75)

    # Inherited methods work
    print(car.start_engine())  # Toyota Camry engine started
    print(car.get_info())  # 2022 Toyota Camry with 4 doors

    # Child_specific methods
    print(car.honk())  # Beep Beep!

    # Overridden methods
    print(bike.start_engine())  # Harley Davidson revs loudly!
    print(tesla.start_engine())  # Tesla model 3 powers on silently

    # check inheritance Relationships
    print(isinstance(car, Car))  # True
    print(isinstance(car, Vehicle))  # True (Car IS-A Vehicle)
    print(isinstance(tesla, Car))  # True (ElectricCar IS-A Car)
    print(isinstance(tesla, Vehicle))  # True (EclecticCar IS-A Vehicle)

    # Method Resolution (MRO)
    print(ElectricCar.__mro__)
    # (<class '__main__.ElectricCar'>,
    #  <class '__main__.Car'>,
    #  <class '__main__.Vehicle>,
    #  <class 'object'>)
