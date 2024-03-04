# Python program to for student height record for a school using Class and Objects

# Define a class 'Student' which contains the name and height of the student
class Student:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def getheight(self):
        return self.height

    def __str__(self):
        return f"{self.name}: {self.getheight()}"

# Define a function for building a height record
def HeightRecord(rec, name, height):
    rec.append(Student(name, height))
    return rec

# Initialize an empty list for the student records
Record = []

# Prompt the user to input student names and heights
x = 'y'
while x == 'y':
    name = input("Enter the name of the student: ")
    height = input("Enter the height recorded: ")
    Record = HeightRecord(Record, name, height)
    x = input("Add another student? (y/n): ")

# Display the student records
n = 1
for el in Record:
    print(f"{n}. {el}")
    n += 1
