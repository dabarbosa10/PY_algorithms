# Node stores data and a reference to the next node.
class Node:
    def __init__(self,data, next=None):
        self.data=data # Data stored in the node
        self.next=next

class Linked:
    def __init__(self,head=None):
        self.head=head
        
    