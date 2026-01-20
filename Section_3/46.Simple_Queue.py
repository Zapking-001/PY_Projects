"""
Docstring for Section_3.46.Simple_Queue

            Efficiency : Time complexity: O(1)
                         Space complexity: O(n)
                         Where n is the number of elements in the queue.
"""

# Method - 1
from collections import deque

class QueueEfficient:
    def __init__(self):
        self.queue = deque()
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.popleft() if self.queue else None
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)

# Method - 2
x = input("Enter the object: ")
queue = []
queue.append(x) # Enqueue
queue.pop(0) if queue else None # Dequeue

# Method - 3
class QueueMath:
    def __init__(self):
        self.items = []
        self.head = 0
    def enqueue(self, x):
        self.items.append(x)
    def dequeue(self):
        if self.head < len(self.items):
            val = self.items[self.head]
            self.head += 1
            return val
        return None

for x in range(int(input("Enter the number of elements to enqueue: "))):
    QueueMath().enqueue(input("Enter the object: "))
