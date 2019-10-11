class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        self.stack.pop()
        if len(self.stack) == 0:
            return None  # если стек пустой

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if len(self.stack) == 0:
            return None  # если стек пустой
        else:
            return self.stack[-1]
