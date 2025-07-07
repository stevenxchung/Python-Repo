import copy
import heapq
import math
import re
from collections import Counter, defaultdict, deque
from math import ceil, inf, sqrt
from time import time
from typing import Dict, List, Optional, Tuple


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
        """Graph node"""
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         '''Special linked-list node'''
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution:
    def test(self, adj_list: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for a, b in adj_list:
            adj_list[a].append(b)

        res = [0]
        seen = set()
        seen.add(0)

        def dfs(curr):
            if curr not in adj_list or adj_list[curr] == []:
                return

            for nei in adj_list[curr]:
                if nei not in seen:
                    res.append(nei)
                    seen.add(nei)
                    dfs(nei)

            return

        dfs(0)
        return res

    def reference(self):
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.test(case))
                else:
                    self.test(case)
        print(f"Runtime for our solution: {time() - sol_start}\n")

        # ref_start = time()
        # for i in range(0, runs):
        #     for case in test_cases:
        #         if i == 0:
        #             print(self.reference(case))
        #         else:
        #             self.reference(case)
        # print(f'Runtime for reference: {time() - ref_start}')


if __name__ == "__main__":
    test = Solution()
    test_cases = [
        [
            [0, 1],  # [start, end]
            [0, 2],
            [1, 4],
            [2, 3],
            [4, 1],
            [4, 3],
            [4, 5],
            [5, 2],
            [5, 6],
            [6, 3],
        ],
    ]
    test.quantify(test_cases)
