class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 2**(depth+1)-1
        self.Tree = [None] * tree_size  # массив ключей

    def FindKeyIndex(self, key):
        arr = self.Tree
        if arr[0] == None:  # предусматриваем вставку корневого ключа если массив пуст
             return 0
        if arr[0] != None:
            index = 0
            while True:  # предусматриваем совпадение узлов также выход узла за диапазон
                if arr[index] == key:  # узел найден если значение узла и вставляемого узла равны
                    return index
                if arr[index] > key:  # левый потомак
                    index = 2 * index + 1  # передвигаем переменную с которой сравниваем key по массиву с помощью формулы детей
                    if index > len(arr) - 1:  # отслеживаем выход индекса за диапазон
                        return None
                    if arr[index] == None: # eсли искомый индекс попадает на незаполненное место в массиве
                        return -index
                if arr[index] < key:  # правай потомак
                    index = 2 * index + 2
                    if index > len(arr) - 1:  # отслеживаем выход индекса за диапазон
                        return None
                    if arr[index] == None: # eсли искомый индекс попадает на незаполненное место в массиве
                        return -index

    def AddKey(self, key):
        arr = self.Tree
        if arr[0] == None:# предусматриваем вставку корневого ключа если массив пуст
            arr[0] = key# добавляем ключ в массив
            return 0
        if arr[0] != None:
            index = 0
            while True: # предусматриваем совпадение узлов также выход узла за диапазон
                if 2 * index + 1 > len(arr) or 2 * index + 2 > len(arr): # отслеживаем выход индекса за диапазон
                    return -1
                if arr[index] == key: # если значение узла и вставляемого узла равны
                    return
                if arr[index] > key and arr[2 * index + 1] != None:# левый потомак
                    index = 2 * index + 1 #передвигаем переменную с которой сравниваем key по массиву с помощью формулы детей
                if 2 * index + 1 > len(arr) or 2 * index + 2 > len(arr):# отслеживаем выход индекса за диапазон
                    return -1
                if arr[index] > key and arr[2 * index + 1] == None:
                    index = 2 * index + 1
                    arr[index] = key
                    return index
                if arr[index] < key and arr[2 * index + 2] != None: # правай потомак
                    index = 2 * index + 2
                if 2 * index + 1 > len(arr) or 2 * index + 2 > len(arr):# отслеживаем выход индекса за диапазон
                    return -1
                if arr[index] < key and arr[2 * index + 2] == None:
                    index = 2 * index + 2
                    arr[index] = key
                    return index

tree = aBST(0)
# tree.AddKey(50)
# tree.AddKey(25)
# tree.AddKey(75)
# tree.AddKey(37)
# tree.AddKey(62)
# tree.AddKey(84)
# tree.AddKey(31)
# tree.AddKey(43)
# tree.AddKey(55)
# tree.AddKey(92)
# tree.AddKey(98)
print(tree.FindKeyIndex(55))
#print(tree.FindKeyIndex(26))
#полное дерево
# tree = aBST(3)
# tree.AddKey(4)  # формируем дерево
# tree.AddKey(12)
# tree.AddKey(2)
# tree.AddKey(6)
# tree.AddKey(10)
# tree.AddKey(14)
# tree.AddKey(1)
# tree.AddKey(3)
# tree.AddKey(5)
# tree.AddKey(7)
# tree.AddKey(9)
# tree.AddKey(11)
# tree.AddKey(13)
# tree.AddKey(15)
# print(tree.FindKeyIndex(55))
# прогнать тесты
# ноль нод
# одна нода
# две ноды
# три нодв с листами
# полное бинарное дерево
# с ним тоже все тесты