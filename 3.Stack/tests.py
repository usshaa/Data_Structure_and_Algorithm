from unittest import TestCase
from node import Node
from linkedlist import LinkedList
from linkedstack import LinkedStack


class TestLinkedList(TestCase):
    
    def test_node_creation(self):
        text = "Stack Input"
        
        node = Node(text)
        
        self.assertEqual(text,node.text)
        
    def test_list_creation(self):
        linked_list = LinkedList()
    
        self.assertIsNone(linked_list.get_root())
    
    def test_add_to_list_start(self):
        text = "Stack Input"
        
        node = Node(text)
        
        linked_list = LinkedList()
        
        linked_list.add_start_to_list(node)
        
        self.assertEqual(linked_list.get_root(),node)
            
    def test_remove_start_from_list(self):
        text = "Stack Input"
        
        node = Node(text)
        
        linked_list = LinkedList()
        
        linked_list.remove_start_from_list()
        
        self.assertEqual(linked_list.size(),node)
        
        