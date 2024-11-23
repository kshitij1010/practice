# implment stack using queue
#
# Reference:
# https://www.youtube.com/watch?v=xBugrptVRUQ

from collections import deque

class Stack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    # method to insert in a queue
    def enqueue(self, queue, data):
        queue.append(data)
        return

    # method to deque from a queue
    def deque_elem(self, queue):
        return queue.popleft()

    # To insert into the stack
    def insert(self, data):
        self.enqueue(self.queue1, data)
        return

    # to pop from the stack
    def pop(self):
        poped_val = None
        if len(self.queue1) > 0:
            while len(self.queue1) > 1:
                val = self.deque_elem(self.queue1)
                self.enqueue(self.queue2, val)
            poped_val = self.deque_elem(self.queue1)
            self.queue1, self.queue2 = self.queue2, self.queue1
        return poped_val

s = Stack()
s.insert(1)
s.insert(2)
s.insert(3)
s.insert(4)
s.insert(5)

print (s.pop()) # 5
print (s.pop()) # 4

s.insert(7)

print (s.pop()) # 7
print (s.pop()) # 3
print (s.pop()) # 2
print (s.pop()) # 1
# print (s.pop()) # None # since no elems in the stack
