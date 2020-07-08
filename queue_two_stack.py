class Queue:
    def __init__(self):
        self.queue_1 = []
        self.queue_2 = []

    def enqueue(self, item):
        return self.queue_1.append(item)


    def copy(self):
        self.queue_2.append(self.queue_1[-1])
        self.queue_1.pop()


    def dequeue(self):
        if self.size_1() == self.size_2() == 0:
            return None  # если очередь пустая
        if self.size_2() == 0:
            while self.size_1() != 0:
                self.copy()
        first_el = self.queue_2[-1]
        self.queue_2.pop()
        return first_el

    def size_1(self):
        return len(self.queue_1)

    def size_2(self):
        return len(self.queue_2)

qu = Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(4)
qu.dequeue()
qu.enqueue(5)
print(qu.dequeue())

 
