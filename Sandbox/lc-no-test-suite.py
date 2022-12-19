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
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class Solution:
    def __init__(self, k: int, nums: List[int], debug=False):
        self.index = k - 1
        self.heap = [-n for n in nums]
        heapq.heapify(self.heap)
        self.debug = debug

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        if self.debug:
            print(
                f'No.{self.index + 1} largest element: {-self.heap[self.index]}'
            )
        return -self.heap[self.index]


if __name__ == '__main__':
    test = Solution(3, [4, 5, 8, 2], debug=True)
    sol_start = time()
    test.add(3)  # return 4
    test.add(5)  # return 5
    test.add(10)  # return 5
    test.add(9)  # return 8
    test.add(4)  # return 8
    print(f'Runtime for our solution: {time() - sol_start}')
