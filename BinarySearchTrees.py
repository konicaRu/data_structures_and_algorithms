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
          return  False
        if BSTFind.ToLeft == False:
           node = BSTNode(key, val, BSTFind.Node)
           BSTFind.Node.RightChild = node
           return
        if BSTFind.ToLeft == True:
           node = BSTNode(key, val, BSTFind.Node)
           BSTFind.Node.LeftChild = node
           return

    def FinMinMax(self, FromNode, FindMax):
        cursor_node = FromNode.Node
        if FindMax == True:
            while cursor_node.RightChild != None:
                cursor_node = cursor_node.RightChild
                if cursor_node.RightChild == None:
                    return cursor_node
        if FindMax == False:
            while cursor_node.LeftChild != None:
                cursor_node = cursor_node.LeftChild
                if cursor_node.LeftChild == None:
                    return cursor_node
    def DeleteNodeByKey(self, key):
        self.FindNodeByKey(key)
        del_node = BSTFind.Node
        if BSTFind.NodeHasKey == False:
            return False
        if del_node.LeftChild == None and del_node.RightChild == None and del_node.Parent.RightChild == del_node:
            del_node.Parent.RightChild = None
            del_node.Parent = None
            BSTFind.Node = None
            return
        if del_node.LeftChild == None and del_node.RightChild == None and del_node.Parent.LeftChild == del_node:
            del_node.Parent.LeftChild = None
            del_node.Parent = None
            BSTFind.Node = None
            return
        if del_node.LeftChild != None and del_node.RightChild == None:
            del_node.LeftChild.Parent = del_node.Parent
            if del_node.Parent.LeftChild == del_node:
                del_node.Parent.LeftChild = del_node.LeftChild
                BSTFind.Node = None
                return
            if del_node.Parent.RightChild == del_node:
                del_node.Parent.RightChild = del_node.LeftChild
                BSTFind.Node = None
                return
        if del_node.LeftChild == None and del_node.RightChild != None:
            del_node.RightChild.Parent = del_node.Parent
            if del_node.Parent.LeftChild == del_node:
                del_node.Parent.LeftChild = del_node.RightChild
                BSTFind.Node = None
                return
            if del_node.Parent.RightChild == del_node:
                del_node.Parent.RightChild = del_node.RightChild
                BSTFind.Node = None
                return
        if del_node.LeftChild != None and del_node.RightChild != None:
            stop_node = del_node
            del_node = del_node.RightChild
            count = 0
            while count == 0:
                if del_node.LeftChild == None and del_node.RightChild == None:
                    del_node.Parent = stop_node.Parent
                    if stop_node.Parent.LeftChild == stop_node:
                        stop_node.Parent.LeftChild = stop_node.RightChild
                        stop_node.LeftChild.Parent = stop_node.RightChild
                        stop_node.RightChild.LeftChild  = stop_node.LeftChild
                        BSTFind.Node = None
                        return
                    if stop_node.Parent.RightChild == stop_node:
                        stop_node.Parent.RightChild = stop_node.RightChild
                        stop_node.LeftChild.Parent = stop_node.RightChild
                        stop_node.RightChild.LeftChild = stop_node.LeftChild
                        BSTFind.Node = None
                        return
                else: del_node = del_node.LeftChild
                count += 1
            while True:
                if del_node.LeftChild == None and del_node.RightChild == None:
                    del_node.Parent = stop_node.Parent
                    if stop_node.Parent.LeftChild == stop_node:
                        stop_node.Parent.LeftChild = stop_node.RightChild
                        stop_node.LeftChild.Parent = stop_node.RightChild
                        stop_node.RightChild.LeftChild  = stop_node.LeftChild
                        BSTFind.Node = None
                if del_node.LeftChild == None and del_node.RightChild != None:
                    del_node.RightChild.Parent = del_node.Parent
                    if del_node.Parent.LeftChild == del_node:
                        del_node.Parent.LeftChild = del_node.RightChild
                        BSTFind.Node = None
                        return
            pass

    def Count(self):
        return 0

tree = BST(BSTNode(8, 18, None))
tree.AddKeyValue(4, 4)  # формируем дерево
tree.AddKeyValue(12, 12)
tree.AddKeyValue(2, 2)
tree.AddKeyValue(6, 6)
tree.AddKeyValue(10, 10)
tree.AddKeyValue(14, 14)
tree.AddKeyValue(1, 1)
tree.AddKeyValue(3, 3)
tree.AddKeyValue(5, 5)
tree.AddKeyValue(7, 7)
tree.AddKeyValue(9, 9)
tree.AddKeyValue(11, 11)
tree.AddKeyValue(13, 13)
tree.AddKeyValue(15, 15)
tree.AddKeyValue(15, 15)
tree.AddKeyValue(15, 15)
tree.DeleteNodeByKey(12)

