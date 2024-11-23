# 201. implement stack with List



class Stack():
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack) <= 0:
            return "Empty stack"
        return self.stack.pop()

    def top(self):
        if len(self.stack) <= 0:
            return "Empty stack"
        return self.stack[-1]


stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(100)
stack1.push(200)
stack1.push(300)

print ("Top elem:", stack1.top())
print (stack1.stack)

print (stack1.pop())
print (stack1.pop())
print (stack1.pop())
print (stack1.pop())
print (stack1.pop())
print (stack1.pop()) # popping last element of the stack
print ("Top elem:", stack1.top())
