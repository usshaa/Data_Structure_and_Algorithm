from unittest import TestCase
from node import Node
from linkedlist import LinkedList
from linkedqueue import LinkedQueue


class TestLinkedList(TestCase):
    
    def test_node_creation(self):
        name = "Jose"
        phone = "123-456-7898"
        
        node = Node(name,phone)
        
        self.assertEqual(name,node.name)
        self.assertEqual(phone,node.phone)
        
        
    def test_list_creation(self):
        linked_list = LinkedList()
    
        self.assertIsNone(linked_list.get_root())
    
    def test_add_to_list_start(self):
        name = "Jose"
        phone = "123-456-7898"
        
        node = Node(name,phone)
        
        linked_list = LinkedList()
        
        linked_list.add_start_to_list(node)
        
        self.assertEqual(linked_list.get_root(),node)
        
    def test_add_many_to_list_start(self):
        names = ("Jose","1234-356"),("Rolf","2345-1-53563-2"),("Anna","345623-16779-3")
        
        nodes = [Node(name,phone) for name, phone in names]
        
        linked_list = LinkedList()
        
        for node in nodes:
            linked_list.add_start_to_list(node)
            
        marker = linked_list.get_root()
        for i in range(len(nodes)-1,-1,-1):
            self.assertEqual(marker,nodes[i])
            marker = marker.get_next()
            
    def test_remove_end_from_list(self):
        names = ("Jose","1234-356"),("Rolf","2345-1-53563-2"),("Anna","345623-16779-3")
        
        