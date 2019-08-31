# Reverse a linked list

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def appendNode(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            return
        
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = node

    def reverse(self):
        currentNode = self.head
        prev = None
        while currentNode:
            temp = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = temp
        self.head = prev
        return prev

    def printLinkedList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, "->", end = " ")
            currentNode = currentNode.next

ll = LinkedList()
ll.appendNode(1)
ll.appendNode(2)
ll.appendNode(3)
print(ll.printLinkedList())
ll.reverse()
print(ll.printLinkedList())