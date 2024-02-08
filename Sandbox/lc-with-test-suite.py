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
    def test(self, n: int, edges: List[List[int]]) -> bool:
        '''
        - Build adjacency list with source and target nodes
        - DFS traverse graph from root to leaf nodes
        - A valid tree has only one connected component
        - Check that visited nodes matches number of nodes
        '''
        if len(edges) == 0:
            return True

        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)

        seen = set()

        def dfs(node):
            if node in seen:
                return False

            seen.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False

            return True

        return dfs(0) and len(seen) == n

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
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]]),
        # Additional
        (0, []),
        (5, [[0, 1], [0, 2], [0, 3], [1, 4], [0, 4]]),
        (7, [[0, 1], [0, 2], [3, 5], [5, 6], [1, 4]]),
        (7, [[0, 1], [0, 2], [3, 5], [5, 6], [1, 4], [0, 4]]),
    ]
    test.quantify(test_cases)
