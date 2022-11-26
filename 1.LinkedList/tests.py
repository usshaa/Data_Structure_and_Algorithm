from unittest import TestCase
from node import Node
from linkedlist import LinkedList


class TestLinkedList(TestCase):
    
    def test_node_creation(self):
        name = "Jose"
        matric = "1234"
        year = 2
        
        node = Node(name,matric,year)
        
        self.assertEqual(name,node.name)
        self.assertEqual(matric,node.matric)
        self.assertEqual(year,node.year)
        
    def test_list_creation(self):
        linked_list = LinkedList()
        
        self.assertIsNone(linked_list.get_root())
    
    def test_add_to_list(self):
        name = "Jose"
        matric = "1234"
        year = 2
        
        node = Node(name,matric,year)
        
        linked_list = LinkedList()
        
        linked_list.add_to_list(node)
        
        self.assertEqual(linked_list.get_root(),node)
        