# OOP in Python - Association
# --------------------------------------------------------------------------------
# Association is a relationship between two classes where an object of one class
# uses an object of another class. It can be `unidirectional` or `bidirectional`.
# ------------------------------------------------------------------------------


# --------------------------- unidirectional association ---------------------------
# In this example, the Car class has an association with the Engine class. The Car class can use
# the Engine class to start the car, but the Engine class does not depend on the Car class.
# This is a unidirectional association, as the Car class is aware of the Engine class,
# but the Engine class is not aware of the Car class.
# The lifetime of the Engine object is independent of the Car object,
# meaning that the Engine can exist without the Car and vice versa.


class Engine:
    def start(self):
        print("Engine started.")


class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        self.engine.start()


if __name__ == "__main__":
    engine = Engine()
    car = Car(engine=engine)
    car.start()


# --------------------------- bidirectional association ---------------------------
# In this example, the Student class has an association with the Course class, and the Course
# class has an association with the Student class. This is a bidirectional association, as both
# classes are aware of each other. The Student class can access the Course class to enroll in
# courses, and the Course class can access the Student class to manage enrolled students.
# The lifetime of the Student and Course objects is independent of each other, meaning that
# they can exist without each other.


class Student:
    def __init__(self, name: str):
        self.name = name

    def enroll(self, course: "Course"):
        course.enroll(self)


class Course:
    def __init__(self, title: str):
        self.title = title
        self.students = []

    def enroll(self, student: Student):
        self.students.append(student)
        print(f"{student.name} has been enrolled in {self.title}.")


if __name__ == "__main__":
    student1 = Student(name="Alice")
    student2 = Student(name="Bob")

    course1 = Course(title="Python Programming")
    course2 = Course(title="Data Structures")

    student1.enroll(course1)
    student2.enroll(course1)
    student1.enroll(course2)
