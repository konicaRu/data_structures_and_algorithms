import unittest
import PowerSet_without_hush


class MyTestCase(unittest.TestCase):
    def test_put_add(self):
        arr = PowerSet_without_hush.PowerSet()
        arr.put("rrrrr")
        arr.put('vasya')
        arr.put('forest')
        arr.put('foretst')
        arr.put('forwetst')
        res = arr.size()
        self.assertEqual(res, 5)

    def test_put_not_add(self):
        arr = PowerSet_without_hush.PowerSet()
        arr.put("rrrrr")
        arr.put('vasya')
        arr.put('forest')
        arr.put('foretst')
        arr.put('forest')
        res = arr.size()
        self.assertEqual(res, 4)

    def test_put_remove(self):
        arr = PowerSet_without_hush.PowerSet()
        arr.put("rrrrr")
        arr.put('vasya')
        arr.put('foreset')
        arr.put('foretst')
        arr.put('forest')
        arr.remove('forest')
        res = arr.size()
        self.assertEqual(res, 4)

    def test_intersection(self):
        arr = PowerSet_without_hush.PowerSet()
        arr.put('1')
        arr.put('2')
        arr.put('3')
        arr.put('4')
        arr.put('5')
        self.assertEqual(len(arr.intersection({'1', '2', '3'})), 3)

    def test_intersection_empty(self):
        arr = PowerSet_without_hush.PowerSet()
        arr.put('1')
        arr.put('2')
        arr.put('3')
        arr.put('4')
        arr.put('5')
        self.assertEqual(arr.intersection({'7', '9', '8'}), None)

    def test_union(self):
        arr = PowerSet_without_hush.PowerSet()
        arr.put('1')
        arr.put('2')
        arr.put('3')
        arr.put('4')
        arr.put('5')
        self.assertEqual(len(arr.union({'7', '9', '8'})), 8)

    def test_union_empty(self):
        arr = PowerSet_without_hush.PowerSet()
        arr.put('1')
        arr.put('2')
        arr.put('3')
        arr.put('4')
        arr.put('5')
        self.assertEqual(arr.union({}), None)

    def test_difference(self):
        arr = PowerSet_without_hush.PowerSet()
        arr.put('1')
        arr.put('2')
        arr.put('3')
        arr.put('4')
        arr.put('5')
        self.assertEqual(len(arr.difference({'1','3', '7', '9', '8'})), 3)

    def test_difference_empty(self):
        arr = PowerSet_without_hush.PowerSet()
        arr.put('1')
        arr.put('2')
        arr.put('3')
        self.assertEqual(arr.difference({'1','2','3','12','34','56'}), None)
if __name__ == '__main__':
    unittest.main()
