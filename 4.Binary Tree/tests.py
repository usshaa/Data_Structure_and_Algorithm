from unittest import TestCase
from node import Node
from binary_tree import BinaryTree


class TestBinaryTree(TestCase):
    
    def test_node_creation(self):
        data = [1,2,3,4,5]
        value = 8
        node = Node(data,value)
        self.assertEqual(value,node.value)
        self.assertEqual(data,node.data)