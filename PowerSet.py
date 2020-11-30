class PowerSet:

    def __init__(self):
        self.line = 20000
        self.step = 3
        self.slots = [None] * self.line  # создает массив с size количеством слотов

    def size(self):
        count = 0
        for i in self.slots:
            if i != None:
                count += 1
        return count
        # количество элементов в множестве

    def hash_fun(self, value):  # в качестве value поступают строки!
        hash = sum(map(ord, value)) % self.line  # всегда возвращает корректный индекс слота
        return hash  # суммируем значения кодов символов строки, и потом их брать по модулю размера таблицы.

    def put(self, value):
        num = self.hash_fun(value)
        count = 0
        if value in self.slots:  # если значение уже есть во множестве
            return
        else:
            while None in self.slots:
                if self.slots[num] == None:
                    self.slots[num] = value
                    return
                if self.slots[num] != None:
                    num += self.step
                if num > self.line - 1:  # находит индекс пустого слота для значения, или None
                    num = count
                    count += 1
            return None

    def get(self, value):
        if value in self.slots:
            return True  # возвращает True если value имеется в множестве,
        else:  # иначе False
            return False

    def remove(self, value):
        if self.get(value) == True:
            num = self.hash_fun(value)  # возвращает True если value удалено
            self.slots[num] = None
            return True
        else:  # иначе False
            return False

    def intersection(self, set2):
        inter_set = []
        for i in self.slots:
            if i in set2:  # пересечение текущего множества и set2
                inter_set.append(i)
        end_set = set(inter_set)
        return end_set

    def union(self, set2):
        for i in set2:
            if i in self.slots:  # объединение текущего множества и set2
                continue
            else:
                self.put(i)
        return self.slots

    def difference(self, set2):
        inter_set = []
        for i in self.slots:
            if i not in set2 and i != None:  # пересечение текущего множества и set2
                inter_set.append(i)
        end_set = set(inter_set)
        return end_set
        # разница текущего множества и set2

    def issubset(self, set2):
        count = 0
        for i in set2:
            if i in self.slots and i != None:
                count += 1
        if count == len(set2):
            return True
        else:
            return False
 

