# Write a program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

student1 = Student(name="abhi", age=25, grade="A")

print(f"Student Name: {student1.name}")
print(f"Student Age: {student1.age}")
print(f"Student Grade: {student1.grade}")


