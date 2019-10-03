class Node:
    def __init__(self, v, p=None, n=None):
        self.value = v
        self.prev = p
        self.next = n

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            else:
                node = node.next

    def find_all(self, val):
        node = self.tail
        arr = []
        while node is not None:
            if node.value == val:
                arr.append(val)
            node = node.prev
        return arr

    def delete(self, val, all=False):
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

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.tail
        count = 0
        while node is not None:
            count += 1
            node = node.prev
        return count

    def insert(self, afterNode, newNode):
        node = self.head
        if self.head == None:
            self.tail = self.head = newNode  # self.tail = self.head = Node(newNode)
            return
        if afterNode == None and self.head != None:#Если afterNode = None и список непустой, добавьте новый эл посл
            self.tail.next = newNode
            newNode.prev = self.tail # self.tail = self.head = Node(newNode)
            self.tail = self.tail.next
            return
        while node is not None:
            if node.value == self.tail.value:# вставляем ноду вконце
                node.next = Node(newNode.value, node, node.next)
                self.tail = self.tail.next
                return
            if node == afterNode:
                node.next = Node(newNode.value, node, node.next)
                node = node.next.next
                node.prev = node.prev.next
            else: node = node.next

    def add_in_head(self, newNode):  # проверяем когда список пустой, когда в списке 1 элемент
        if self.head is None:
            self.head = newNode  # self.head = self.tail = Node(newNode, None, None)
            newNode.next = None
            newNode.prev = None
            return
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
