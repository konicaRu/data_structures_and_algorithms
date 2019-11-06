from datetime import datetime

start_time = datetime.now()


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

    def intersection(self, set2):
        arr = []
        for i in set2:
            if i in self.slots:  # пересечение текущего множества и set2
                arr.append(i)
        return arr

    def union(self, set2):
        for i in set2:
            if self.get(i) == True:  # объединение текущего множества и set2
                continue
            else:
                self.put(i)
            return self.slots

    def difference(self, set2):
        inter_set = []
        for i in self.slots:
            if i not in set2:  # пересечение текущего множества и set2
                inter_set.append(i)
        return inter_set
        # разница текущего множества и set2

    def issubset(self, set2):
        count = 0
        for i in set2:
            if i in self.slots:
                count += 1
        if count == len(set2):
            return True
        else:
            return False


arr = PowerSet()
arr.put("rrrrr")
arr.put('vasya')
arr.put('forest')
arr.put('foretst')
arr.put('forwetst')
arr.put('foretst')
arr.put('foretst')
# arr.remove('utr')
# arr.remove('forest')
print(arr.intersection({"rrrrr3", 'vasya', 'forest', 'foretst', 'fortreetst'}))
print(arr.union({"rrrrr3", 'vasya', 'forest', 'foretst', 'fortreetst'}))
print(arr.difference({"rrrrr3", 'vasya', 'forest', 'foretst', 'fortreetst'}))
print(arr.issubset({"rrrrr", 'vasya', 'forest', 'foretst', 'fortreetst'}))
print(arr.size())
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
