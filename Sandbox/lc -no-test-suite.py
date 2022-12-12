from collections import defaultdict
import heapq
from time import time
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class Solution:
    def __init__(self, debug=False):
        self.table = defaultdict(list)
        self.debug = debug

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table:
            if self.debug:
                print('Nothing!')
            return ''

        arr = self.table[key]
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m][-1] == timestamp:
                if self.debug:
                    print(arr[m][0])
                return arr[m][0]
            elif arr[m][-1] < timestamp:
                l = m + 1
            else:
                r = m - 1

        if self.debug:
            print('Previous:', arr[m][0])
        return arr[m][0]


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
    print(f'Runtime for our solution: {time() - sol_start}')
