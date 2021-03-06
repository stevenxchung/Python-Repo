'''
Tasks:
1. Reverse a linked list
2. Remove linked list elements
3. Odd even linked list
4. Palindrome linked list
'''


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
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

    def removeElements(self, value):
        # If head is null
        if self.head == None:
            return None

        currentNode = self.head
        while currentNode:
            nextNode = currentNode.next
            # Break if next node is None
            if currentNode.next == None:
                break
            # If first node is value, point to none and adjust head
            if currentNode.value == value:
                currentNode.next = None
                self.head = nextNode
                currentNode = self.head
            elif currentNode.next.value == value:
                temp = currentNode.next.next
                currentNode.next.next = None
                currentNode.next = temp
            currentNode = currentNode.next

    def isPalindrome(self):
        # Build stack
        stack = []
        currentNode = self.head
        while currentNode:
            stack.append(currentNode.value)
            currentNode = currentNode.next

        # Reset current node to self.head
        currentNode = self.head
        # Compare each node with top of the stack
        while currentNode:
            if currentNode.value != stack.pop():
                return False
            currentNode = currentNode.next
        return True

    def oddEvenList(self):
        listOne = self.head
        listTwo = listOne.next
        listTwoHead = listTwo
        while listOne and listTwo.next:
            listOne.next = listOne.next.next
            listTwo.next = listTwo.next.next
            # Increment
            listOne = listOne.next
            listTwo = listTwo.next
        listOne.next = listTwoHead

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
            print(currentNode.value, "->", end=" ")
            currentNode = currentNode.next


ll = LinkedList()
ll.appendNode(1)
ll.appendNode(2)
ll.appendNode(3)
ll.appendNode(4)
ll.appendNode(3)
ll.appendNode(2)
ll.appendNode(1)
# print(ll.printLinkedList())
ll.reverse()
print(ll.printLinkedList())
# print(ll.removeElements(1))
# print(ll.oddEvenList())
print(ll.isPalindrome())
