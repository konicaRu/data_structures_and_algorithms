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

  def brackets (self, str):# подаем скобки на вход
      count = 0
      for i in reversed(str):# пробегаем их с зади чтобы начало в стеке было сверху
          self.push(i)# набиваем стек
      for i in range(self.size()):#бегаем по стеку
          if self.peek() == '(': #если верхний элемент
              count += 1
              self.pop()
          else:
              count -= 1
              self.pop()
      if 0 > count or count > 0:
          print('Folse')
      if count == 0:
          print('True')
slack = Stack()
slack.brackets('(())()')
