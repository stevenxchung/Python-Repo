# Merge two sorted linked lists (from leet code)


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
    # Merge two sorted lists together
    def mergeTwoSorted(self, l1, l2):
        currentNode = self.head
        while l1.head and l2.head:
            if l1.head.value <= l2.head.value:
                self.addNode(l1.head.value)
                l1.head = l1.head.nextNode
            elif l2.head.value <= l1.head.value:
                self.addNode(l2.head.value)
                l2.head = l2.head.nextNode
        # Need to account for the last node because either l1.head or l2.head is None at this point so while loop is broken
        self.addNode(l1.head.value) if l1.head.value is not None else self.addNode(
            l2.head.value)

    def printLinkedList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, "->", end=" ")
            currentNode = currentNode.nextNode
        print("None")


# Build lists
l1 = LinkedList()
l2 = LinkedList()
l1.addNode(1)
l1.addNode(5)
l1.addNode(7)
l2.addNode(2)
l2.addNode(4)
l2.addNode(6)
l1.printLinkedList()
l2.printLinkedList()

# Solution
l3 = LinkedList()
l3.mergeTwoSorted(l1, l2)
l3.printLinkedList()
