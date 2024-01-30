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
    def test(self, grid: List[List[int]]) -> int:
        '''
        - Multi-source BFS starting w/ rotten oranges
        - Run until all oranges are rotten or queue is empty
        '''
        ROWS, COLS = len(grid), len(grid[0])

        q = deque([])
        seen = set()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
                    seen.add((r, c))

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        t = 0
        while fresh > 0 and q:
            # Multi-source BFS
            for _ in range(len(q)):
                r1, c1 = q.popleft()
                if fresh == 0:
                    return t

                for dr, dc in moves:
                    r2, c2 = r1 + dr, c1 + dc
                    if (
                        r2 < 0
                        or c2 < 0
                        or r2 >= ROWS
                        or c2 >= COLS
                        or (r2, c2) in seen
                        or grid[r2][c2] != 1
                    ):
                        continue
                    q.append((r2, c2))
                    seen.add((r2, c2))
                    fresh -= 1
            # Add to time after each big iteration
            t += 1

        return -1 if fresh > 0 else t

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
        [[2, 1, 1], [1, 1, 0], [0, 1, 1]],
        [[2, 1, 1], [0, 1, 1], [1, 0, 1]],
        [[0, 2]],
    ]
    test.quantify(test_cases)
