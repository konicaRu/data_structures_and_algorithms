import unittest
import LinkedList_test


class MyTestCase(unittest.TestCase):
    def test_clear(self):  # проверяем удаление списка
        my_list = LinkedList_test.LinkedList()
        my_list.add_in_tail(LinkedList_test.Node(54))
        my_list.add_in_tail(LinkedList_test.Node(69))
        my_list.add_in_tail(LinkedList_test.Node(78))
        my_list.add_in_tail(LinkedList_test.Node(83))

        self.assertEqual(my_list.clear(), None)

    def test_len(self):  # проверяем длинну списка
        my_list = LinkedList_test.LinkedList()
        my_list.add_in_tail(LinkedList_test.Node(54))
        my_list.add_in_tail(LinkedList_test.Node(68))
        my_list.add_in_tail(LinkedList_test.Node(78))
        my_list.add_in_tail(LinkedList_test.Node(83))
        res = my_list.len()

        self.assertEqual(res, 4)

    def test_delete_one(self):  # сравниваем длины после удаления одного элемента
        my_list_2 = LinkedList_test.LinkedList()
        my_list_2.add_in_tail(LinkedList_test.Node(1))
        my_list_2.add_in_tail(LinkedList_test.Node(2))
        my_list_2.add_in_tail(LinkedList_test.Node(3))
        my_list_2.add_in_tail(LinkedList_test.Node(3))
        my_list_2.delete(3)
        res = my_list_2.len()
        self.assertEqual(res, 3)

    def test_delete_more(self):  # сравниваем длины после удаления двух элементов
        my_list_2 = LinkedList_test.LinkedList()
        my_list_2.add_in_tail(LinkedList_test.Node(1))
        my_list_2.add_in_tail(LinkedList_test.Node(2))
        my_list_2.add_in_tail(LinkedList_test.Node(3))
        my_list_2.add_in_tail(LinkedList_test.Node(3))
        my_list_2.delete(3, True)
        res = my_list_2.len()
        self.assertEqual(res, 2)

    def test_delete_item(self):  # сравниваем длины после удвления из списка с 1 элементом
        my_list_2 = LinkedList_test.LinkedList()
        my_list_2.add_in_tail(LinkedList_test.Node(1))
        my_list_2.delete(1)
        res = my_list_2.len()
        self.assertEqual(res, 0)
    def test_delete_more1(self):  # сравниваем после удаления двух элементов
        my_list_2 = LinkedList_test.LinkedList()
        my_list_1 = LinkedList_test.LinkedList()
        my_list_1.add_in_tail(LinkedList_test.Node(1))
        my_list_1.add_in_tail(LinkedList_test.Node(2))
        my_list_2.add_in_tail(LinkedList_test.Node(1))
        my_list_2.add_in_tail(LinkedList_test.Node(2))
        my_list_2.add_in_tail(LinkedList_test.Node(3))
        my_list_2.add_in_tail(LinkedList_test.Node(3))
        my_list_2.delete(3, True)
        a = my_list_1
        b = my_list_2
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()
