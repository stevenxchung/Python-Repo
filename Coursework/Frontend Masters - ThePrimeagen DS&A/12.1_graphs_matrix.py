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
    def test(self, adj_matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(adj_matrix), len(adj_matrix[0])
        adj = {i: [] for i in range(len(adj_matrix))}
        for r in range(ROWS):
            for c in range(COLS):
                if adj_matrix[r][c] > 0:
                    adj[r].append(c)

        res = [0]
        seen = set()
        seen.add(0)
        q = deque(adj[0])

        while q:
            node = q.popleft()
            if node in seen:
                continue
            res.append(node)
            seen.add(node)
            for nei in adj[node]:
                if nei in seen:
                    continue
                q.append(nei)

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
        [
            [0, 3, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 7, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 5, 0, 2, 0],
            [0, 0, 18, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 1],
        ],
    ]
    test.quantify(test_cases)
