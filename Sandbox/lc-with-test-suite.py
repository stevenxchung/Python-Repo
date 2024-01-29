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
    def test(self, board: List[List[str]]) -> None:
        '''
        - Flip all 'O's connected to edges into '~'
        - BFS/DFS starting from (r + 1, c + 1) until (len(board) - 1, len(board[0]) - 1)
        - Flip all 'O's on path to 'X's
        - Flip back '~' to 'O's
        '''
        clone = board[:]
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, have, want):
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                # Element already set
                or clone[r][c] == want
                # Element is not the one we care about
                or clone[r][c] != have
            ):
                return

            clone[r][c] = want

            dfs(r + 1, c, have, want)
            dfs(r - 1, c, have, want)
            dfs(r, c + 1, have, want)
            dfs(r, c - 1, have, want)

            return

        def handle_edges(have, want):
            for r in range(ROWS):
                dfs(r, 0, have, want)
                dfs(r, COLS - 1, have, want)
            for c in range(COLS):
                dfs(0, c, have, want)
                dfs(ROWS - 1, c, have, want)

        handle_edges('O', '~')

        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                dfs(r, c, 'O', 'X')

        handle_edges('~', 'O')

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
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X'],
        ],
        [['X']],
        [
            ['O', 'O', 'X', 'O'],
            ['O', 'X', 'O', 'X'],
            ['O', 'O', 'X', 'O'],
            ['O', 'O', 'O', 'O'],
        ],
    ]
    test.quantify(test_cases)
