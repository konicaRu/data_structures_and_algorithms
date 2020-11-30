class Vertex: 

    def __init__(self, val):
        self.Value = val
        self.hit = False
        self.level = 0


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

    def BreadthFirstSearch(self, VFrom, VTo):
        if self.m_adjacency[VFrom].count(0) == len(self.m_adjacency) or self.m_adjacency[VTo].count(0) == len(self.m_adjacency):  # если у начального и конечного элемента
            return []  # нет связей с остальными
        if VFrom == VTo:# проверяем если ввод и вывод ссылается на себя , равны
            if self.m_adjacency[VFrom].count(0) == len(self.m_adjacency):# если ребер никуда нет возврашаем отсутствие пути
                return []
            else:
                return [self.vertex[VFrom], self.vertex[VTo]]# если ребра есть поиск из узла в него же возвращает либо пустой список, либо список из двух элементов, если есть ребро само в себя, как для узла D.
        res = [] # итоговый список всех узлов графа поиска в ширину
        res.append(self.vertex[VFrom])  # добавляем в итоговый-промежуточный массив графф с которого начинаем поиск
        count_graf = -1 # счетчик показывает какое ребро естьв списке
        for i in res:  # бежим по этому списку
            if i.hit != True:  # пробегаем по нему если стоит отметка что еще не смотрели hit != True
                i.hit = True  # ставим флаг что просмотрено
                for j in self.m_adjacency[self.vertex.index(i)]:  # пробегаем по массиву где ребра этого графа
                    count_graf += 1 # показывает индекс еденицы
                    if j == 1 and self.vertex[count_graf].hit != True and self.vertex[count_graf] not in res:  # если есть ребро и соответственно смежный граф но в списке его еще нет
                        res.append(self.vertex[count_graf])  # добавляем его в итоговый промежуточный список
                        self.vertex[count_graf].level = i.level + 1  # ставим отметку какой уровень
                count_graf = -1  # при выходе из цикла сбрасываем счетчик
        res_way = [] # итоговый список узлов кратчайщего пути
        res_way.insert(0, self.vertex[VTo]) # добавляем в список последний узел с него начинаем поиск
        index_way = VTo # bндекс списка ребер конечного узла
        count_way = -1
        while True:
            for i in self.m_adjacency[index_way]: #бежим по списку ребер конечного узла
                count_way += 1
                if i == 1: # находим ребро
                    if self.vertex[count_way].level == 0: # если это конечное ребро оно у нас под индексом 0 то поиск закончен путь найден
                        res_way.insert(0, self.vertex[count_way]), # добавляем эл в начало спписка
                        if self.vertex[VFrom] not in res_way or self.vertex[VTo] not in res_way:  # если начальный и конечный элемент не входят в итоговый список значит пути нет
                            for k in self.vertex: # обнуляем показатели графоф левел и уровни до начального состояния чтобы при следующем запуске функции все работало
                                k.level = 0
                                k.hit = False
                            return []
                        else:
                            for k in self.vertex: # обнуляем показатели графоф левел и уровни до начального состояния смотри в тесте функцию test_my_peper_B2
                                k.level = 0
                                k.hit = False
                            return res_way
                    if self.vertex[count_way].level == self.vertex[index_way].level - 1 and self.vertex[count_way] not in res_way: # ищем по ребру граф с уровнем меньше на 1
                        res_way.insert(0, self.vertex[count_way]) #  добавляем его в список
                        index_way = count_way #  переходим на пробег по нему меняя массив self.m_adjacency[index_way]
                        count_way = -1 #  обнуляем счетчик ребер  для очередного цикла поиска пути self.m_adjacency[index_way]
                        break

graff = SimpleGraph(5)
graff.AddVertex(0)
graff.AddVertex(1)
graff.AddVertex(2)
graff.AddVertex(3)
graff.AddVertex(4)
graff.AddEdge(0, 1)
graff.AddEdge(0, 2)
graff.AddEdge(0, 3)
graff.AddEdge(1, 4)
graff.AddEdge(1, 3)
graff.AddEdge(2, 3)
graff.AddEdge(3, 4)
print(graff.BreadthFirstSearch(0, 4))
print(graff.BreadthFirstSearch(3, 0))

# graff = SimpleGraph(7)
# graff.AddVertex(0)
# graff.AddVertex(1)
# graff.AddVertex(2)
# graff.AddVertex(3)
# graff.AddVertex(4)
# graff.AddVertex(5)
# graff.AddVertex(6)
# graff.AddEdge(0, 1)
# graff.AddEdge(0, 2)
# graff.AddEdge(1, 2)
# #graff.AddEdge(2, 3)
# graff.AddEdge(3, 4)
# graff.AddEdge(4, 5)
# graff.AddEdge(5, 6)
# print(len(graff.BreadthFirstSearch(2, 6)))

# graff = SimpleGraph(6)
# graff.AddVertex(0)
# graff.AddVertex(1)
# graff.AddVertex(2)
# graff.AddVertex(3)
# graff.AddVertex(4)
# graff.AddVertex(5)
# graff.AddEdge(0, 1)
# graff.AddEdge(0, 2)
# graff.AddEdge(0, 3)
# graff.AddEdge(4, 2)
# graff.AddEdge(0, 3)
# graff.AddEdge(1, 2)
# graff.AddEdge(2, 3)
# graff.AddEdge(3, 4)
# print(graff.BreadthFirstSearch(1, 5))


# graff = SimpleGraph(6)
# graff.AddVertex(0)
# graff.AddVertex(1)
# graff.AddVertex(2)
# graff.AddVertex(3)
# graff.AddVertex(4)
# graff.AddEdge(0, 1)
# graff.AddEdge(0, 2)
# graff.AddEdge(2, 3)
# graff.AddEdge(3, 4)
# #graff.AddEdge(1, 4)
# print(graff.BreadthFirstSearch(0, 4))


# graff = SimpleGraph(10)
# graff.AddVertex(0)
# graff.AddVertex(1)
# graff.AddVertex(2)
# graff.AddVertex(3)
# graff.AddEdge(0, 1)
# graff.AddEdge(0, 2)
# graff.AddEdge(0, 3)
#
# print(graff.BreadthFirstSearch(0, 3))
