import unittest


class Node:
    def __init__(self, v, d=None):
        self.value = v
        self.next = d


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head == None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def clear(self):
        self.__init__()

    def len(self):
        node = self.head
        count = 0
        while node != None:
            count += 1
            node = node.next
        return count

    def delete(self, val, all=True):  # если нужно найти на удаление более 2 х элементов мб
        if self.head == None:  # после нахождения 1 го запускать цикл по новой
            return
        one_run = self.head
        two_run = self.head
        if one_run.value == val:  # если удаляем первый элемент
            self.head = self.head.next
        while one_run != None:
            if one_run.value == val:
                two_run.next = one_run.next
                if all == False:
                    return
                else:
                    one_run = self.head
                    two_run = self.head
            else:
                two_run = one_run
                one_run = one_run.next


class LinkedList_1:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head == None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def arr_full(self):  # создаем обычный список из связанного списка
        arr_f = []
        node = self.head
        while node != None:
            arr_f.append(node.value)
            node = node.next
        return arr_f


class LinkedList_2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head == None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def delete(self, val, all=True):  # если нужно найти на удаление более 2 х элементов мб
        if self.head == None:  # после нахождения 1 го запускать цикл по новой
            return
        one_run = self.head
        two_run = self.head
        if one_run.value == val:  # если удаляем первый элемент
            self.head = self.head.next
        while one_run != None:
            if one_run.value == val:
                two_run.next = one_run.next
                if all == False:
                    return
                else:
                    one_run = self.head
                    two_run = self.head
            else:
                two_run = one_run
                one_run = one_run.next

    def arr_full(self):  # создаем обычный список из связанного списка УБРАТЬ
        arr_f = []
        node = self.head
        while node != None:
            arr_f.append(node.value)
            node = node.next
        return arr_f

    def arr_select(self, var):  # делаем список из конкретных узлов начиная с первого УБРАТЬ
        arr_sel = []
        court = 0
        node = self.head
        while node != None and court < var:
            court += 1
            arr_sel.append(node)
            node = node.next

        return arr_sel

    def arr_knot(self):  # создаем узлов список из связанного списка УБРАТЬ
        arr_f = []
        node = self.head
        while node != None:
            arr_f.append(node)
            node = node.next
        return arr_f

my_list = LinkedList()
my_list_1 = LinkedList_1()
my_list_2 = LinkedList_2()


class MyTestCase(unittest.TestCase):
    def test_clear(self):# проверяем удаление списка
        my_list.add_in_tail(Node(54))
        my_list.add_in_tail(Node(69))
        my_list.add_in_tail(Node(78))
        my_list.add_in_tail(Node(83))

        self.assertEqual(my_list.clear(), None)

    def test_len(self):# проверяем длинну списка
        my_list.add_in_tail(Node(54))
        my_list.add_in_tail(Node(69))
        my_list.add_in_tail(Node(78))
        my_list.add_in_tail(Node(83))
        res = my_list.len()

        self.assertEqual(res, 4)

    def test_delete_last(self):# сравниваем после удаления размеры списков через обычные списки
        my_list_1.add_in_tail(Node(1))
        my_list_1.add_in_tail(Node(2))
        my_list_2.add_in_tail(Node(1))
        my_list_2.add_in_tail(Node(2))
        my_list_2.add_in_tail(Node(3))
        my_list_2.add_in_tail(Node(3))
        my_list_2.delete(3)
        self.assertEqual(my_list_1.arr_full(), my_list_2.arr_full())

    def test_delete_select(self):# сравниваем после удаления размеры списков через списки узлов
        my_list_2.add_in_tail(Node(1))
        my_list_2.add_in_tail(Node(2))
        my_list_2.add_in_tail(Node(3))
        my_list_2.add_in_tail(Node(3))
        a = my_list_2.arr_select(2)
        my_list_2.delete(3)
        b = my_list_2.arr_knot()
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()
