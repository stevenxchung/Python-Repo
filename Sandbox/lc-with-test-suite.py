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
        - Build adjacency list of prerequisite to courses
        - Track number of required courses for each course
        - Load queue with initial required courses
        - BFS traverse all courses and add to result
        - Only add courses to queue if all prerequisites met
        - Compare courses taken with total courses to determine output
        '''
        required = [0] * numCourses
        adj = {i: [] for i in range(numCourses)}
        for c, pre in prerequisites:
            adj[pre].append(c)
            required[c] += 1

        q = deque()
        for i in range(numCourses):
            # Start with first required courses
            if required[i] == 0:
                q.append(i)

        res = []
        while q:
            c = q.popleft()
            res.append(c)
            for c_next in adj[c]:
                required[c_next] -= 1
                if required[c_next] == 0:
                    # Only add to queue when all prerequisites taken
                    q.append(c_next)

        return res if len(res) == numCourses else []

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
