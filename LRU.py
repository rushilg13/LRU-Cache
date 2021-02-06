import time
start_time = time.time()
# Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LRU:
    def __init__(self):
        self.head = None

    # Deletion from begnning. O(1)
    def delete(self):
        self.head = self.head.next
        self.head.prev = None

    # Insertion at end. O(1)
    def add(self, value):
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

Hashmap = {}

# Execution
lru = LRU()
lru.add(1)
Hashmap[1] = id(1)
lru.add(2)
Hashmap[2] = id(2)
lru.add(3)
Hashmap[3] = id(3)
lru.delete()
lru.add(4)
Hashmap[4] = id(4)
print(Hashmap)

print("--- %s seconds ---" % (time.time() - start_time))
# --- 0.0009982585906982422 seconds ---
