class HeapSort:

    def __init__(self, a):
        self.arr = a
        self.HeapObject = [None] * len(self.arr)  # создаем итоговый архив с нанами
        for i in range(len(self.arr)):  # пробегаем  по данным исходного массива начиная со второго тк первый уже вставили
            self.Add(a[i])

    def GetNextMax(self):
        if len(self.HeapObject) == self.HeapObject.count(None):
            return -1
        count = len(self.HeapObject) - self.HeapObject.count(None)
        index = 0
        root = self.HeapObject[0]
        self.HeapObject[0] = self.HeapObject[count - 1]
        self.HeapObject[count - 1] = None
        while True:  # if self.HeapObject[2]== None and self.HeapObject[0] < self.HeapObject[1]  меняем местами
            if 2 * index + 1 >= count - 2 or 2 * index + 2 >= count - 2:
                return root
            if self.HeapObject[2 * index + 2] >= self.HeapObject[2 * index + 1]:
                swapR = self.HeapObject[index]
                self.HeapObject[index] = self.HeapObject[2 * index + 2]
                self.HeapObject[2 * index + 2] = swapR
                index = 2 * index + 2
            if 2 * index + 1 >= count - 2 or 2 * index + 2 >= count - 2:
                return root
            if self.HeapObject[2 * index + 2] <= self.HeapObject[2 * index + 1]:
                swapL = self.HeapObject[index]
                self.HeapObject[index] = self.HeapObject[2 * index + 1]
                self.HeapObject[2 * index + 1] = swapL
                index = 2 * index + 1

    def Add(self, key):
        count = len(self.HeapObject) - self.HeapObject.count(None)
        if None not in self.HeapObject:
            return False  # если куча вся заполнена
        self.HeapObject[count] = key
        while self.HeapObject[count] > self.HeapObject[int((count - 1) / 2)]:  # если элемент больше родителя
            swap = self.HeapObject[int((count - 1) / 2)]  # сохраняем значение родителя в переменной
            self.HeapObject[int((count - 1) / 2)] = self.HeapObject[count]  # меняем значение  родителя на ребенка
            self.HeapObject[count] = swap  # меняем значение ребенка на родителя
            count = int((count - 1) // 2)  # увеличивваем индекс на родительский


        # УДбРАТЬ ВЫВОД МАССИВА ИЗ return
    # ошибка при максимуме 10 и 5
    # добавление сделать отдельным кодом


#a = [110, 9, 40, 70, 80, 30, 10, 20, 50, 60, 65, 31, 29, 11, 90]
#a = [1, 1, 1, 2, 3, 4, 5, 6, 7]
# a = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# a = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
# a = [4, 10, 3, 5, 1, 2, 8]
# a = [6, 5, 2, 1, 3, 8, 11, 4, 9, 7]
#a = []
# a = [5, 6]
# a = [4, 5] #если 2 элемента придобавлени большего и послед удалением максимального получается неправильная пирамида
#a = [6, 5, 2] # некорректно работет при удалении максимального элемента поочередно когда остается 2 элемента
#a = [5, 6, 2]
#a = [2, 5, 6]
a = [5, 8, 6, 3]  # некорректно работет некорректно работет при удалении максимального элемента поочередно когда остается 2 элемента

# a = [5, 11, 7]
# a = [5, 7, 8]
# a = [5, 7, 8, 4]
# a = [5, 7, 8, 4, 10]
heap = HeapSort(a)
print(heap.GetNextMax())
print(heap.GetNextMax())
print(heap.GetNextMax())
print(heap.GetNextMax())
print(heap.GetNextMax())
print(heap.GetNextMax())
print(heap.GetNextMax())
print(heap.GetNextMax())
print(heap.GetNextMax())


# print(heap.Add(11))
# должно получиться из [4, 10, 3, 5, 1] -> [10, 5, 3, 4, 1]
# a = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17] -> [17, 15, 13, 9, 6 , 5, 10 , 4, 8, 3, 1]
