import heapq
from collections import defaultdict
from math import inf
from time import time
from typing import List


class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def to_string(self):
        return f'Node({self.val})'


class DoublyLinkedList:
    def __init__(self, debug=False):
        self.debug = debug
        self.size = 0
        self.head = self.tail = None

    def get_length(self) -> int:
        if self.debug:
            print(f'Length: {self.size}')
        return self.size

    def insert_at(
        self,
        index: int,
        node: Node,
    ):
        if index > self.size - 1:
            if self.debug:
                print('Error, index out of bounds!')
            return

        if index == 0:
            self.prepend(node)
        elif index == self.size - 1:
            self.append(node)
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next

            node.prev, node.next = curr, curr.next
            curr.prev, curr.next = node, node
            self.size += 1

        if self.debug:
            print(f'Added Node({node.val})')

    def remove(self, node: Node) -> Node | None:
        if not node:
            return

        curr = node
        if node == self.head:
            self.head = curr.next
            curr.next, self.head.prev = None, None
        elif node == self.tail:
            self.tail = curr.prev
            curr.prev, self.tail.next = None, None
        else:
            # Otherwise, node is between head and tail
            curr.prev.next, curr.next.prev = curr.next, curr.prev
            node.prev, node.next = None, None
        self.size -= 1

        if self.debug:
            print(f'Removed Node({node.val})')

        return node

    def remove_at(self, index: int) -> Node | None:
        if index > self.size - 1:
            if self.debug:
                print('Error, index out of bounds!')
            return

        curr = self.head
        for _ in range(index):
            curr = curr.next

        return self.remove(curr)

    def append(self, node: Node):
        self.size += 1
        if self.size <= 1:
            self.head = node
            self.tail = node
            return

        curr = self.tail
        curr.next, node.prev = node, curr
        self.tail = node

    def prepend(self, node: Node):
        self.size += 1
        if self.size <= 1:
            self.head = node
            self.tail = node
            return

        curr = self.head
        curr.prev, node.next = node, curr
        self.head = node

    def get(self, index: int) -> Node | None:
        if index > self.size - 1:
            if self.debug:
                print('Error, index out of bounds!')
            return

        curr = self.head
        for _ in range(index):
            curr = curr.next

        if self.debug:
            print(f'Get node @ index={index}: {curr.to_string()}')
        return curr


if __name__ == '__main__':
    test = DoublyLinkedList(debug=True)
    sol_start = time()
    test.append(Node(val=1))
    test.append(Node(val=2))
    test.append(Node(val=3))
    test.get_length()
    # Should return 1, 2, 3
    test.get(0)
    test.get(1)
    test.get(2)
    test.prepend(Node(val=4))
    test.prepend(Node(val=5))
    test.prepend(Node(val=6))
    test.get_length()
    # Should return 6, 5, 4
    test.get(0)
    test.get(1)
    test.get(2)
    test.remove_at(3)
    test.remove_at(3)
    test.remove_at(3)
    test.get_length()
    test.insert_at(0, Node(val=7))
    test.insert_at(1, Node(val=8))
    test.insert_at(2, Node(val=9))
    test.get_length()
    # Should return 7, 8, 9, 1, 2, 3
    test.get(0)
    test.get(1)
    test.get(2)
    test.get(3)
    test.get(4)
    test.get(5)

    print(f'Runtime for our solution: {time() - sol_start}\n')
