import unittest
import BalancedBST


class MyTestCase(unittest.TestCase):
    def test_one(self):
        tree = BalancedBST.BalancedBST()
        self.assertEqual(tree.GenerateTree([3]), True)
        self.assertEqual(tree.IsBalanced(tree.FindNodeByKey(3)), True)

    def test_two(self):
        tree = BalancedBST.BalancedBST()
        self.assertEqual(tree.GenerateTree([3, 2, 1, 3, 3, 3, 3, 3]), True)
        self.assertEqual(tree.IsBalanced(tree.FindNodeByKey(3)), True)

    def test_three(self):
        tree = BalancedBST.BalancedBST()
        self.assertEqual(tree.GenerateTree([3, 3, 1]), True)
        self.assertEqual(tree.IsBalanced(tree.FindNodeByKey(3)), True)



    def test_four(self):
        tree = BalancedBST.BalancedBST()
        self.assertEqual(tree.GenerateTree([3, 3, 1, 3]), True)
        self.assertEqual(tree.IsBalanced(tree.FindNodeByKey(3)), True)

    def test_five(self):
        tree = BalancedBST.BalancedBST()
        self.assertEqual(tree.GenerateTree([3, 3]), True)
        self.assertEqual(tree.IsBalanced(tree.FindNodeByKey(3)), True)

    def test_six(self):
        tree = BalancedBST.BalancedBST()
        self.assertEqual(tree.GenerateTree([3, 1]), True)
        self.assertEqual(tree.IsBalanced(tree.FindNodeByKey(3)), True)

    def test_seven(self):
        tree = BalancedBST.BalancedBST()
        self.assertEqual(tree.GenerateTree([4, 8, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15]), True)
        self.assertEqual(tree.IsBalanced(tree.FindNodeByKey(3)), True)

if __name__ == '__main__':
    unittest.main()
