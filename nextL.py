# Node stores data and a reference to the next node.
class Node:
    def __init__(self,data, next=None):
        self.data=data # Data stored in the node
        self.next=next

class Linked:
    def __init__(self,head=None):
        self.head=head
    def insert_beginning(self, new_data):
        new_node= Node(new_data)
        new_node.next=self.head
        self.head=new_data


n1=Node("hola")
print(n1.data)
print(n1.next)
        
    