# Reverse a linked list


class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # Add new node to linked list
    def addNode(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            return

        currentNode = self.head
        while True:
            if currentNode.nextNode == None:
                currentNode.nextNode = newNode
                break
            # Traverse linked list
            currentNode = currentNode.nextNode

    # Reverse a linked list
    def reverse(self):
        currentNode = self.head
        prev = None
        while currentNode:
            nextNode = currentNode.nextNode
            currentNode.nextNode = prev
            prev = currentNode
            currentNode = nextNode
        self.head = prev


    # Print linked list
    def printLinkedList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, "->", end=" ")
            currentNode = currentNode.nextNode
        print("None")


# Building a linked list
ll = LinkedList()
ll.addNode(1)
ll.addNode(2)
ll.addNode(3)
ll.printLinkedList()

# Reverse a linked list
ll.reverse()
ll.printLinkedList()
