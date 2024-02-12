# LC w/ Test Suite
from collections import Counter, defaultdict, deque
import copy
import heapq
from math import ceil, inf, sqrt
import re
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
    def test(self, nums: List[int], target: int) -> int:
        '''
        - Given sorted array of distinct values
        - Compare nums[l] to nums[r] to check for rotation
        - Binary search depending on which section target
        '''
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[l] <= nums[m]:
                # Left sorted
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            else:
                # Right sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m

        return l if nums[l] == target else -1

    def reference(self):
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.test(*case))
                else:
                    self.test(*case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        # ref_start = time()
        # for i in range(0, runs):
        #     for case in test_cases:
        #         if i == 0:
        #             print(self.reference(case))
        #         else:
        #             self.reference(case)
        # print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([4, 5, 6, 7, 0, 1, 2], 3),
        ([1], 0),
        # Additional
        ([3, 1], 3),
        ([5, 1, 3], 3),
        ([5, 1, 3], 1),
    ]
    test.quantify(test_cases)
