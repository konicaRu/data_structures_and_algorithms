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

#построение и обход деревьев питон? Нерекурсивная реализация обхода дерева питон
#https://www.youtube.com/watch?v=V8bu4tn4i-4&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=21
#https://acm.bsu.by/wiki/%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%B0%D1%8F_%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F_%D0%B1%D0%B8%D0%BD%D0%B0%D1%80%D0%BD%D1%8B%D1%85_%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%BE%D0%B2%D1%8B%D1%85_%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D1%8C%D0%B5%D0%B2#.D0.9A.D0.BB.D0.B0.D1.81.D1.81_.D0.B2.D0.B5.D1.80
# .D1.88.D0.B8.D0.BD.D1.8B_.D0.B4.D0.B5.D1.80.D0.B5.D0.B2.D0.B0_3