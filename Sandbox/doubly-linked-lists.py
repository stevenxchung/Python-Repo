'''
First, implement a doubly linked list with add(), remove(), and print() methods
Second, implement LRU Cache problem (very popular leet code problem) which
utilizes the get(key) and put(key, value) methods
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
    def __init__(self, val=0, key=0, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next


class DLList:
    def __init__(self, capacity=None, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.cache = {}
        self.capacity = capacity

    def addToFront(self, val, key):
        node = DNode(val, key)
        currentNode = self.head

        # If there is no node
        if currentNode is None:
            self.cache[key] = val
            self.head, self.tail = node, node
            return

        node.next, currentNode.prev = currentNode, node
        self.head = node

        self.cache[key] = val

        # The tail will have to be reset since the linked list has changed
        while currentNode:
            self.tail = currentNode
            currentNode = currentNode.next

    # Actually need to remove at a specific key for LRU Cache
    def removeAtIndex(self, key):
        if key not in self.cache:
            print('Key does not exist!')
            return -1

        # print("Removing node with key = " + str(self.cache[key]) + "...")
        currentNode = self.head
        while currentNode:
            if currentNode.key == key:
                # We also have to remove the key-value pair from the dictionary
                del self.cache[key]
                # At the front of the linked list
                if currentNode.prev is None and currentNode.next is not None:
                    currentNode.next.prev = None
                    self.head = currentNode.next
                # At the end of the linked list
                elif currentNode.next is None:
                    currentNode.prev.next = None
                    self.tail = currentNode.prev
                # Somewhere in the middle
                else:
                    currentNode.prev.next, currentNode.next.prev = (
                        currentNode.next,
                        currentNode.prev,
                    )
            currentNode = currentNode.next

    def get(self, key):
        if key not in self.cache:
            print('Key does not exist!')
            return -1

        val = self.cache[key]
        print("Node found! Moving node to the front of the list...")
        self.removeAtIndex(key)
        self.addToFront(val, key)
        print("Node key:", key, ", Node value:", self.cache[key])

        return key

    def put(self, key, val):
        if len(self.cache) == self.capacity:
            self.removeAtIndex(self.tail.key)
            self.addToFront(val, key)
        else:
            self.addToFront(val, key)

    def printList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.val, '<->', end=' ')
            currentNode = currentNode.next
        print("None")


# Test
# dll = DLList()
# dll.addToFront(3, 3)
# print(dll.cache)
# dll.addToFront(2, 2)
# print(dll.cache)
# dll.addToFront(1, 1)
# print(dll.cache)
# dll.printList()
# dll.removeAtIndex(2)
# print(dll.cache)
# dll.printList()
# dll.get(3)
# dll.printList()

# Test LRU Cache
dll = DLList(2)
dll.put(1, 1)
dll.put(2, 2)
dll.get(1)  # returns 1
dll.put(3, 3)  # evicts key 2
dll.get(2)  # returns -1 (not found)
dll.put(4, 4)  # evicts key 1
dll.get(1)  # returns -1 (not found)
dll.get(3)  # returns 3
dll.get(4)  # returns 4
# dll.printList()
