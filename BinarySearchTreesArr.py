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

