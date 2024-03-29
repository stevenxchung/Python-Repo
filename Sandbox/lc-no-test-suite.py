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
    def __init__(self, debug=False):
        '''
        - Store hashmap of key to list of (time, value) tuples
        - Retrieve based on key and timestamp
        - To speed up retrieval, use binary search on timestamp
        '''
        self.debug = debug
        self.table = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        if key not in self.table:
            if self.debug:
                print(f'get({key, timestamp}): {res}')
            return res

        arr = self.table[key]
        l, r = 0, len(arr) - 1
        while l <= r:
            m = l + (r - l) // 2
            if arr[m][0] <= timestamp:
                res = arr[m][-1]
                l = m + 1
            else:
                r = m - 1

        if self.debug:
            print(f'get({key, timestamp}): {res}')
        return res


if __name__ == '__main__':
    test = Solution(debug=True)
    sol_start = time()
    # Store the key 'foo' and value 'bar' along with timestamp = 1.
    test.set('foo', 'bar', 1)
    # Return 'bar'
    test.get('foo', 1)
    # Return 'bar', since there is no value corresponding to 'foo' at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is 'bar'.
    test.get('foo', 3)
    # Store the key 'foo' and value 'bar2' along with timestamp = 4.
    test.set('foo', 'bar2', 4)
    # Return 'bar2'
    test.get('foo', 4)
    # Return 'bar2'
    test.get('foo', 5)

    print('\nAdditional testing...')
    test.set('foo', 'bar3', 7)
    test.get('yeet', 5)  # Return ""
    test.get('foo', 1)  # Return 'bar'
    test.get('foo', 2)  # Return 'bar'
    test.get('foo', 3)  # Return 'bar'
    test.get('foo', 4)  # Return 'bar2'
    test.get('foo', 5)  # Return 'bar2'
    test.get('foo', 6)  # Return 'bar2'
    test.get('foo', 7)  # Return 'bar3'
    test.get('foo', 8)  # Return 'bar3'
    print(f'Runtime for our solution: {time() - sol_start}\n')
