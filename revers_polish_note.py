class Stack:
    def __init__(self):
        self.stack = []
        self.stack_2 = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None  # если стек пустой
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() == 0:
            return None  # если стек пустой
        return self.stack[-1]

    def size_2(self):
        return len(self.stack_2)

    def pop_2(self):
        if self.size_2() == 0:
            return None  # если стек пустой
        return self.stack_2.pop()

    def push_2(self, value):
        self.stack_2.append(value)

    def peek_2(self):
        if self.size_2() == 0:
            return None  # если стек пустой
        return self.stack_2[-1]

    def reverse_polish(self, str):

        for i in reversed(str):
            self.push(i)
        while self.size() != 0:
            for i in reversed(self.stack):
                if i.isdigit():
                    self.push_2(int(i))
                    self.pop()
                if i == '+':
                    self.pop()
                    x = self.stack_2[-1] + self.stack_2[-2]
                    self.pop_2()
                    self.pop_2()
                    self.push_2(x)
                if i == '*':
                    self.pop()
                    y = self.stack_2[-1] * self.stack_2[-2]
                    self.pop_2()
                    self.pop_2()
                    self.push_2(y)
                if i == '=':
                    return self.peek_2()
stack = Stack()
print(stack.reverse_polish('123+*4+='))