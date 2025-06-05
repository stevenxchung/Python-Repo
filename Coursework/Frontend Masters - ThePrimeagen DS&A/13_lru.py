import heapq
from collections import defaultdict
from math import inf
from time import time
from typing import List


class Node:
    def __init__(self, key='', val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def to_string(self):
        return f'Node({self.val})'


class LRUCache:
    def __init__(self, capacity=0, debug=False):
        self.capacity = capacity
        # Start with dummy nodes for easier handling
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head
        self.cache = {}
        self.debug = debug

    def _add(self, node: Node):
        if node.key in self.cache:
            return
        # Recall that head is a dummy node
        head, next = self.head, self.head.next
        head.next = next.prev = node
        node.prev, node.next = head, next
        self.cache[node.key] = node

    def _delete(self, node: Node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        del self.cache[node.key]

    def get(self, key: str) -> int:
        # Get node from cache
        if key not in self.cache:
            if self.debug:
                print(f'Node does not exist when key = {key}!')
            return None

        # Move node from current position to head
        node = self.cache[key]
        self._delete(node)
        self._add(node)

        if self.debug:
            print(f'Node ({node.key}, {node.val})')

        return node.val

    def put(self, key, value):
        # Evict tail if full
        if len(self.cache) == self.capacity:
            # Recall that tail is a dummy node
            tail = self.tail.prev
            self._delete(tail)
            if self.debug:
                print(f'Evicting LRU node ({tail.key}, {tail.val})')

        if key in self.cache:
            # Update value if node already exists
            node = self.cache[key]
            node.val = value
            self._delete(node)
        else:
            node = Node(key=key, val=value)

        # Add node to cache, add node to head
        self._add(node)


if __name__ == '__main__':
    test = LRUCache(capacity=3, debug=True)
    sol_start = time()
    test.get('foo')  # None
    test.put('foo', 69)
    test.get('foo')  # 69

    test.put('bar', 420)
    test.get('bar')  # 420

    test.put('baz', 1337)
    test.get('baz')  # 1337

    test.put('ball', 69420)
    test.get('ball')  # 69420
    # The key 'foo' is popped off
    test.get('foo')  # None
    test.get('bar')  # 420
    test.put('foo', 69)
    test.get('bar')  # 420
    test.get('foo')  # 69

    # The key 'baz' is popped off
    test.get('baz')  # None

    print(f'Runtime for our solution: {time() - sol_start}\n')
