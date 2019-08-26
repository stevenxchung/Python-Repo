'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.
'''


class DLNode:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLNode(), DLNode()

        self.head.next, self.next.tail = self.tail, self.head

    # Add to front
    def addNode(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev, self.head = node, node

    # Removes node from anywhere
    def removeNode(self, node):
        prev, nextNode = node.prev, node.next
        prev.next, nextNode.prev = nextNode, prev

    # Moves node to front
    def toFront(self, node):
        self.removeNode(node)
        self.addNode(node)

    # Removes last node
    def removeLast(self):
        last = self.tail.prev
        self.removeLast(last)
        return last

    def get(self, key):

    def put(self, key, value):
