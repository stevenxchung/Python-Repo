from time import time
from typing import List


class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, debug=False):
        self.debug = debug
        # Head and tail are pointer nodes
        self.head = self.tail = ListNode()

    def _getNode(self, index: int) -> ListNode:
        '''
        Returns node at index if found, otherwise returns default ListNode.
        '''
        i = -1
        node = self.head
        while node:
            if i == index:
                return node
            i += 1
            node = node.next

        return ListNode()

    def get(self, index: int) -> int:
        '''
        Get node value at given index if exists, otherwise returns default value (-1).
        '''
        res = self._getNode(index).val
        if self.debug:
            print(f'LinkedList[{index}]: {res}')
        return res

    def insertHead(self, val: int) -> None:
        '''
        Insert node at the beginning of the linked list.
        '''
        node = ListNode(val)
        node.next, self.head.next = self.head.next, node
        if not node.next:
            # List was empty before
            self.tail = node

    def insertTail(self, val: int) -> None:
        '''
        Insert node at the end of the linked list.
        '''
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        '''
        Remove node at a specific index if exists (True), otherwise returns False.
        '''
        prev = self._getNode(index - 1)
        curr = prev.next

        if not curr:
            if self.debug:
                print(
                    f'{False}, element does not exist at LinkedList[{index}]!'
                )
            # Node not in bounds
            return False

        prev.next = curr.next
        if not prev.next:
            # Removed the tail node so set new tail
            self.tail = prev

        if self.debug:
            print(f'{True}, removed element at LinkedList[{index}]!')
        return True

    def getValues(self) -> List[int]:
        '''
        Returns all node values in the linked list.
        '''
        res = []
        node = self.head
        while node.next:
            node = node.next
            res.append(node.val)

        if self.debug:
            print(f'LinkedList elements: {res}')
        return res


if __name__ == '__main__':
    sol_start = time()
    print('##### Test 1 #####')
    test = LinkedList(debug=True)
    test.insertHead(1)
    test.insertTail(2)
    test.insertHead(0)
    test.remove(1)  # True
    test.getValues()  # [0, 2]

    print('\n##### Test 2 #####')
    test = LinkedList(debug=True)
    test.insertHead(1)
    test.insertHead(2)
    test.get(5)  # -1

    print('\nAdditional testing...')
    test = LinkedList(debug=True)
    test.insertTail(1)
    test.insertTail(2)
    test.get(1)  # 2
    test.remove(1)  # True
    test.insertTail(2)
    test.get(1)  # 2
    test.get(0)  # 1

    print(f'Runtime for our solution: {time() - sol_start}\n')
