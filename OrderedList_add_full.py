class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0
        if v1 > v2:
            return 1
            # -1 если v1 < v2
            # 0 если v1 == v2
            # +1 если v1 > v2

    def add(self, value):
        node = self.head
        node_end = self.tail
        if self.head == None:  # вставляем элемент если список пустой
            self.tail = self.head = Node(value)
            return
        if self.head == self.tail:  # проверяем что элемент один
            if self.compare(node.value, value) == -1 or self.compare(node.value, value) == 0:
                if self.__ascending == True:
                    node.next = Node(value)  # вставляем элемент назад в списке 1 элемент и спис возраст
                    node.next.prev = node
                    self.tail = node.next
                    return
                if self.__ascending == False:  # вставляем элемент назад в списке 1 элемент и спис увывание
                    node.prev = Node(value)
                    node.prev.next = node
                    self.head = node.prev
                    return
            if self.compare(node.value, value) == 1:  # вставляем элемент вперед в списке 1 элемент и спис возраст
                if self.__ascending == True:
                    node.prev = Node(value)
                    node.prev.next = node
                    self.head = node.prev
                    return
                if self.__ascending == False:
                    node.next = Node(value)  # вставляем элемент назад в списке 1 элемент и спис убывание
                    node.next.prev = node
                    self.tail = node.next
                    return
        if self.head != self.tail:  # вставляем по концам self.head != self.tail больше 1 эл в списк
            if self.__ascending == True:
                if self.compare(node_end.value, value) == -1 or self.compare(node_end.value, value) == 0:
                    node_end.next = Node(value)  # вставляем элемент в хвост, в списке <1 элемент и спис возраст
                    node.next.prev = node
                    self.tail = node.next
                    self.tail = node_end.next
                    node_end.next.prev = node_end
                    return
                if self.compare(node.value, value) == 1 or self.compare(node.value, value) == 0:
                    node.prev = Node(value)  # вставляем элемент в голову в списке <1 элемент и спис возраст
                    node.prev.next = node
                    self.head = node.prev
                    return
            if self.__ascending == False:
                if self.compare(node_end.value, value) == 1 or self.compare(node_end.value, value) == 0:
                    node_end.next = Node(value)  # вставляем элемент в хвост, в списке <1 элемент и спис убывание
                    node.next.prev = node
                    self.tail = node.next
                    self.tail = node_end.next
                    node_end.next.prev = node_end
                    return
                if self.compare(node.value, value) == -1 or self.compare(node.value, value) == 0:
                    node.prev = Node(value)  # вставляем элемент в голову в списке <1 элемент и спис убывание
                    node.prev.next = node
                    self.head = node.prev
                    return
        while node is not None:  # вставляем элемент назад в списке <1 элемент  м/у 2 мя элементамии и спис возраст
            if (self.compare(node.value, value) == -1 and self.compare(node.next.value, value) == 1) or (
                    self.compare(node.value, value) == 1 and self.compare(node.next.value, value) == -1):
                node_next = node.next
                node.next = Node(value)
                node.next.prev = node
                node_next.prev = node.next
                node.next.next = node_next
                return
            else:
                node = node.next

    def find(self, val):
        return None  # здесь будет ваш код

    def delete(self, val):
        pass  # здесь будет ваш код

    def clean(self, asc):
        self.__ascending = asc
        pass  # здесь будет ваш код

    def len(self):
        node = self.head
        court = 0
        while node is not None:
            court += 1
            node = node.next
        return court  # здесь будет ваш код

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node.value)
            node = node.next
        return r


my_list = OrderedList(False)
my_list.add(6)
my_list.add(5)
my_list.add(8)
my_list.add(7)
my_list.add(5)
print(my_list.get_all())
