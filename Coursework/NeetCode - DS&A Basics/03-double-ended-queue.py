from time import time


class DLNode:
    def __init__(self, val=-1, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class Deque:
    def __init__(self, debug=False):
        self.debug = debug
        self.head = self.tail = DLNode()
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0

    def isEmpty(self) -> bool:
        '''
        Returns True if the list is empty, False otherwise.
        '''
        res = self.size == 0
        if self.debug:
            print(f'isEmpty(): {res}')
        return res

    def append(self, value: int) -> None:
        '''
        Insert at the end of the queue.
        '''
        node = DLNode(value)
        prev = self.tail.prev
        prev.next, node.next = node, self.tail
        self.tail.prev, node.prev = node, prev
        self.size += 1

    def appendleft(self, value: int) -> None:
        '''
        Insert at the beginning of the queue.
        '''
        node = DLNode(value)
        next_node = self.head.next
        self.head.next, node.next = node, next_node
        next_node.prev, node.prev = node, self.head
        self.size += 1

    def pop(self) -> int:
        '''
        Remove element at the end of the queue.
        '''
        if self.size == 0:
            res = -1
        else:
            curr = self.tail.prev
            res = curr.val
            prev = curr.prev
            prev.next, self.tail.prev = self.tail, prev
            self.size -= 1

        if self.debug:
            print(f'pop(): {res}')
        return res

    def popleft(self) -> int:
        '''
        Remove element at the beginning of the queue.
        '''
        if self.size == 0:
            res = -1
        else:
            curr = self.head.next
            res = curr.val
            next_node = curr.next
            self.head.next, next_node.prev = next_node, self.head
            self.size -= 1

        if self.debug:
            print(f'popleft(): {res}')
        return res


if __name__ == '__main__':
    sol_start = time()
    print('##### Test 1 #####')
    test = Deque(debug=True)
    test.isEmpty()  # True
    test.append(10)
    test.isEmpty()  # False
    test.appendleft(20)
    test.popleft()  # 20
    test.pop()  # 10
    test.pop()  # -1
    test.append(30)
    test.pop()  # 30
    test.isEmpty()  # True

    print(f'Runtime for our solution: {time() - sol_start}\n')
