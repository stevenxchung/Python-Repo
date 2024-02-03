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
    def test(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        '''
        - Build adjacency list of course to prerequisites
        - DFS through prerequisites and add to result
        - Use two sets to track cycles and prevent duplicates
        '''
        adj = {i: [] for i in range(numCourses)}
        for c, pre in prerequisites:
            adj[c].append(pre)

        res = []
        seen, cycle = set(), set()

        def dfs(c):
            if c in cycle:
                return False
            if c in seen:
                return True

            cycle.add(c)
            for pre in adj[c]:
                if not dfs(pre):
                    return False
            cycle.remove(c)
            seen.add(c)
            res.append(c)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

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
        (2, [[1, 0]]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
        (1, []),
        # Additional
        (5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]),
        (3, [[0, 1], [1, 2], [2, 0]]),
        (3, [[0, 1], [0, 2], [1, 2], [2, 1]]),
    ]
    test.quantify(test_cases)
