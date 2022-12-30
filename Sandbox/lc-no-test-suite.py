from collections import defaultdict
import heapq
from math import inf
from time import time
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Node:
    def __init__(self, key=0, val=0):
        '''Doubly Linked-list Node'''
        self.key, self.val = key, val
        self.prev = self.next = None


class Solution:
    def __init__(self, capacity: int, debug=False):
        self.debug = debug
        self.capacity = capacity
        self.cache = {}  # {key: Node()}
        # LRU is head and MRU is tail
        self.lru, self.mru = Node(), Node()
        self.lru.next, self.mru.prev = self.mru, self.lru

    def delete(self, node: Node):
        # Delete by linking neighbors
        l, r = node.prev, node.next
        l.next, r.prev = r, l

    def insert(self, node: Node):
        # Every element is added to tail (MRU)
        l, r = self.mru.prev, self.mru
        l.next = r.prev = node
        node.prev, node.next = l, r

    def get(self, key: int) -> int:
        res = -1
        if key in self.cache:
            # Move to tail
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            res = key

        if self.debug:
            print(res)
        return res

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # Over capacity, remove LRU
            lru = self.lru.next
            self.delete(self.cache[lru.key])
            if self.debug:
                print(lru.key)
            del self.cache[lru.key]

        if self.debug:
            print(self.cache.keys())


if __name__ == '__main__':
    test = Solution(2, debug=True)
    sol_start = time()
    test.put(1, 1)  # Cache is {1=1}
    test.put(2, 2)  # Cache is {1=1, 2=2}
    test.get(1)  # Return 1
    test.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    test.get(2)  # Returns -1 (not found)
    test.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    test.get(1)  # Return -1 (not found)
    test.get(3)  # Return 3
    test.get(4)  # Return 4
    print(f'Runtime for our solution: {time() - sol_start}')
