# 1) Create a class named Shape. Add an instance method called area. But don't define the method, just raise
# NotImplementedError() exception with a suitable message.
# 2) Make it an abstract base class by inheriting ABC class from the abc module. (To import: from abc import ABC)
# Make the area method an abstract method by decorating it with abstractmethod decorator (import this also from 
# abc).
# 3) Add 4 different subclasses for class Shape. - Triangle, Square, Pentagon, Circle.
# Define constructor for each of them to assign the necessary parameters required for calculating the area.
# Define the area method for each of the classes. When invoked it Should return the area of the shape by calculating it.
# Create an object for each of the subclasses and call the area method on the objects.


from abc import ABC,abstractmethod

class Shape(ABC):
    
    """Abstract base class representing various shapes."""
    
    @abstractmethod    
    def area(self):
      raise NotImplementedError("implement subclass")
    


class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5 * self.base * self.height
    
class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side * self.side
    
class Pentagon(Shape):
    def __init__(self,side,apothem):
        self.side = side
        self.apothem = apothem
    def area(self):
         return 0.5 * self.side * self.apothem * 5

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

triangle= Triangle(10,15)
square = Square(15)
pentagon = Pentagon(7, 3)
circle = Circle(4)

print("Triangle area:", triangle.area())
print("Square area:", square.area())
print("Pentagon area:", pentagon.area())
print("Circle area:", circle.area())

    
    
    
        
        
    