arr_res2 = []
class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 1

class BalancedBST:

    def __init__(self):
        self.Root = None

    def FindNodeByKey(self, key):
        cursor_node = self.Root
        if cursor_node == None:
            return None
        while True:
            if cursor_node.NodeKey == key and (cursor_node.RightChild == None or cursor_node.RightChild.NodeKey != key):
                return cursor_node
            if cursor_node.NodeKey == key and cursor_node.RightChild.NodeKey == key:
                cursor_node = cursor_node.RightChild
            if cursor_node.NodeKey < key and cursor_node.RightChild != None:
                cursor_node = cursor_node.RightChild
            if cursor_node.NodeKey < key and cursor_node.RightChild == None:
                return cursor_node
            if cursor_node.NodeKey > key and cursor_node.LeftChild != None:
                cursor_node = cursor_node.LeftChild
            if cursor_node.NodeKey > key and cursor_node.LeftChild == None:
                return cursor_node



    def _createBalancedTree(self, arr, start, end):
        if end < start:
            return None
        mid = (start + end) // 2
        node = arr[mid]
        arr_res2.append(node)
        node_left = self._createBalancedTree(arr, start, mid - 1)
        node_right = self._createBalancedTree(arr, mid + 1, end)
        return arr_res2

    def GenerateTree(self, a):
        a = sorted(a)
        a = self._createBalancedTree(a, 0, len(a) - 1)
        arr_res = [None] * (len(a) + 1)
        arr_res[0] = a[0]
        cursor_node = BSTNode(a[0], None)
        self.Root = cursor_node
        for node in a[1:]:
            index = 0
            while True:
                if 2 * index + 1 > len(arr_res) or 2 * index + 2 > len(arr_res):
                    return
                if arr_res[index] > node and arr_res[2 * index + 1] != None:
                    index = 2 * index + 1
                if (2 * index + 2) > len(arr_res) - 1:
                     arr_res = arr_res + ([None] * ((2 * index + 2) -  len(arr_res)))
                if arr_res[index] > node and arr_res[2 * index + 1] == None:
                    index = 2 * index + 1
                    arr_res[index] = node  # вставляем левого потомка
                    cursor_node = self.FindNodeByKey(arr_res[int((index - 1) / 2)])
                    cursor_node2 = BSTNode(arr_res[index], cursor_node)
                    cursor_node2.Level = cursor_node.Level + 1
                    cursor_node.LeftChild = cursor_node2
                    break
                if arr_res[index] <= node and arr_res[2 * index + 2] != None:  # правай потомак
                    index = 2 * index + 2
                if (2 * index + 2) > len(arr_res) - 1:
                     arr_res = arr_res + ([None] * ((2 * index + 3) - len(arr_res)))
                if arr_res[index] <= node and arr_res[2 * index + 2] == None:
                    index = 2 * index + 2
                    arr_res[index] = node
                    cursor_node = self.FindNodeByKey(arr_res[int((index - 1) / 2)])
                    cursor_node2 = BSTNode(node, cursor_node)
                    cursor_node2.Level = cursor_node.Level + 1
                    cursor_node.RightChild = cursor_node2
                    break
        return True

    def IsBalanced(self, root_node):
        vizit = []
        stack = []
        node = root_node
        if node == None:
            return 0
        if node.LeftChild != None:
            stack.append(node.LeftChild)
        if node.RightChild != None:
            stack.append(node.RightChild)
        if node.LeftChild == None and node.RightChild == None:
            return True
        while len(stack) != 0:
            node = stack[0]
            if node.LeftChild != None:
                stack.append(node.LeftChild)
            if node.RightChild != None:
                stack.append(node.RightChild)
            if node.LeftChild == None and node.RightChild == None:
             vizit.append(node.Level)
            stack.pop(0)
        if abs(max(vizit) - min(vizit)) <= 1:
            return True

        return False



