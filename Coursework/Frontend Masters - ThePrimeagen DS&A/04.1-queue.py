import copy
import heapq
import math
import re
from collections import Counter, defaultdict, deque
from math import ceil, inf, sqrt
from time import time
from typing import List, Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Node:
    def __init__(self, val=0, neighbors=None):
        '''Graph node'''
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         '''Special linked-list node'''
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution:
    def __init__(self, nums=[], debug=False) -> None:
        self.nums = nums
        self.debug = debug

    def _enqueue(self, val: int) -> None:
        '''Add element to end of queue'''
        self.nums.append(val)

    def _deque(self) -> None:
        '''Remove element from front of queue'''
        res = self.nums.pop(0) if self._peek() else None
        if self.debug:
            print(res)

    def _peek(self) -> int:
        '''View front of queue'''
        res = self.nums[0] if len(self.nums) > 0 else None
        return res

    def test(self, nums: List[int]) -> List[int]:
        return self.bubble_sort(nums)

    def reference(self, nums: List[int]) -> List[int]:
        return self.test_sort(nums)


if __name__ == '__main__':
    test = Solution(debug=True)
    sol_start = time()
    # First set of tests
    test._enqueue(5)
    test._enqueue(7)
    test._enqueue(9)
    test._deque()
    print(f'There are {len(test.nums)} element(s) in the list')
    # Second set of tests
    test._enqueue(11)
    test._deque()
    test._deque()
    print(test._peek())
    test._deque()
    test._deque()
    print(f'There are {len(test.nums)} element(s) in the list')
    # Third set of tests
    test._enqueue(69)
    print(test._peek())
    print(f'There are {len(test.nums)} element(s) in the list')
    print(f'Runtime for our solution: {time() - sol_start}\n')
