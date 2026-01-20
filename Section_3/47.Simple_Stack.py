"""
Docstring for Section_3.47.Simple_Stack

            Efficiency : Time complexity: O(1)
                         Space complexity: O(n)
                         Where n is the number of elements in the stack.
"""

# Method - 1
class StackEfficient:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop() if self.stack else None
    

# Method - 2
x = input("Enter the object: ")
stack = []
stack.append(x) # Push
stack.pop() if stack else None # Pop

# Method - 3

class StackMath:
    def __init__(self, size):
        self.data = [None] * size
        self.top = -1
    def push(self, x):
        self.top += 1
        self.data[self.top] = x
    def pop(self):
        val = self.data[self.top]
        self.top -= 1
        return val if val is not None else None
    
for x in range(int(input("Enter the number of elements to push: "))):
    StackMath(int(input("Enter the size of the stack: "))).push(input("Enter the object: "))