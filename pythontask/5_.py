# Write a Python program to implement a stack using a list.(push and pop)


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty.")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print("Popped item:", my_stack.pop())
print("Popped item:", my_stack.pop())
print("Stack size:", my_stack.size())
