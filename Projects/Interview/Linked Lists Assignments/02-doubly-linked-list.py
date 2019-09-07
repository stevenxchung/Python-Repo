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
            currentNode = currentNode.nextNode
        return -1

    def addAtHead(self, value):
        currentNode = self.head
        self.head = DLNode(value)
        self.head.next = currentNode

    def printLinkedList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, "<->", end=" ")
            currentNode = currentNode.next
        print("None")


dll = DoublyLinkedList()
dll.addAtHead(3)
dll.addAtHead(2)
dll.addAtHead(1)
dll.printLinkedList()
