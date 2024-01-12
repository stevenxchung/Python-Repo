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
    def test(self, s: str, k: int) -> int:
        '''
        - Sliding window w/ two pointers
        - Hashmap to track count
        - Replacement char count = substr - longest char count
        - Shrink window when k > replacement char count
        '''
        count_map = defaultdict(int)
        longest = 0
        res = 0

        l = 0
        for r in range(len(s)):
            count_map[s[r]] += 1
            # Next character could be the longest
            longest = max(longest, count_map[s[r]])

            if k < (len(s[l : r + 1])) - longest:
                # Shrink window if replacements exceeds limit
                count_map[s[l]] -= 1
                l += 1

            res = max(res, (len(s[l : r + 1])))

        return res

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
        ('ABAB', 2),
        ('AABABBA', 1),
        # Additional
        ('AAABAAABAAAB', 1),
        ('BBAABBAABBAA', 2),
        ('AAAABAAAABAA', 3),
        ('XXYYZZXXYYZZ', 4),
        ('AAABBCAAABBC', 5),
    ]
    test.quantify(test_cases)
