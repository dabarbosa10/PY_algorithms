class Node:
    def __init__(self, value, next_node=None):
        self.value=value
        self.next_node=next_node

    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self,next_node):
        self.next_node=next_node

class LinkedList:
    def __init__(self, value=None):
        self.value=value
        self.head_node=Node(self.value)
    
    def get_head_node(self):
        return self.head_node
    
    def stringify_list(self):
        string_list=''
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list


my_node=Node(44)
print(my_node.get_value())

