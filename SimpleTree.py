class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root;  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children = NewChild
        # ваш код добавления нового дочернего узла существующему ParentNode



    def DeleteNode(self, NodeToDelete):
        NodeToDelete.NodeValue = None
        NodeToDelete.Parent = None
        NodeToDelete.Children = None# ваш код удаления существующего узла NodeToDelete

    def GetAllNodes(self):
        # ваш код выдачи всех узлов дерева в определённом порядке
        return []

    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        return []

    def MoveNode(self, OriginalNode, NewParent):
        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        pass

    def Count(self):
        # количество всех узлов в дереве
        return 0

    def LeafCount(self):
        # количество листьев в дереве
        return 0

graf = SimpleTree(8)
node1 = SimpleTreeNode(graf, None)
node2 = SimpleTreeNode(2, node1)
node3 = SimpleTreeNode(3, node2)
node4 = SimpleTreeNode(4, node2)
graf.AddChild(node1, node2)
graf.AddChild(node2, node3)
graf.AddChild(node2, [node3, node4])
#graf.DeleteNode(node2)

