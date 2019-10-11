class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None  # если стек пустой
        return self.stack.pop(0)

    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if self.size() == 0:
            return None  # если стек пустой
        else:
            return self.stack[0]
stack = Stack()
stack.push(1)
stack.push("2")
stack.push(3.14)
print(stack.pop())
print(stack.peek())
