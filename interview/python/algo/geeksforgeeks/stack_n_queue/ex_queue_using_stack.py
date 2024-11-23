# implment queue using stack
#
# Reference:
# https://www.youtube.com/watch?v=n1nsfg8O4Mk


class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue_helper(self, data):
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(data)

        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())

    def enqueue(self, data):
        if len(self.stack1) == 0:
            self.stack1.append(data)
        else:
            self.enqueue_helper(data)
        return

    def deque(self):
        elem = None
        if len(self.stack1) > 0:
            elem = self.stack1.pop()
        return elem


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(7)

print (q.deque()) # 1
print (q.deque()) # 2
print (q.deque()) # 7
