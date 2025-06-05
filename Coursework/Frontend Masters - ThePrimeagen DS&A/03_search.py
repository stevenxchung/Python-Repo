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
    def linear_search(self, target: int, haystack: List[int]) -> bool:
        return target in haystack

    def binary_search(self, target: int, haystack: List[int]) -> bool:
        l, r = 0, len(haystack) - 1
        while l <= r:
            m = (l + r) // 2
            m_val = haystack[m]
            if m_val == target:
                return True
            elif target < m_val:
                r = m - 1
            else:
                l = m + 1
        return False

    def test(self, target: int, haystack: List[int]) -> bool:
        return self.linear_search(target, haystack)

    def reference(self, target: int, haystack: List[int]) -> bool:
        return self.binary_search(target, haystack)

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.test(*case))
                else:
                    self.test(*case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(*case))
                else:
                    self.reference(*case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        (69, [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]),
        (1336, [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]),
        (69420, [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]),
        (69421, [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]),
        (1, [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]),
        (0, [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]),
    ]
    test.quantify(test_cases)
