from datetime import datetime

start_time = datetime.now()


class PowerSet:

    def __init__(self):
        self.line = 20
        self.step = 3
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


arr = PowerSet()
arr.put("rrrrr")
arr.put('vasya')
arr.put('forest')
arr.put('foretst')
arr.put('forwetst')
arr.put('forwetrst')
arr.put('forest')
print(arr.size())
arr.remove('utr')
arr.remove('forest')
print(arr.intersection({"rrrrr", 'vasya', 'forest', 'foretst', 'forwetst'}))
print(arr.size())
print(arr.issubset({"rrrrr", 'vasya', 'forest', 'foretst', 'forwetst'}))
print(arr.difference({"rrrrr", 'vasya', 'forest', 'foretst', 'fortreetst'}))
print(arr.union({"rrrrr", 'vasya', 'forest', 'foretst', 'fortreetst'}))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

"""1. у нас разные значения могут давать одинаковые индексы по хэшу
   2. если мы формируем множество, в котором есть только те элементы, которые имеются в каждом из множеств
   пробегаем по базовому множеству берем значение, смотрим есть ли оно вво втором множестве, если да, берем от него хэш, смотрим по этому хэшу значение,
    сравниваем с исходным если совпадает загоняем в новое итоговое множество, если не совпало но элемент есть в списке идем тройками дальше перебирая 
    все ячейки
    http://skillsmart.ru/algo/py-kf32y/s83e6f8ef537.html
    http://skillsmart.ru/algo/py-kf32y/re8af6c877.html
    """
