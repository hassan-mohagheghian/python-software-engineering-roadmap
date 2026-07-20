# Classes - Class Attributes
# -----------------------------------------------------------------------------
# Class attributes are shared by all instances. They belong to the class
# itself, not to individual objects.
#
# Key concepts:
# 1. Defined directly in the class body
# 2. Shared across all instances
# 3. Used for constants and counters
# 4. Accessed via ClassName.attr
# -----------------------------------------------------------------------------
# Why class attributes matter:
#
# - Share data across all instances without duplicating memory
# - Define constants (e.g., PI, MAX_RETRIES)
# - Track instance counts (e.g., employee_count)
# - Set defaults that can be overridden per-instance
# -----------------------------------------------------------------------------
# High-level flow:
#
# Class defines attribute → All instances share it → Instance can shadow it
#       (shared value)         (same memory)         (local override)
# -----------------------------------------------------------------------------
# Lookup order:
#
# instance.attr
#      │
#      ├── Found on instance? → Use instance attribute
#      └── Otherwise → Look on the class
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - Employee.employee_count — track total employees
# - Config.debug = False — application-wide default
# - Circle.PI = 3.14159 — mathematical constant
# - Database.MAX_CONNECTIONS = 100 — infrastructure limit
# -----------------------------------------------------------------------------


# =============================================================================
# Basic Class Attributes
# =============================================================================


class Employee:
    company = "Acme Corp"  # class attribute
    employee_count = 0

    def __init__(self, name, role):
        self.name = name  # instance attribute
        self.role = role  # instance attribute
        type(self).employee_count += 1

    def __repr__(self):
        return f"Employee({self.name!r}, {self.role!r})"


emp1 = Employee("Alice", "Engineer")
emp2 = Employee("Bob", "Designer")

# Class attribute shared by all instances
print(f"Company: {emp1.company}")
print(f"Company: {emp2.company}")
print(f"Count: {Employee.employee_count}")

# Changing the class attribute affects every instance
Employee.company = "Tech Corp"

print(f"Updated company (emp1): {emp1.company}")
print(f"Updated company (emp2): {emp2.company}")


# =============================================================================
# Instance vs Class Attributes
# =============================================================================


class Dog:
    species = "Canis familiaris"  # class attribute

    def __init__(self, name, breed):
        self.name = name  # instance attribute
        self.breed = breed  # instance attribute


dog1 = Dog("Rex", "Labrador")
dog2 = Dog("Buddy", "Poodle")

print(f"dog1.species: {dog1.species}")
print(f"dog2.species: {dog2.species}")
print(f"Dog.species: {Dog.species}")

# Shadow the class attribute on one instance only
dog1.species = "Wolf"

print(f"dog1.species (instance): {dog1.species}")
print(f"dog2.species (class): {dog2.species}")
print(f"Dog.species: {Dog.species}")


# =============================================================================
# Class Attribute as Default
# =============================================================================


class Config:
    debug = False
    max_retries = 3

    def __init__(self, **kwargs):
        self.debug = kwargs.get("debug", Config.debug)
        self.max_retries = kwargs.get("max_retries", Config.max_retries)


default_config = Config()
custom_config = Config(debug=True, max_retries=5)

print(f"Default debug: {default_config.debug}")
print(f"Custom debug: {custom_config.debug}")


def main():
    print("=== Class Attributes ===")
    print(f"Employee count: {Employee.employee_count}")

    _emp3 = Employee("Charlie", "Manager")
    print(f"After hire: {Employee.employee_count}")


if __name__ == "__main__":
    main()
