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
        node = self.head
        node_end = self.tail
        if self.head == None:
            return None
        if self.__ascending == True:
            if val < node.value or val > node_end.value:
                return None
        if self.__ascending == False:
            if val > node.value or val < node_end.value:
                return None
        while node is not None:
            if node.value == val:
                return node
            else:
                node = node.next

    def delete(self, val):
        one_run = self.head
        if self.head == None:  # после нахождения 1 го запускать цикл по новой
            return
        if one_run.value == val and self.head.next == None:  # если удаляем один элемент
            self.head = self.tail = None
            return
        if one_run.value == val:  # если удаляем первый элемент
            self.head = self.head.next
            one_run.next.prev = None
            one_run.next = None
            one_run = self.head
            if all == False:
                return
        while one_run is not None:
            if one_run.value == val and one_run.next != None:
                one_run = one_run.prev
                one_run.next = one_run.next.next
                one_run = one_run.next
                one_run.prev = one_run.prev.prev
                one_run = one_run.prev
                if all == False:
                    return
            if one_run.value == val and one_run.next == None:  # если в составе удаленного есть последний элемент
                one_run = one_run.prev
                one_run.next = None  # one_run.next.next
                self.tail = one_run
                if all == False:
                    return
            else:
                one_run = one_run.next

    def clean(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

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


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        print(len(v1), len(v2))
        v1 = v1.strip()  # убираем пробел
        v2 = v2.strip()
        print(len(v1), len(v2))
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0
        if v1 > v2:
            return 1


