'''
First, implement a doubly linked list with add(), remove(), and print() methods
Second, implement LRU Cache problem (very popular leet code problem)
'''

# Test (LRU Cache Problem)
# cache = LRUCache()
# cache.put(1, 1)
# cache.put(2, 2)
# cache.get(1)       # returns 1
# cache.put(3, 3)    # evicts key 2
# cache.get(2)       # returns -1 (not found)
# cache.put(4, 4)    # evicts key 1
# cache.get(1)       # returns -1 (not found)
# cache.get(3)       # returns 3
# cache.get(4)       # returns 4


class DNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DLList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def addToFront(self, val):
        currentNode = self.head
        node = DNode(val)
        node.next = currentNode

        if currentNode is not None:
            currentNode.prev = node

        self.head = node

        while currentNode:
            self.tail = currentNode
            currentNode = currentNode.next

    def printList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.val, '<->', end=' ')
            currentNode = currentNode.next
        print("None")

# Test
dll = DLList()
dll.addToFront(3)
dll.addToFront(2)
dll.addToFront(1)
dll.printList()
