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
        arr_end = PowerSet()
        for i in set2.slots:
            if self.get(i) == True:
                arr_end.put(i)
        return arr_end


    def union(self, set2):
        arr_end = PowerSet()
        if len(set2.slots) == 0 or self.size() == 0:
            return arr_end
        for i in self.slots:
            arr_end.put(i)
        for i in set2.slots:
            if self.get(i) == False:  # объединение текущего множества и set2
                arr_end.put(i)
        return arr_end

    def difference(self, set2):  # self.slots = ['1', '2', '3', '4'] set2 = ['1', '2']
        arr_end = PowerSet()
        for i in self.slots:
            if set2.get(i) == False:  # в качестве параметра выступает другое множество,
                arr_end.put(i)  # а возвращается подмножество текущего множества из таких элементов, которые не входят в множество-параметр;
        return arr_end

    def issubset(self, set2):
        count = 0
        for i in self.slots:
            for j in set2.slots:  # пересечение текущего множества и set2
                if i == j:
                    count += 1
        if count == len(set2.slots):
            return True
        else:
            return False
