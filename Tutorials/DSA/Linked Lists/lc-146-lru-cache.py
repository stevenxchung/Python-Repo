'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
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

        self.head.next, self.tail.next = self.tail, self.head

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
        node = self.cache.get(key)
        if not node:
            return -1
        self.toFront(node)

        return node.value

    def put(self, key, value):
        node = self.cache.get(key)
        if not node:
            newNode = DLNode()
            newNode.key = key
            newNode.value = value
            self.cache[key] = newNode
            self.addNode(newNode)

            self.size += 1

            if self.size > self.capacity:
                last = self.removeLast()
                del self.cache[last.key]
                self.size -= 1
        else:
            # Change value of existing node
            node.value = value
            self.toFront(node)
