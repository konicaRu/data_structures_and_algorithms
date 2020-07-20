import unittest 
import BinarySearchTrees


class MyTestCase(unittest.TestCase):
    def test_FindNodeByKey(self):  # проверяем вставку ноды и поиск ноды
        tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 18, None))  # добавляем корневую ноду
        tree.FindNodeByKey(8)  # ищем значение 8
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)  # определяем что нода найдена по параметру BSTFind.NodeHasKey = True
        tree.AddKeyValue(4, 4)  # добавляем узел 4 к узлу 8, это левый узел
        self.assertEqual(BinarySearchTrees.BSTFind.ToLeft, True)  # проверяем что он левый по параметру BSTFind.ToLeft = True
        tree.AddKeyValue(4, 15)
        self.assertEqual(tree.AddKeyValue(4, 4), False)
        # проверить попытку добавления ключа который уже есть в дереве проверим фукцией количества узлов в дереве
        tree.Count()
        self.assertEqual(tree.Count(), 2)

        tree.FindNodeByKey(6)  # ищем ноду 6 которой нет
        self.assertEqual(BinarySearchTrees.BSTFind.Node.NodeKey == 4, True)  # определили что указатель стоит на 4
        self.assertEqual(BinarySearchTrees.BSTFind.Node.Parent.NodeKey == 8, True)  # проверили что нода 4 имеет родителем ноду 8
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)  # определяем что нода не найдена по параметру BSTFind.NodeHasKey = Folse
        tree.AddKeyValue(12, 12)  # добавлем ноду 6 к ноде 4 это правый узел
        self.assertEqual(BinarySearchTrees.BSTFind.ToLeft, False)  # проверяем что он правый по параметру BSTFind.ToLeft = Folse
        tree.FindNodeByKey(12)  # ищем ноду 6
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)  # определяем что нода найдена по параметру BSTFind.NodeHasKey = True
        self.assertEqual(BinarySearchTrees.BSTFind.Node.Parent.RightChild == BinarySearchTrees.BSTFind.Node, True)
        # проверили что предпоследняя 6 нода имеет правым узлом ноду 4
        tree.FindNodeByKey(20)  # проверить что ключа нет
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)  # проверить что ключа нет

    def test_FinMinMax(self):# тестим вариант когда полное дерево максимальный и минимальный элемент
        tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 8, None))  # добавляем корневую ноду
        tree.AddKeyValue(4, 4) # формируем дерево
        tree.AddKeyValue(12, 12)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(10, 10)
        tree.AddKeyValue(14, 14)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(11, 11)
        tree.AddKeyValue(13, 13)
        tree.AddKeyValue(15, 15)
        #проверяем от стартовой ноды
        tree.FindNodeByKey(8)
        start = tree.FinMinMax(BinarySearchTrees.BSTFind.Node, False)
        tree.FindNodeByKey(1)
        self.assertEqual( start == BinarySearchTrees.BSTFind.Node, True) # находим наименьщую
        tree.FindNodeByKey(8)
        start = tree.FinMinMax(BinarySearchTrees.BSTFind.Node, True)
        tree.FindNodeByKey(15)
        self.assertEqual(start == BinarySearchTrees.BSTFind.Node, True) # находлим наибольшую
        # проверяем от промежуточной ноды
        tree.FindNodeByKey(12)
        start = tree.FinMinMax(BinarySearchTrees.BSTFind.Node, False)
        tree.FindNodeByKey(9)# находим наименьщую
        self.assertEqual(start == BinarySearchTrees.BSTFind.Node, True)# BinarySearchTrees.BSTFind.Node ссылка на ноду при работе функции tree.FindNodeByKey(9)
        tree.FindNodeByKey(12)
        start = tree.FinMinMax(BinarySearchTrees.BSTFind.Node, True)
        tree.FindNodeByKey(15)
        self.assertEqual(start == BinarySearchTrees.BSTFind.Node, True)# находлим наибольшую
        tree.FindNodeByKey(5)
        self.assertEqual(tree.FinMinMax(BinarySearchTrees.BSTFind.Node, True), None)

    def test_FinMinMax2(self): #поиск максимального и минимального ключей, начиная с заданного узла тестим вариант когда 2 ноды
        tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 8, None))  # добавляем корневую ноду
        tree.AddKeyValue(4, 4) # формируем дерево
        tree.FindNodeByKey(8)
        start = tree.FinMinMax(BinarySearchTrees.BSTFind.Node, False)
        tree.FindNodeByKey(4)
        self.assertEqual( start == BinarySearchTrees.BSTFind.Node, True) # находим наименьщую
        tree.FindNodeByKey(8)
        start = tree.FinMinMax(BinarySearchTrees.BSTFind.Node, True)
        tree.FindNodeByKey(15)
        self.assertEqual(start == None, True) # находлим наибольшую, 15 нет , значит None

    def test_FinMinMax2_2(self):  # в пустом дереве поиск максимального и минимального ключей, в пустом дереве
        tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 8, None))  # добавляем корневую ноду
        tree.AddKeyValue(4, 4)
        tree.DeleteNodeByKey(4)
        tree.DeleteNodeByKey(8)
        self.assertEqual(tree.FinMinMax(BinarySearchTrees.BSTFind.Node, False), None)

    def test_FinMinMax3(self):# тестим вариант когда 1 нода поиск максимального и минимального ключей, начиная с заданного узла,
        tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 8, None))  # добавляем корневую ноду
        tree.FindNodeByKey(8)
        #self.assertEqual(BinarySearchTrees.BSTFind.Node == tree.FinMinMax(tree.FindNodeByKey(8), True), True)
        self.assertEqual(tree.FinMinMax(BinarySearchTrees.BSTFind.Node, False), None)
        self.assertEqual(tree.FinMinMax(BinarySearchTrees.BSTFind.Node, True), None)


    def test_DeleteNodeByKeyList(self):#удаляем правый лист
        tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 8, None))  # добавляем корневую ноду
        tree.AddKeyValue(4, 4)  # формируем дерево
        tree.AddKeyValue(12, 12)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(10, 10)
        tree.AddKeyValue(14, 14)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(11, 11)
        tree.AddKeyValue(13, 13)
        tree.AddKeyValue(15, 15)
        tree.DeleteNodeByKey(1)
        tree.FindNodeByKey(1)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        tree.DeleteNodeByKey(3)
        tree.FindNodeByKey(3)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        tree.DeleteNodeByKey(11)
        tree.FindNodeByKey(11)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        tree.DeleteNodeByKey(9)
        tree.FindNodeByKey(9)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        self.assertEqual(tree.DeleteNodeByKey(22), False)

    def test_DeleteNodeByKeyListLeft(self):# удаляем ноду слева от родителя с левым листом
        tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 8, None))  # добавляем корневую ноду
        tree.AddKeyValue(4, 4)  # формируем дерево
        tree.AddKeyValue(12, 12)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(10, 10)
        tree.AddKeyValue(14, 14)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(11, 11)
        tree.AddKeyValue(13, 13)
        tree.AddKeyValue(15, 15)
        tree.DeleteNodeByKey(3)
        tree.FindNodeByKey(3)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        tree.FindNodeByKey(1)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)
        tree.DeleteNodeByKey(2)
        tree.FindNodeByKey(2)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)

    def test_DeleteNodeByKeyListLeft2(self):  # удаляем ноду слева от родителя с правым листом
        tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 8, None))  # добавляем корневую ноду
        tree.AddKeyValue(4, 4)  # формируем дерево
        tree.AddKeyValue(12, 12)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(10, 10)
        tree.AddKeyValue(14, 14)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(11, 11)
        tree.AddKeyValue(13, 13)
        tree.AddKeyValue(15, 15)
        tree.DeleteNodeByKey(9)
        tree.FindNodeByKey(9)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        tree.DeleteNodeByKey(10)
        tree.FindNodeByKey(10)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        tree.FindNodeByKey(11)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)

    def test_DeleteNodeByKeyListRight(self):  # удаляем ноду справа от родителя с левым листом
        tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 8, None))  # добавляем корневую ноду
        tree.AddKeyValue(4, 4)  # формируем дерево
        tree.AddKeyValue(12, 12)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(10, 10)
        tree.AddKeyValue(14, 14)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(11, 11)
        tree.AddKeyValue(13, 13)
        tree.AddKeyValue(15, 15)
        tree.DeleteNodeByKey(15)
        tree.FindNodeByKey(15)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        tree.DeleteNodeByKey(14)
        tree.FindNodeByKey(14)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        tree.FindNodeByKey(13)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)

    def test_DeleteNodeByKeyListRight2(self):  # удаляем ноду справа от родителя с правым листом
        tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 8, None))  # добавляем корневую ноду
        tree.AddKeyValue(4, 4)  # формируем дерево
        tree.AddKeyValue(12, 12)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(10, 10)
        tree.AddKeyValue(14, 14)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(11, 11)
        tree.AddKeyValue(13, 13)
        tree.AddKeyValue(15, 15)
        tree.DeleteNodeByKey(5)
        tree.FindNodeByKey(5)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        tree.FindNodeByKey(7)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)
        tree.DeleteNodeByKey(6)
        tree.FindNodeByKey(6)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        tree.FindNodeByKey(7)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)

    def test_DeleteNode2knotLeft(self): # удаляем узел с двумя дочерними листами слева от родителя
        tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 8, None))  # добавляем корневую ноду
        tree.AddKeyValue(4, 4)  # формируем дерево
        tree.AddKeyValue(12, 12)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(10, 10)
        tree.AddKeyValue(14, 14)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(11, 11)
        tree.AddKeyValue(13, 13)
        tree.AddKeyValue(15, 15)
        tree.AddKeyValue(15, 15)
        tree.DeleteNodeByKey(10)
        tree.FindNodeByKey(10)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        tree.FindNodeByKey(11)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)
        tree.FindNodeByKey(9)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)

    def test_DeleteNode2knotRight(self): # удаляем узел с двумя дочерними листами справа от родителя
        tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 8, None))  # добавляем корневую ноду
        tree.AddKeyValue(4, 4)  # формируем дерево
        tree.AddKeyValue(12, 12)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(10, 10)
        tree.AddKeyValue(14, 14)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(11, 11)
        tree.AddKeyValue(13, 13)
        tree.AddKeyValue(15, 15)
        tree.AddKeyValue(15, 15)
        tree.DeleteNodeByKey(14)
        tree.FindNodeByKey(14)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        tree.FindNodeByKey(15)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)
        tree.FindNodeByKey(13)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)

    def test_DeleteNode2knot(self):  # удаляем узел с двумя дочерними узлами справа от родителя
        tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 8, None))  # добавляем корневую ноду
        tree.AddKeyValue(4, 4)  # формируем дерево
        tree.AddKeyValue(12, 12)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(10, 10)
        tree.AddKeyValue(14, 14)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(11, 11)
        tree.AddKeyValue(13, 13)
        tree.AddKeyValue(15, 15)
        tree.AddKeyValue(15, 15)
        tree.DeleteNodeByKey(14)
        tree.FindNodeByKey(14)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        tree.FindNodeByKey(15)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)

    def test_DeleteNode2knot2R(self): # удаляем правый узел с двумя дочерними узлами идем вниз налево до листа
        tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 8, None))  # добавляем корневую ноду
        tree.AddKeyValue(4, 4)  # формируем дерево
        tree.AddKeyValue(12, 12)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(10, 10)
        tree.AddKeyValue(14, 14)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(11, 11)
        tree.AddKeyValue(13, 13)
        tree.AddKeyValue(15, 15)
        tree.AddKeyValue(15, 15)
        tree.DeleteNodeByKey(12)
        tree.FindNodeByKey(12)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        tree.FindNodeByKey(13)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)
        tree.FindNodeByKey(15)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)
        tree.FindNodeByKey(10)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)

    def test_DeleteNode2knot2L(self): # удаляем левый узел с двумя дочерними узлами идем вниз налево до листа
        tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 8, None))  # добавляем корневую ноду
        tree.AddKeyValue(4, 4)  # формируем дерево
        tree.AddKeyValue(12, 12)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(10, 10)
        tree.AddKeyValue(14, 14)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(11, 11)
        tree.AddKeyValue(13, 13)
        tree.AddKeyValue(15, 15)
        tree.AddKeyValue(15, 15)
        tree.DeleteNodeByKey(4)
        tree.FindNodeByKey(4)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        tree.FindNodeByKey(7)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)
        tree.FindNodeByKey(5)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)
        tree.FindNodeByKey(2)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)

    def test_DeleteNode2knot2DelLeft(self): # удаляем левый лист потом удаляем узел с оставшимся правым листом
        tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 8, None))  # добавляем корневую ноду
        tree.AddKeyValue(4, 4)  # формируем дерево
        tree.AddKeyValue(12, 12)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(10, 10)
        tree.AddKeyValue(14, 14)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(11, 11)
        tree.AddKeyValue(13, 13)
        tree.AddKeyValue(15, 15)
        tree.AddKeyValue(15, 15)
        tree.DeleteNodeByKey(5)
        tree.FindNodeByKey(5)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        tree.DeleteNodeByKey(4)
        tree.FindNodeByKey(4)


    def test_DeleteNode2knot2DelRight(self): # удаляем правый лист потом удаляем узел с оставшимся правым листом
        tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 8, None))  # добавляем корневую ноду
        tree.AddKeyValue(4, 4)  # формируем дерево
        tree.AddKeyValue(12, 12)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(10, 10)
        tree.AddKeyValue(14, 14)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(11, 11)
        tree.AddKeyValue(13, 13)
        tree.AddKeyValue(15, 15)
        tree.AddKeyValue(15, 15)
        tree.DeleteNodeByKey(15)
        tree.FindNodeByKey(15)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        tree.DeleteNodeByKey(12)
        tree.FindNodeByKey(12)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        tree.FindNodeByKey(8)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)
        tree.FindNodeByKey(14)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)
        tree.FindNodeByKey(13)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)

    def test_DeleteNode2knot2Del2(self): # удаляем правый лист из 2 нод
        tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 8, None))  # добавляем корневую ноду
        tree.AddKeyValue(12, 12)
        tree.DeleteNodeByKey(12)
        tree.FindNodeByKey(12)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        tree.FindNodeByKey(8)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)

    def test_DeleteNode2knot2Del3(self): # удаляем правый лист из 2 нод
        tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 8, None))  # добавляем корневую ноду
        tree.AddKeyValue(4, 4)
        tree.DeleteNodeByKey(4)
        tree.FindNodeByKey(4)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        tree.FindNodeByKey(8)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, True)

    def test_DeleteNode2knot2Delcent(self): # удаляем 1 ноду
        tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 8, None))  # добавляем корневую ноду
        tree.DeleteNodeByKey(8)
        tree.FindNodeByKey(8)
        self.assertEqual(BinarySearchTrees.BSTFind.NodeHasKey, False)
        self.assertEqual(tree.Root == None, True)

    def test_Count(self):  # считаем узлы
            tree = BinarySearchTrees.BST(BinarySearchTrees.BSTNode(8, 8, None))  # добавляем корневую ноду
            tree.AddKeyValue(4, 4)  # формируем дерево
            tree.AddKeyValue(12, 12)
            tree.AddKeyValue(2, 2)
            tree.AddKeyValue(6, 6)
            tree.AddKeyValue(10, 10)
            tree.AddKeyValue(14, 14)
            tree.AddKeyValue(1, 1)
            tree.AddKeyValue(3, 3)
            tree.AddKeyValue(5, 5)
            tree.AddKeyValue(7, 7)
            tree.AddKeyValue(9, 9)
            tree.AddKeyValue(11, 11)
            tree.AddKeyValue(13, 13)
            tree.AddKeyValue(15, 15)
            tree.AddKeyValue(15, 15)
            tree.DeleteNodeByKey(15)
            tree.DeleteNodeByKey(12)
            tree.Count()
            self.assertEqual(tree.Count(), 13)
            # tree.DeleteNodeByKey(1)
            # tree.Count()
            # self.assertEqual(tree.Count(), 14)

if __name__ == '__main__':
    unittest.main()
