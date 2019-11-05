class PowerSet:

    def __init__(self):
        self.line = 20000
        self.slots = [None] * self.line  # создает массив с size количеством слотов

    def size(self):
        count = 0
        for i in self.slots:
            if i != None:
                count += 1
        return count
        # количество элементов в множестве

    def put(self, value):
        if value in self.slots:
            return
        inter_set = self.slots
        return inter_set.append(value)

    def get(self, value):
        if value in self.slots:
            return True  # возвращает True если value имеется в множестве,
        else:  # иначе False
            return False

    def remove(self, value):
        if self.get(value) == True:
            self.slots.remove(value)  # возвращает True если value удалено
            return
        else:  # иначе False
            return False

    def intersection(self, set2):
        inter_set = set(self.slots)
        return inter_set & set2

    def union(self, set2):
        inter_set = set(self.slots)
        return inter_set | set2

    def difference(self, set2):
        inter_set = set(self.slots)
        return inter_set - set2

    def issubset(self, set2):
        inter_set = set(self.slots)
        if set2 <= inter_set:
            return True
        else:
            return False
