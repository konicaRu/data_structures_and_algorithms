class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов
        self.level = 1
class SimpleTree:
    def __init__(self, root):
        self.Root = root;  # корень, может быть None
    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)  # ParentNode.Children = NewChild
        NewChild.Parent = ParentNode
        # ваш код добавления нового дочернего узла существующему ParentNode
    def GetAllNodes(self):  # пробегаем по значению узлов NodeValue
        vizit = []  # надо предусмотреть если корень нана или только один корень
        stack = []
        node = self.Root
        if node == None:
            return vizit
        vizit.append(node)
        while True:
            for i in range(len(node.Children)):
                node_level = node.Children[i]
                node_level.level = node.level + 1
                stack.insert(0, node.Children[i])
            if len(stack) == 0:
                break
            node = stack[0]
            vizit.insert(0, stack[0])
            stack.pop(0)
        return vizit

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
print(graf.GetAllNodes())

# node1 = SimpleTreeNode(1, None)
# node2 = SimpleTreeNode(2, None)
# node3 = SimpleTreeNode(3, None)
# node4 = SimpleTreeNode(4, None)
# node5 = SimpleTreeNode(5, None)
# node6 = SimpleTreeNode(6, None)
# graf = SimpleTree(node1)
# graf.AddChild(node1, node2)
# graf.AddChild(node1, node3)
# graf.AddChild(node2, node4)
# graf.AddChild(node2, node5)
# graf.AddChild(node5, node6)
# print(graf.GetAllNodes())