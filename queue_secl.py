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
            return
        for i in range(step):
            self.enqueue(self.dequeue())
        return



qu = Queue()
qu.enqueue(125)

while qu.size()> 0:
    print(qu.dequeue())

