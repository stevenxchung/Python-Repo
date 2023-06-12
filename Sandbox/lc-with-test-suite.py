from collections import Counter, defaultdict, deque
import heapq
from math import ceil, inf, sqrt
import math
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
        self.neighbors = neighbors if neighbors != None else []


# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         '''Special linked-list node'''
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution:
    def test(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        coord = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = [(r, c)]
            while q:
                r1, c1 = q.pop(0)
                seen.add((r1, c1))
                for dr, dc in coord:
                    r2, c2 = r1 + dr, c1 + dc
                    if (
                        r2 < 0
                        or c2 < 0
                        or r2 >= ROWS
                        or c2 >= COLS
                        or (r2, c2) in seen
                        or grid[r2][c2] == '0'
                    ):
                        continue
                    q.append((r2, c2))

            return

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in seen and grid[r][c] == '1':
                    bfs(r, c)
                    res += 1

        return res

    def reference():
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.test(case))
                else:
                    self.test(case)
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
    test_cases = [
        [
            ['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0'],
        ],
        [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1'],
        ],
        # Additional
        [['1']],
    ]
    test.quantify(test_cases)
