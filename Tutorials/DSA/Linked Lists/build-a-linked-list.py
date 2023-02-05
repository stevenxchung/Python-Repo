# Build a linked list and print it from scratch


class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # Adds node to the end of the list
    def addNode(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            return

        # Start at the head node
        currentNode = self.head
        while True:
            if currentNode.nextNode == None:
                currentNode.nextNode = node
                break
            # Traverse through linked list
            currentNode = currentNode.nextNode

    def printLinkedList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, "->", end=" ")
            currentNode = currentNode.nextNode
        print("None")


ll = LinkedList()
ll.addNode(1)
ll.addNode(2)
ll.addNode(3)
ll.printLinkedList()
