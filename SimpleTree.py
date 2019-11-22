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
        # ваш код добавления нового дочернего узла существующему ParentNode

    def DeleteNode(self, NodeToDelete):
        node_up = NodeToDelete.Parent
        if node_up == None:
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

    def MoveNode(self, OriginalNode, NewParent):
        if OriginalNode or NewParent == None:
            return# ваш код перемещения узла вместе с его поддеревом // # в качестве дочернего для узла NewParent
        self.AddChild(NewParent, OriginalNode)
        node_up = OriginalNode.Parent
        for i in range(len(node_up.Children)):
            if node_up.Children[i] == OriginalNode:
                node_up_pop = i
        node_up.Children.pop(node_up_pop)
        OriginalNode.Parent = NewParent

    def Count(self):
        if self.node == None:  # если первая нода нан
            return 0
        count = len(self.GetAllNodes())  # количество всех узлов в дереве
        return count

    def LeafCount(self):
        if self.node == None:  # если первая нода нан
            return 0
        count = 0
        for i in self.GetAllNodes():
            if len(i.Children) == 0:
                count += 1  # количество листьев в дереве
        return count
