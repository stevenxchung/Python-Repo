'''
Given n sorted linked list, create one sorted linked list
'''


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def printLinkedList(self):
        current = self.head
        while current:
            print(current.data, '->', end=' ')
            current = current.next
        print('None')


# Build lists
l1 = LinkedList()
l2 = LinkedList()
l1.insert(1)
l1.insert(5)
l1.insert(7)
l2.insert(2)
l2.insert(4)
l2.insert(6)
l1.printLinkedList()
l2.printLinkedList()

# Solution
# l3 = LinkedList()
# l3.mergeTwoSorted(l1, l2)
# l3.printLinkedList()

