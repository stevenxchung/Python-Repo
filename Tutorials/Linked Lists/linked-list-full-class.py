# Two simple ways to code linked lists in python
# This goes over the full class for linked lists


class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = linkedListNode(value)
        if self.head is None:
            self.head = node
            return

        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, "->", end=" ")
            currentNode = currentNode.nextNode
        print("None")


ll = linkedList()
ll.printLinkedList()
ll.insert(5)
ll.printLinkedList()
ll.insert(10)
ll.printLinkedList()
ll.insert(15)
ll.printLinkedList()
