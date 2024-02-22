# Extend the above solution again and add another instance method called 'as_dict'. The method should return a dictionary with the data of the student. It should contain 'name', 'score', 'grade', keys and their respective values.

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.grade = self.calculate_grade()

    def calculate_grade(self):
       
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        else:
            return "D"

    def display(self):
        print(f"Name: {self.name}")
        print(f"Score: {self.score}")
        print(f"Grade: {self.grade}")

    def as_dict(self):
        return {
            "name": self.name,
            "score": self.score,
            "grade": self.grade
        }


student1 = Student(name="abhi", score=60)
student2 = Student(name="mur", score=70)

student1.display()
student2.display()

student1_data = student1.as_dict()
student2_data = student2.as_dict()

print("\nStudent 1 data as dictionary:")
print(student1_data)

print("\nStudent 2 data as dictionary:")
print(student2_data)
