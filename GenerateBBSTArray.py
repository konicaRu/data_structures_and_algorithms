
def GenerateBBSTArray(arr):
    if arr == []:
        return []
    arr = sorted(arr)
    arr_res = [None] * len(arr)
    return Bst(arr_res,  _createBalancedTree(arr, 0, len(arr) - 1))

arr_res2 = []
def _createBalancedTree(arr, start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    node = arr[mid]
    arr_res2.append(node)
    node_left = _createBalancedTree(arr, start, mid - 1)
    node_right = _createBalancedTree(arr, mid + 1, end)
    return arr_res2


def Bst(arr_res, arr_res2):
    arr_res[0] = arr_res2[0]
    for node in arr_res2[1:]:
        index = 0
        while True:
            if 2 * index + 1 > len(arr_res) or 2 * index + 2 > len(arr_res):  # отслеживаем выход индекса за диапазон
                return
            if arr_res[index] > node and arr_res[2 * index + 1] != None:  # левый потомак
                index = 2 * index + 1  # передвигаем переменную с которой сравниваем key по массиву с помощью формулы детей
            if arr_res[index] > node and arr_res[2 * index + 1] == None:
                index = 2 * index + 1
                arr_res[index] = node  # вставляем левого потомка
                break
            if arr_res[index] < node and arr_res[2 * index + 2] != None:  # правай потомак
                index = 2 * index + 2
            if arr_res[index] < node and arr_res[2 * index + 2] == None:
                index = 2 * index + 2
                arr_res[index] = node  # вставляем правого потомка
                break
    return arr_res
