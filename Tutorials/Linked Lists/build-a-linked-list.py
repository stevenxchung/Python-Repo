# Build a linked list and print it from scratch


class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


class LinkedList:
    def __init__(self, head=None):
        self.head = head


ll = LinkedList()
ll.addNode(1)
ll.addNode(2)
ll.addNode(3)
ll.printLinkedList()
