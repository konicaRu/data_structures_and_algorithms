class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:
    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов
        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


vizit = []  # надо предусмотреть если корень нана или только один корень
stack = []

class BST:
    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key):
        cursor_node = self.Root
        BSTFind.NodeHasKey = False
        if cursor_node == None:
            BSTFind.Node = None
            return BSTFind
        while True:
            if cursor_node.NodeKey == key:
                BSTFind.NodeHasKey = True
                BSTFind.Node = cursor_node
                return BSTFind
            if cursor_node.NodeKey < key and cursor_node.RightChild != None:
                cursor_node = cursor_node.RightChild
                BSTFind.Node = cursor_node
            if cursor_node.NodeKey < key and cursor_node.RightChild == None:
                BSTFind.Node = cursor_node
                BSTFind.ToLeft = False
                return BSTFind
            if cursor_node.NodeKey > key and cursor_node.LeftChild != None:
                cursor_node = cursor_node.LeftChild
                BSTFind.Node = cursor_node
            if cursor_node.NodeKey > key and cursor_node.LeftChild == None:
                BSTFind.Node = cursor_node
                BSTFind.ToLeft = True
                return BSTFind

    def AddKeyValue(self, key, val):
        self.FindNodeByKey(key)
        if BSTFind.Node == None or BSTFind.NodeHasKey == True:
            return False
        if BSTFind.ToLeft == False:
            node = BSTNode(key, val, BSTFind.Node)
            BSTFind.Node.RightChild = node
            return True
        if BSTFind.ToLeft == True:
            node = BSTNode(key, val, BSTFind.Node)
            BSTFind.Node.LeftChild = node
            return True

    def WideAllNodes(self):
        vizit = []  # надо предусмотреть если корень нана или только один корень
        stack = []
        node = self.Root
        if node == None:
            return tuple ()
        vizit.append(node)
        if node.LeftChild != None:
            stack.append(node.LeftChild)
        if node.RightChild != None:
            stack.append(node.RightChild)
        if node.LeftChild == None and node.RightChild == None:
            return tuple(vizit)
        while True:
            node = stack[0]
            if node.LeftChild != None:
                stack.append(node.LeftChild)
            if node.RightChild != None:
                stack.append(node.RightChild)
            vizit.append(node)
            stack.pop(0)
            if len(stack) == 0:
                break
        return tuple(vizit)


    def DeepAllNodes(self, order):
        node = self.Root
        if node == None:
            return tuple ()
        if order == 2:
            return tuple (self.PreOrder(node))
        if order == 0:
            return tuple (self.InOrder(node))
        if order == 1:
            return tuple (self.PostOrder(node))

    def PreOrder(self, root):  # Root -> Left ->Right
        res = []
        if root:
            res.append(root)
            res = res + self.PreOrder(root.LeftChild)
            res = res + self.PreOrder(root.RightChild)
        return res

    def InOrder(self, root):  # Left -> Root -> Right
        res = []
        if root:
            res = self.InOrder(root.LeftChild)
            res.append(root)
            res = res + self.InOrder(root.RightChild)
        return res

    def PostOrder(self, root):  # Left ->Right -> Root
        res = []
        if root:
            res = self.PostOrder(root.LeftChild)
            res = res + self.PostOrder(root.RightChild)
            res.append(root)
        return res
