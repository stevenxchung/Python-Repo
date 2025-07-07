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
    def test(self, adj_list: List[List[int]], start: int, end: int) -> List[int]:
        adj_list = defaultdict(list)
        for s, e, w in adj_list:
            adj_list[s].append((w, e))

        seen = set()
        q = [(0, start, [start])]

        while q:
            w1, node, path = heapq.heappop(q)
            if node == end:
                return path
            seen.add(node)
            for w2, nei in adj_list[node]:
                if nei in seen:
                    continue
                heapq.heappush(q, (w1 + w2, nei, path + [nei]))

        return []

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
        (
            [
                [0, 1, 3],  # [start, end, weight]
                [0, 2, 1],
                [1, 0, 3],
                [1, 2, 4],
                [1, 4, 1],
                [2, 1, 4],
                [2, 3, 7],
                [2, 0, 1],
                [3, 2, 7],
                [3, 4, 5],
                [3, 6, 1],
                [4, 1, 1],
                [4, 3, 5],
                [4, 5, 2],
                [5, 6, 1],
                [5, 4, 2],
                [5, 2, 18],
                [6, 3, 1],
                [6, 5, 1],
            ],
            0,
            6,
        ),
    ]
    test.quantify(test_cases)
