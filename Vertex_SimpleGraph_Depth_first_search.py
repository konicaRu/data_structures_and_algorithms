class Vertex:

    def __init__(self, val):
        self.Value = val
        self.hit = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        for i in range(len(self.vertex)):
            if self.vertex[i] == None:
                self.vertex[i] = Vertex(v)
                return
            if self.vertex[i] != None:
                continue
        return

    def RemoveVertex(self, v):
        self.vertex[v] = None  # ваш код удаления вершины со всеми её рёбрами
        for i in range(len(self.m_adjacency[v])):
            if self.m_adjacency[v][i] != 0:
                self.m_adjacency[v][i] = 0
        for j in range(len(self.m_adjacency)):
            if self.m_adjacency[j][v] == 1:
                self.m_adjacency[j][v] = 0
        return

    def IsEdge(self, v1, v2):
        if self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1:
            return True
        else:  # True если есть ребро между вершинами v1 и v2
            return False

    def AddEdge(self, v1, v2):  # предусмотреть выход за диапазон списка
        self.m_adjacency[v1][v2] = 1  # добавление ребра между вершинами v1 и v2
        self.m_adjacency[v2][v1] = 1
        return

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0  # удаление ребра между вершинами v1 и v2
        self.m_adjacency[v2][v1] = 0
        return

    def DepthFirstSearch(self, VFrom, VTo):
        res = []
        node = self.m_adjacency[VFrom]
        res.append(self.vertex[VFrom])
        self.vertex[VFrom].hit = True
        count = -1
        while True:
            for i in node:
                count += 1
                if count > len(node) - 1:
                    res.pop()
                    if res == []:
                        return []
                    node = self.m_adjacency[len(res) - 1]
                    count = -1
                    break
                if i == 1 and count == VTo:
                    res.append(self.vertex[VTo])
                    return res
                if i == 1 and count != VTo and self.vertex[count].hit == False:
                    res.append(self.vertex[count])
                    self.vertex[count].hit = True
                    node = self.m_adjacency[count]
                    count = -1
                    break


graff = SimpleGraph(4)
print(graff.AddVertex(1))
print(graff.AddVertex(2))
print(graff.AddVertex(3))
print(graff.AddVertex(4))
print(graff.AddEdge(0, 1))
print(graff.AddEdge(1, 2))
print(graff.AddEdge(1, 3))
print(graff.DepthFirstSearch(0, 5))

#Vertex_BreadthFirstSearch
