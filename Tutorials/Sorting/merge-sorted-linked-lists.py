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

    # Merge two list which are already sorted
    def mergeTwoSorted(self, ll1, ll2):
        # Cover edge case
        if ll1.head is None and ll2.head is None:
            return
        
        # Use the insert function to insert into new list
        current = self.head
        while ll1.head and ll2.head:
            if ll1.head.data <= ll2.head.data:
                self.insert(ll1.head.data)
                ll1.head = ll1.head.next
            elif ll1.head.data >= ll2.head.data:
                self.insert(ll2.head.data)
                ll2.head = ll2.head.next

        self.insert(ll1.head.data) if ll1.head.data is not None else self.insert(ll2.head.data)


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
l3 = LinkedList()
l3.insert(8)
l3.insert(9)
l3.insert(10)
l3.mergeTwoSorted(l1, l2)
l3.printLinkedList()

