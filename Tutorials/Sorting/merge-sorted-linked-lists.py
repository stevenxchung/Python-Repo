'''
Given n sorted linked list, create one sorted linked list
'''


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linkedList:
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


ll = linkedList()
ll.printLinkedList()
ll.insert(5)
ll.printLinkedList()
ll.insert(10)
ll.printLinkedList()
ll.insert(15)
ll.printLinkedList()
