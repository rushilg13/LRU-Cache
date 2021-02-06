# Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    # Deletion from begnning. O(1)
    def delete(self):
        self.head = self.head.next
        self.head.prev = None

    # Insertion at end. O(1)
    def insert_end(self, value):
        newNode = Node(value)
        if self.head==None:
            newNode.prev=None
            self.head = newNode
            self.head.next = None
        else:
            temp = self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next = newNode
            newNode.prev = temp
            newNode.next = None

