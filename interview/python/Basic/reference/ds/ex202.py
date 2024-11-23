# 202. Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time.




class Stack():
    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val):
        if len(self.minimum) > 0:
            self.minimum.append(min(self.minimum[-1], val))
        else:
            self.minimum.append(val)
        self.stack.append(val)

    def pop(self):
        if len(self.stack) <= 0:
            return "Empty stack"
        self.minimum.pop()
        return self.stack.pop()

    def min(self):
        if len(self.stack) <= 0:
            return "Empty stack"
        return self.minimum[-1]


stack1 = Stack()
stack1.push(3)
stack1.push(100)
stack1.push(2)
stack1.push(200)
stack1.push(300)
stack1.push(1)

print (stack1.stack)
print (stack1.minimum)
print ("min:", stack1.min())

print ("popped:", stack1.pop())
print ("min:", stack1.min())
print ("popped:", stack1.pop())
print ("min:", stack1.min())
print ("popped:", stack1.pop())
print ("min:", stack1.min())
print ("popped:", stack1.pop())
print ("min:", stack1.min())
print ("popped:", stack1.pop())
print ("min:", stack1.min())
print ("popped:", stack1.pop()) # popping last element of the stack
print ("min:", stack1.min()) # empty
print ("popped:", stack1.pop()) # empty
