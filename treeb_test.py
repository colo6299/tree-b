from treeb import TreeB, NodeB
import unittest
from random import randint

class BTreeTest(unittest.TestCase):

    def test_init_and_properties(self):
        tree = TreeB(3)
        assert tree.b is 3

    def _insert_b(self, b, l=10):
        tree = TreeB(b)
        test_list = []
        for _ in range(l):
            n = randint(0, 1000)
            if n not in test_list:
                test_list.append(n)
        for item in test_list:
            tree.insert(item)
        return tree, test_list

    def test_node_binary_search_odd(self):
        node = NodeB(5, [None, 5, None, 7, None, 11, None, 12, None])
        assert node._find_array_index(5, 0, (len(node.array)-1)//2) == (1, True)
        assert node._find_array_index(6, 0, (len(node.array)-1)//2) == (2, False)
        assert node._find_array_index(4, 0, (len(node.array)-1)//2) == (0, False)

    def test_insert_multi_b_odds(self):
        for b in range(3, 20, 2):
            print('Testing insert with b=' + str(b) + '... ', end='')
            self._insert_b(b, b*4)
            print('OK')

    def test_search_multi_b_odds(self):
        for b in range(3, 20, 2):
            print('Testing search with b=' + str(b) + '... ', end='')
            treeple = self._insert_b(b, b*4)
            for num in treeple[1]:
                assert treeple[0].contains(num) is True
            print('OK')

    def test_dfs_in_order_traversal_odds(self):
         for b in range(3, 20, 2):
            print('Testing in order traversal with b=' + str(b) + '... ', end='')
            treeple = self._insert_b(b, b*4)
            treeple[1].sort()
            assert treeple[0].value_order_traversal() == treeple[1]
            print('OK')       
    
    def test_insert_multi_b(self):
        for b in range(3, 20):
            print('Testing insert with b=' + str(b) + '... ', end='')
            self._insert_b(b, b*4)
            print('OK')

    def test_search_multi_b(self):
        for b in range(3, 20):
            print('Testing search with b=' + str(b) + '... ', end='')
            treeple = self._insert_b(b, b*4)
            for num in treeple[1]:
                assert treeple[0].contains(num) is True
            print('OK')

    def test_dfs_in_order_traversal(self):
         for b in range(3, 20):
            print('Testing in order traversal with b=' + str(b) + '... ', end='')
            treeple = self._insert_b(b, b*4)
            treeple[1].sort()
            assert treeple[0].value_order_traversal() == treeple[1]
            print('OK')       
