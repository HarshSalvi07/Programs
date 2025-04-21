class Stack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)
        return True

    def pop(self):
        self.stack.pop(-1)
        return True

    def isEmpty(self):
        return len(self.stack) == 0

    def length(self):
        return len(self.stack)

    def print(self):
        print(self.stack)

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.print()

stack.pop()
stack.pop()

stack.print()

print(stack.isEmpty())
print(stack.length())
