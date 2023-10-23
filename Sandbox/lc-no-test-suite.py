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
        self.debug = debug
        self.table = {}  # {key, List[Tuple[time, value]]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.table:
            self.table[key].append((timestamp, value))
        else:
            self.table[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        # NOTE: timestamps are strictly increasing
        res = ''

        if key not in self.table:
            return res

        tup = self.table[key]
        l, r = 0, len(tup) - 1
        while l < r:
            m = (l + r) // 2
            if timestamp < tup[m][0]:
                r = m - 1
            elif timestamp > tup[m][0]:
                l = m + 1
            else:
                res = tup[m][-1]
                if self.debug:
                    print(res)
                return res

        res = tup[r][-1]
        if self.debug:
            print(res)
        # Return the last saved value
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
    print(f'Runtime for our solution: {time() - sol_start}\n')
