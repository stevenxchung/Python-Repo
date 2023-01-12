from collections import Counter, defaultdict, deque
import heapq
from math import ceil, inf, sqrt
import queue
from time import time
from typing import List, Optional


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


# class Node:
#     def __init__(self, val=0, neighbors=None):
#         '''Graph Node'''
#         self.val = val
#         self.neighbors = neighbors if neighbors != None else []


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        '''Linked-list Node'''
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def test(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_table, t_table = {}, {}
        for i in range(len(s)):
            s_table[s[i]] = s_table.get(s[i], 0) + 1
            t_table[t[i]] = t_table.get(t[i], 0) + 1

        if s_table == t_table:
            return True
        else:
            return False

    def reference():
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.test(*case))
                else:
                    self.test(*case)
        print(f'Runtime for our solution: {time() - sol_start}')

        # ref_start = time()
        # for i in range(0, runs):
        #     for case in test_cases:
        #         if i == 0:
        #             print(self.reference(*case))
        #         else:
        #             self.reference(*case)
        # print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [('anagram', 'nagaram'), ('rat', 'car')]
    test.quantify(test_cases)
