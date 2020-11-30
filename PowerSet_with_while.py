class PowerSet:
    def __init__(self):
        self.slots = []  # создает массив под множество

    def size(self):
        return len(self.slots)
        # количество элементов в множестве

    def put(self, value):
        if self.get(value) == True:  # если значение уже есть во множестве
            return
        else:
            self.slots.append(value)

    def get(self, value):
        if value in self.slots:
            return True  # возвращает True если value имеется в множестве,
        else:  # иначе False
            return False

    def remove(self, value):
        if self.get(value) == True:  # возвращает True если value удален
            self.slots.remove(value)
            return True
        else:  # иначе False
            return False

    # а возвращается пересечение этих множеств (множество, в котором есть только те элементы, которые имеются в каждом из множеств);
    def intersection(self, set2):#в качестве параметра выступает другое множество,
        arr_end = []
        count = 0
        while count < len(set2):
            count +=1
            i = set2[count - 1]
            if self.get(i) == True:
                arr_end.append(i)
        self.slots = arr_end
        return self.slots

    def union(self, set2):
        if len(set2) == 0 or self.size() == 0:
            return None
        for i in set2:
            if self.get(i) == True:  # объединение текущего множества и set2
                continue
            else:
                self.put(i)
        return self.slots

    def difference(self, set2):  # self.slots = ['1', '2', '3', '4'] set2 = ['1', '2']
        arr = []
        for i in self.slots:
            if i in set2:  # пересечение текущего множества и set2
                arr.append(i)
        if len(arr) == 0:
            return None
        for j in arr:
            self.slots.remove(j)
        return self.slots

    def issubset(self, set2):
        count = 0
        for i in set2:
            if i in self.slots:
                count += 1
        if count == len(set2):
            return True
        else:
            return False

