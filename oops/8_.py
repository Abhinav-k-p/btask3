# show class method, static method and instance method with simple example

class Test:
    def __init__(self, val):
        self.val = val

    def display(self):
        print(f"Value: {self.val}")

obj = Test(val=30)
obj.display()