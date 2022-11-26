class BinaryTree:
    
    
    def __init__(self):
        self.__root = None
    
    def get_root(self):
        return self.__root
    
    def add(self,node):
        if not self.__root:
            self.__root = node
        else:
            marker = self.__root
            while marker:
                if node.value == marker.value:
                    raise ValueError("A node with that value alreay exists.")
                elif node.value > marker.value:
                    if not marker.get_right():
                        marker.set_right(node)
                        return
                    else:
                        marker = marker.get_right()
                else:
                    if not marker.get_left():
                        marker.set_left(node)
                        return
                    else:
                        marker = marker.get_left()
    def find(self,value):
        marker = self.__root
        while marker:
            if value == marker.value:
                return marker
            elif value > marker.value:
                return marker.get_right()
            else:
                return marker.get_left()
        raise LookupError("A node with value {} was not found.".format(value))
    
    # def print_inorder(self):
    #     self.__print_inorder_r(self.__root)
        
    # def __print_inorder_r(self,current_node):
    #     if not current_node:
            
        