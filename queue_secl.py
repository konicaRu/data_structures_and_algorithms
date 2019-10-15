class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        return self.queue.append(item)
        # вставка в хвост

    def dequeue(self):
        if self.size() == 0:
            return None  # если очередь пустая
        first_el = self.queue[0]
        self.queue.pop(0)
        return first_el

    def size(self):
        return len(self.queue)

    def round (self, step):
        if self.size() == 0:
            return f'Size List {self.size()}'
        if self.size() == 1:
            return self.queue
        for i in range(step):
            self.enqueue(self.queue[0])
            self.queue.pop(0)
        return self.queue



qu = Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
print(qu.round(2))

