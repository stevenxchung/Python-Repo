'''
Given n sorted linked list, create one sorted linked list
'''


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    # Recursive helper function
    def mergeSorted(self, first, second):
        result = None
        # Base case if first or second node is None
        if first is None:
            return second
        elif second is None:
            return first

        # Current result is one of the nodes and the next node will be the return value of the recursive function
        if first.data <= second.data:
            result = first
            result.next = self.mergeSorted(first.next, second)
        else:
            result = second
            result.next = self.mergeSorted(first, second.next)

        return result

    def mergeKSorted(self, lists):
        lastIndex = len(lists) - 1
        while lastIndex != 0:
            i = 0
            j = lastIndex
            while (i < j):
                lists[i] = self.mergeSorted(lists[i], lists[j])
                i += 1
                j -= 1

                if i >= j:
                    j = lastIndex

            return lists[0]

    def printNodeList(self):
        current = self
        while current:
            print(current.data, '->', end=' ')
            current = current.next
        print('None')


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # Adds to the beginning of the list
    def unshift(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # Adds to the end of the list
    def append(self, data):
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
        # Reuse append method
        current = self.head
        while ll1.head and ll2.head:
            if ll1.head.data <= ll2.head.data:
                self.append(ll1.head.data)
                ll1.head = ll1.head.next
            elif ll1.head.data >= ll2.head.data:
                self.append(ll2.head.data)
                ll2.head = ll2.head.next

        if ll1.head:
            self.append(ll1.head.data)
            ll1.head = ll1.head.next
        else:
            self.append(ll2.head.data)
            ll2.head = ll2.head.next

    def printLinkedList(self):
        current = self.head
        while current:
            print(current.data, '->', end=' ')
            current = current.next
        print('None')

# # Build lists
# l1 = LinkedList()
# l2 = LinkedList()
# l1.append(1)
# l1.append(5)
# l1.append(7)
# l2.append(2)
# l2.append(4)
# l2.append(6)
# l1.printLinkedList()
# l2.printLinkedList()

# # Solution
# l3 = LinkedList()
# l3.mergeTwoSorted(l1, l2)
# l3.printLinkedList()


# Build lists for k sorted lists
# Instead of using the LinkedList() class with self.head we will use the Node() class for merge sort recursion
# First linked list
l1 = Node(1)
l1.next = Node(3)
l1.next.next = Node(5)
l1.next.next.next = Node(7)

# Second linked list
l2 = Node(2)
l2.next = Node(4)
l2.next.next = Node(6)
l2.next.next.next = Node(8)

# Third linked list
l3 = Node(0)
l3.next = Node(9)
l3.next.next = Node(10)
l3.next.next.next = Node(11)

# Display linked lists
l1.printNodeList()
l2.printNodeList()
l3.printNodeList()
# Linked lists in array form
arr = [l1, l2, l3]

# Solution
l4 = Node().mergeKSorted(arr)
l4.printNodeList()
