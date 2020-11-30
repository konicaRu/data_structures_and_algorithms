import random
class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root;  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)  # ParentNode.Children = NewChild
        NewChild.Parent = ParentNode
        # ваш код добавления нового дочернего узла существующему ParentNode

    def DeleteNode(self, NodeToDelete):
        node_up = NodeToDelete.Parent
        if node_up == None:
            self.Root = None
            return
        node_up.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None
        # ваш код удаления существующего узла NodeToDelete

    def GetAllNodes(self):  # пробегаем по значению узлов NodeValue
        vizit = []  # надо предусмотреть если корень нана или только один корень
        stack = []
        node = self.Root
        if node == None:
            return vizit
        vizit.append(node)
        while True:
            for i in range(len(node.Children)):
                stack.insert(0, node.Children[i])
            if len(stack) == 0:
                break
            node = stack[0]
            vizit.insert(0, stack[0])
            stack.pop(0)
        return vizit

    def FindNodesByValue(self, val):  # надо предусмотреть если корень нана или только один корень
        vizit = []
        stack = []
        result = []
        node = self.Root
        if node == None:  # если первая нода нан
            return vizit
        if node.NodeValue == val:  # если нода одна корневая
            result.append(node)
        while True:
            for i in range(len(node.Children)):
                stack.insert(0, node.Children[i])
            if len(stack) == 0:
                break
            node = stack[0]
            if node.NodeValue == val:
                result.append(node)
            vizit.insert(0, stack[0])
            stack.pop(0)
        return result

    def MoveNode(self, OriginalNode, NewParent):# ваш код перемещения узла вместе с его поддеревом // # в качестве дочернего для узла NewParent
        if self.Root == None:  # если первая нода нан
            return
        if OriginalNode == None:
            return
        if NewParent == None:
            return
        if OriginalNode.Parent == NewParent:# если переставляемые ноды уже так и стоят graf.AddChild(node2, node4) - graf.MoveNode(node4, node2)
            return
        else:
            node_up = OriginalNode.Parent
            for i in range(len(node_up.Children)):
                if node_up.Children[i] == OriginalNode:
                    node_up.Children.remove(node_up.Children[i])
            self.AddChild(NewParent, OriginalNode)

    def Count(self):
        if self.Root == None:  # если первая нода нан
            return 0
        count = len(self.GetAllNodes())  # количество всех узлов в дереве
        return count

    def LeafCount(self):
        if self.Root == None:  # если первая нода нан
            return 0
        count = 0
        for i in self.GetAllNodes():
            if len(i.Children) == 0 or i.Children == None:
                count += 1  # количество листьев в дереве
        return count

node1 = SimpleTreeNode(1, None)
node2 = SimpleTreeNode(2, None)
node3 = SimpleTreeNode(3, None)
node4 = SimpleTreeNode(4, None)
node5 = SimpleTreeNode(5, None)
node6 = SimpleTreeNode(6, None)
node7 = SimpleTreeNode(7, None)
node8 = SimpleTreeNode(8, None)
node9 = SimpleTreeNode(9, None)
graf = SimpleTree(node1)
graf.AddChild(node1, node2)
graf.AddChild(node1, node3)
graf.AddChild(node2, node4)
graf.AddChild(node2, node5)
graf.AddChild(node5, node6)
graf.AddChild(node5, node7)
graf.AddChild(node3, node8)
graf.AddChild(node8, node9)
print(graf.MoveNode(node4, node2))
# # print(graf.MoveNode(node4, node2))
# # graf.DeleteNode(node4)
# print('knout', graf.Count())
# print('list', graf.LeafCount())
# print(len(graf.GetAllNodes()))
# # print(graf.FindNodesByValue(1))
#print(graf.MoveNode(node4, node2))
# # print(graf.Count())
# # print(graf.LeafCount())
# # node1 = SimpleTreeNode(1, None)
# # node2 = SimpleTreeNode(2, node1)
# # node3 = SimpleTreeNode(3, node2)
# # node4 = SimpleTreeNode(4, node2)
# # node5 = SimpleTreeNode(5, node4)
# # node6 = SimpleTreeNode(6, node3)
# # graf = SimpleTree(node1)
# # graf.AddChild(node1, node2)
# # graf.AddChild(node2, node3)
# # graf.AddChild(node2, node4)
# # graf.AddChild(node4, node5)
# # graf.AddChild(node3, node6)
# # print(graf.MoveNode(node5, node2))
# # print(graf.LeafCount())
# # print(graf.Count())
# # print(graf.DeleteNode(node2))
# # print(graf.LeafCount())
# # print(graf.Count())