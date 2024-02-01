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
    def test(self, rooms: List[List[int]]) -> List[List[int]]:
        '''
        - Multi-source BFS starting from known gates
        - Mark distance from each gate until queue is empty
        '''
        clone = rooms[:]
        ROWS, COLS = len(clone), len(clone[0])
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if clone[r][c] == 0:
                    q.append((0, r, c))

        ignore = {-1, 0}
        while q:
            dist, r1, c1 = q.popleft()
            for dr, dc in moves:
                r2, c2 = r1 + dr, c1 + dc
                if (
                    r2 < 0
                    or c2 < 0
                    or r2 >= ROWS
                    or c2 >= COLS
                    or clone[r2][c2] in ignore
                    or clone[r2][c2] != inf
                ):
                    continue
                q.append((dist + 1, r2, c2))
                clone[r2][c2] = dist + 1

        return clone

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
            [inf, -1, 0, inf],
            [inf, inf, inf, -1],
            [inf, -1, inf, -1],
            [0, -1, inf, inf],
        ]
    ]
    test.quantify(test_cases)
