class Stack:
    def __init__(self):
        self.stack = []

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

    def brackets(self, str):  # подаем скобки на вход
        for i in (str):  # пробегаем по ним
            if i == '(':
                self.push(i)
            if i == ')' and self.size() == 0:
                return False
            if i == ')':
                self.pop()
        if self.size() == 0:
            return True
        else: return False


slack = Stack()

print(slack.brackets('(())()('))
