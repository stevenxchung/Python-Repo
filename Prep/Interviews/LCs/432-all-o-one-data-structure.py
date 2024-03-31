'''
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

- AllOne() Initializes the object of the data structure.
- inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
- dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
- getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
- getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".

Note that each function must run in O(1) average time complexity.
'''
from math import inf
from time import time


class DLNode:
    def __init__(self, key='', val=1):
        self.key = key
        self.val = val
        self.prev = self.next = None


class Solution:
    def __init__(self, debug=False):
        self.debug = debug
        self.s_map = {}
        # Head starts at 0 since max is to the right
        # Tail starts at inf since min is to the left
        self.head, self.tail = DLNode(val=0), DLNode(val=inf)
        self.head.next, self.tail.prev = self.tail, self.head

    def _move_node_left(self, node):
        l, r = node.prev, node.next
        # Swap with left node and reassign pointers
        l.prev.next, node.prev = node, l.prev
        l.prev, node.next = node, l
        l.next, r.prev = r, l

    def _move_node_right(self, node):
        l, r = node.prev, node.next
        # Swap with right node and reassign pointers
        r.next.prev, node.next = node, r.next
        r.next, node.prev = node, r
        r.prev, l.next = l, r

    def _delete_node(self, key, node):
        l, r = node.prev, node.next
        l.next, r.prev = r, l
        node.prev, node.next = None, None
        del self.s_map[key]

    def inc(self, key: str) -> None:
        if key not in self.s_map:
            # Insert new node at tail
            node = self.s_map[key] = DLNode(key)
            curr_min = self.tail.prev
            curr_min.next, node.prev = node, curr_min
            self.tail.prev, node.next = node, self.tail
        else:
            # Otherwise key is already in map, so increment value and move node up if necessary
            node = self.s_map[key]
            node.val += 1
            if node.val > node.prev.val and node.prev != self.head:
                self._move_node_left(node)

    def dec(self, key: str) -> None:
        # Guaranteed to exist before decrement
        node = self.s_map[key]
        node.val -= 1
        if node.val == 0:
            self._delete_node(key, node)
            return
        if node.val < node.next.val:
            self._move_node_right(node)

    def getMaxKey(self) -> str:
        res = self.head.next.key
        if self.debug:
            print(f'Max key={res}')
        return res

    def getMinKey(self) -> str:
        res = self.tail.prev.key
        if self.debug:
            print(f'Min key={res}')
        return res


if __name__ == '__main__':
    test = Solution(debug=True)  # None
    sol_start = time()
    test.inc('hello')
    test.inc('hello')
    test.getMaxKey()  # return 'hello'
    test.getMinKey()  # return 'hello'
    test.inc('leet')
    test.getMaxKey()  # return 'hello'
    test.getMinKey()  # return 'leet'

    # Additional
    print('\nAdditional testing...')
    test.inc('yeet')
    test.inc('hello')
    test.inc('leet')
    test.getMaxKey()  # return 'hello'
    test.getMinKey()  # return 'yeet'
    test.dec('hello')
    test.getMaxKey()  # return 'hello'
    test.getMinKey()  # return 'yeet'
    test.dec('hello')
    test.getMaxKey()  # return 'leet'
    test.getMinKey()  # return 'yeet'
    test.dec('hello')
    test.getMaxKey()  # return 'leet'
    test.getMinKey()  # return 'yeet'
    test.inc('yeet')
    test.inc('yeet')
    test.getMaxKey()  # return 'yeet'
    test.getMinKey()  # return 'leet'

    print(f'Runtime for our solution: {time() - sol_start}\n')
