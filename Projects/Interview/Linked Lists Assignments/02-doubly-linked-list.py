'''
Create a doubly linked list with methods (i.e., get(), addAtHead(), addAtTail(), addAtIndex(), deleteAtIndex())
'''


class DLNode:
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def get(self, index):
        count = 0
        currentNode = self.head
        while currentNode:
            if count == index:
                return currentNode.value
            currentNode = currentNode.next
            count += 1
        return -1

    def addAtHead(self, value):
        currentNode = self.head
        self.head = DLNode(value)
        self.head.next = currentNode
        if currentNode != None:
            currentNode.prev = self.head

        while currentNode:
            self.tail = currentNode
            currentNode = currentNode.next

    def addAtTail(self, value):
        node = DLNode(value)
        if self.head == None:
            self.head = DLNode(value)
            return

        currentNode = self.head
        while currentNode:
            if currentNode.next == None:
                currentNode.next = node
                node.prev = currentNode
                self.tail = node
                currentNode = currentNode.next
            currentNode = currentNode.next

    def printLinkedListFromHead(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, "<->", end=" ")
            currentNode = currentNode.next
        print("None")

    def printLinkedListFromTail(self):
        currentNode = self.tail
        while currentNode:
            print(currentNode.value, "<->", end=" ")
            currentNode = currentNode.prev
        print("None")


dll = DoublyLinkedList()
dll.addAtHead(3)
dll.addAtHead(2)
dll.addAtHead(1)
# dll.printLinkedListFromTail()
dll.addAtTail(5)
dll.addAtTail(6)
dll.addAtTail(7)
dll.printLinkedListFromHead()
# print(dll.get(3))
