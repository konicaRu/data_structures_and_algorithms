import unittest
import OrderedList


class MyTestCase(unittest.TestCase):
    def test_add(self):
        my_list = OrderedList.OrderedList(True)
        my_list.add(4)
        my_list.add(3)
        self.assertEqual(my_list.len(), 2)
        my_list.add(9)
        my_list.add(5)
        self.assertEqual(my_list.len(), 4)


if __name__ == '__main__':
    unittest.main()
