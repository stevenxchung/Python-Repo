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
    def test(
        self, maze: List[str], wall: str, start: Tuple, end: Tuple
    ) -> List[Tuple]:
        ROWS, COLS = len(maze), len(maze[0])
        seen = set()
        # Note: x, y = c, r
        c0, r0 = start

        def dfs(r, c, path):
            if (
                not (0 <= r < ROWS and 0 <= c < COLS)
                or (r, c) in seen
                or maze[r][c] == wall
            ):
                return None

            path.append((c, r))
            if (c, r) == end:
                return path

            seen.add((r, c))

            res = (
                dfs(r + 1, c, path)
                or dfs(r - 1, c, path)
                or dfs(r, c + 1, path)
                or dfs(r, c - 1, path)
            )

            return res if res else None

        return dfs(r0, c0, [])

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
        #             print(self.reference(*case))
        #         else:
        #             self.reference(*case)
        # print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        (
            (
                "xxxxxxxxxx x",
                "x        x x",
                "x        x x",
                "x xxxxxxxx x",
                "x          x",
                "x xxxxxxxxxx",
            ),
            "x",
            (10, 0),
            (1, 5),
        )
    ]
    test.quantify(test_cases)
