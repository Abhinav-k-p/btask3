# Create a class Employee with name and salary attributes.
# The salary must be calculated and should be initialized to zero.
# Create a method to calculate the salary by taking the no of hours worked and multiply it by 200.You 
# can give no of hours to the method as an argument.
# Now create a child class PartTimeEmployee by inheriting the Employee class, and by using method 
# overriding (create salary calculation method in this class also with the same name)
# get the salary of part time employee by multiplying no of hours worked by 150.
# Create 3 objects for each class.
# Now implement '+' operator overloading and find the total salary expense for keeping those 
# employees by adding up the objects together.
# Eg:
# e1 = Employee(name="John")
# e1.update_salary(hours=6)
# e2 = Employee(name="Robin")
# e2.update_salary(hours=8)
# e3 = PartTimeEmployee(name="Jake")
# e3.update_salary(hours=8)
# # The below line should work.
# total_expense = e1 + e2 + e3


class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0
 
    def update_salary(self, hours, rate=200):
        self.salary = hours * rate
 
    def __str__(self):
        return f"Employee: {self.name}, Salary: ${self.salary}"
 
class PartTimeEmployee(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.rate = 150
 
    def update_salary(self, hours):
        super().update_salary(hours, self.rate)
 
 
e1 = Employee(name="Abhin")
e1.update_salary(hours=6)
e2 = Employee(name="Chithra")
e2.update_salary(hours=8)
 
p1 = PartTimeEmployee(name="Mithun")
p1.update_salary(hours=8)
p2 = PartTimeEmployee(name="Akash")
p2.update_salary(hours=4)
p3 = PartTimeEmployee(name="renjith")
p3.update_salary(hours=5)
 
 
print(e1)
print(e2)
print(p1)
print(p2)
print(p3)
 
employees = [e1, e2, p1, p2, p3]
total_expense = sum(employee.salary for employee in employees)
print(f"\nTotal Salary Expense: ${total_expense}")