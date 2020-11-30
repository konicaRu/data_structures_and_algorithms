class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, a, depth):
        self.HeapArray = [None] * (2 ** (depth + 1) - 1)  # создаем итоговый архив с нанами
        if len(a) == 0:
            return self.HeapArray
        # a = a[::-1]  # переворачиваем массив чтобы работать с последнего элемента
        self.HeapArray[0] = a[0]  # сразу ставим первый элемент
        for i in range(1, len(a)):  # пробегаем  по данным исходного массива начиная со второго тк первый уже вставили
            self.HeapArray[i] = a[i]  # вставляем элемент на первое свободное поле
            while self.HeapArray[i] > self.HeapArray[int((i - 1) / 2)]:  # если элемент больше родителя
                swap = self.HeapArray[int((i - 1) / 2)]  # сохраняем значение родителя в переменной
                self.HeapArray[int((i - 1) / 2)] = self.HeapArray[i]  # меняем значение  родителя на ребенка
                self.HeapArray[i] = swap  # меняем значение ребенка на родителя
                i = int((i - 1) // 2)  # увеличивваем индекс на родительский

        return self.HeapArray

    def GetMax(self):
        count_N = 0
        for i in self.HeapArray:
            if i == None:
                count_N += 1
        if len(self.HeapArray) == count_N:
            return -1  # если куча пуста состоит из None
        if len(self.HeapArray) - 1 == count_N:  # если куча  состоит из одного элемента
            return -1
        count = 0
        index = 0
        for i in self.HeapArray:
            if i != None:
                count += 1
        root =  self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[count - 1]
        self.HeapArray[count - 1] = None
        while True:
            if 2 * index + 1 > count - 2 or 2 * index + 2 > count - 2:
                return root, self.HeapArray
            if self.HeapArray[2 * index + 2] > self.HeapArray[2 * index + 1]:
                swapR = self.HeapArray[index]
                self.HeapArray[index] = self.HeapArray[2 * index + 2]
                self.HeapArray[2 * index + 2] = swapR
                index = 2 * index + 2
            if 2 * index + 1 > count - 2 or 2 * index + 2 > count - 2:
                return root, self.HeapArray
            if self.HeapArray[2 * index + 2] < self.HeapArray[2 * index + 1]:
                swapL = self.HeapArray[index]
                self.HeapArray[index] = self.HeapArray[2 * index + 1]
                self.HeapArray[2 * index + 1] = swapL
                index = 2 * index + 1

    def Add(self, key):
        count = 0
        if None not in self.HeapArray:
            return False  # если куча вся заполнена
        for i in self.HeapArray:
            if i != None:
                count += 1
        self.HeapArray[count] = key
        while self.HeapArray[count] > self.HeapArray[int((count - 1) / 2)]:  # если элемент больше родителя
            swap = self.HeapArray[int((count - 1) / 2)]  # сохраняем значение родителя в переменной
            self.HeapArray[int((count - 1) / 2)] = self.HeapArray[count]  # меняем значение  родителя на ребенка
            self.HeapArray[count] = swap  # меняем значение ребенка на родителя
            count = int((count - 1) // 2)  # увеличивваем индекс на родительский

        return self.HeapArray

        # УДбРАТЬ ВЫВОД МАССИВА ИЗ return
    # ошибка при максимуме 10 и 5
    # добавление сделать отдельным кодом


#a = [110, 9, 40, 70,80, 30,10, 20,50, 60,65, 31,29, 11, 90]
a =  [1,1,1,2,3,4,5,6,7]
# a = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# a = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
#a = [4, 10, 3, 5, 1, 2, 8]
#a = [6, 5, 2, 1, 3, 8, 11, 4, 9, 7]
#a = []
# a = [5]
# a = [4, 5] #если 2 элемента придобавлени большего и послед удалением максимального получается неправильная пирамида
# a = [5, 11, 7]
#a = [5, 8, 6, 3]
# a = [5, 7, 8, 4]
#a = [5, 7, 8, 4, 10]
#a = [6, 5, 2]
heap = Heap()
print(heap.MakeHeap(a, 3))
print(heap.GetMax())
print(heap.GetMax())
print(heap.GetMax())
print(heap.GetMax())
print(heap.GetMax())
print(heap.GetMax())
print(heap.GetMax())
print(heap.GetMax())
print(heap.GetMax())
# print(heap.Add(6))
# print(heap.Add(8))

# print(heap.Add(11))
# должно получиться из [4, 10, 3, 5, 1] -> [10, 5, 3, 4, 1]
# a = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17] -> [17, 15, 13, 9, 6 , 5, 10 , 4, 8, 3, 1]
