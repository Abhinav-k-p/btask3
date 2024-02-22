# Write a program that prints the class name using its object

class testing:
    pass

obj = testing()
class_name = obj.__class__.__name__
print(f"Class name using __class__: {class_name}")
