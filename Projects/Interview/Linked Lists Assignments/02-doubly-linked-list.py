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

    def linkedListSize(self):
        # We can add a size property for each linked list and increase the size each time a node is added to the list or create a size function. In this case a size function is sufficient
        size = 0
        currentNode = self.head
        while currentNode:
            size += 1
            currentNode = currentNode.next
        return size

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
        # Check edge case
        if currentNode != None:
            currentNode.prev = self.head

        while currentNode:
            self.tail = currentNode
            currentNode = currentNode.next

    def addAtTail(self, value):
        node = DLNode(value)
        # Check edge case
        if self.head == None:
            self.head = DLNode(value)
            return

        currentNode = self.head
        while currentNode:
            if currentNode.next == None:
                currentNode.next = node
                node.prev = currentNode
                self.tail = node
                # Otherwise would continue in a loop
                currentNode = currentNode.next
            currentNode = currentNode.next

    def addAtIndex(self, value, index):
        size = self.linkedListSize()
        count = 1
        node = DLNode(value)

        if index < 0 or index > size:
            print('Index is out of bounds!')
            return -1

        if index == 0:
            self.addAtHead(value)
        elif index == size:
            self.addAtTail(value)
        else:
            currentNode = self.head
            while currentNode:
                if count == index:
                    temp = currentNode.next
                    currentNode.next = node
                    node.prev = currentNode
                    node.next = temp
                currentNode = currentNode.next
                count += 1

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
dll.addAtIndex(9000, 0)
dll.printLinkedListFromHead()
dll.addAtIndex(9000, 1)
dll.printLinkedListFromHead()
dll.addAtIndex(9000, 2)
dll.printLinkedListFromHead()
# print(dll.get(3))
