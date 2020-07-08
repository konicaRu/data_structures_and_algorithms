import unittest
import OrderedList


class MyTestCase(unittest.TestCase):

    def test_add(self):  # тест на добавление элемента
        my_list = OrderedList.OrderedList(True)  # определяем список
        my_list.add(4)  # загоняем элементы
        my_list.add(3)
        self.assertEqual(my_list.len(), 2)  # убеждаемся что их два assertEqual(a, b)	a == b
        my_list.add(9)
        my_list.add(5)
        self.assertEqual(my_list.len(), 4)  # убеждаемся что их два assertEqual(a, b)	a == b

    def test_compere_up(self):  # тест что элементы добавлены по возрастанию
        my_list = OrderedList.OrderedList(True)  #
        my_list.add(4)
        my_list.add(3)
        arr = my_list.get_all()  # создаем массив с помощью функции из введенных данных
        self.assertGreater(arr[1], arr[0])  # сравниваем первый и второй эл массива, определяем возрастание

    def test_compere_down(self):  # тест что элементы добавлены по убыванию
        my_list = OrderedList.OrderedList(False)  #
        my_list.add(4)
        my_list.add(3)
        arr = my_list.get_all()  # создаем массив с помощью функции из введенных данных
        self.assertGreater(arr[0], arr[1])  # сравниваем первый и второй эл массива, определяем возрастание

    def test_del_up(self):  # тест что элементы удалены, список по возратанию
        my_list = OrderedList.OrderedList(True)  #
        my_list.add(4)
        my_list.add(3)
        my_list.add(2)
        arr = my_list.get_all()
        my_list.delete(3)
        arr_1 = my_list.get_all()  # создаем массив с помощью функции из введенных данных
        self.assertNotEqual(arr[1], arr_1[1])  # позиции удаленного элемента эл массива, определяем возрастание
        self.assertGreater(arr[1], arr[0])  # сравниваем первый и второй эл массива, определяем возрастание

    def test_del_down(self):  # тест что элементы удалены, список по убыванию
        my_list = OrderedList.OrderedList(False)  #
        my_list.add(4)
        my_list.add(3)
        my_list.add(2)
        arr = my_list.get_all()
        my_list.delete(3)
        self.assertEqual(my_list.delete.one_run.next.prev, my_list.one_run)  # проверим связку next после удаления элемента
        arr_1 = my_list.get_all()  # создаем массив с помощью функции из введенных данных
        self.assertNotEqual(arr[1], arr_1[1])  # позиции удаленного элемента эл массива, определяем возрастание
        self.assertGreater(arr[0], arr[1])  # сравниваем первый и второй эл массива, определяем возрастание


    def test_head_tail(self):  # сравниваем головы и хвост
        my_list = OrderedList.OrderedList(False)  #
        my_list.add(4)
        my_list.add(3)
        my_list.add(2)
        my_list.delete(3)
        self.assertEqual(my_list.head.prev, None)
        self.assertEqual(my_list.tail.next, None)


if __name__ == '__main__':
    unittest.main()
import unittest
import calc

#
# class CalcTests(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(calc.add(1, 2), 3)
#
#     def test_sub(self):
#         self.assertEqual(calc.sub(4, 2), 2)
#
#     def test_mul(self):
#         self.assertEqual(calc.mul(2, 5), 10)
#
#     def test_div(self):
#         self.assertEqual(calc.div(8, 4), 2)
#
#
# if __name__ == '__main__':
#     unittest.main()
 
