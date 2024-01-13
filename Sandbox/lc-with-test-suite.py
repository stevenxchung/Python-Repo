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
    def test(self, s1: str, s2: str) -> bool:
        '''
        - Sliding window of length s1
        - Build hashmap for s1 and s2 substring
        - Compare s1 and s2 hashmap to determine outcome
        '''
        s1_map, curr_map = defaultdict(int), defaultdict(int)
        for c in s1:
            s1_map[c] += 1

        l = 0
        for r in range(len(s2)):
            curr = s2[l : r + 1]
            curr_map[s2[r]] += 1
            if s1_map == curr_map:
                return True

            if len(curr) == len(s1):
                curr_map[s2[l]] -= 1
                if curr_map[s2[l]] == 0:
                    del curr_map[s2[l]]
                l += 1

        return False

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
        ('ab', 'eidbaooo'),
        ('ab', 'eidboaoo'),
        # Additional
        ('hello', 'ooolleoooleh'),
        ('adc', 'dcda'),
    ]
    test.quantify(test_cases)
