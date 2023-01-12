from collections import Counter, defaultdict, deque
import heapq
from math import ceil, inf, sqrt
import queue
from time import time
from typing import List, Optional


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


# class Node:
#     def __init__(self, val=0, neighbors=None):
#         '''Graph Node'''
#         self.val = val
#         self.neighbors = neighbors if neighbors != None else []


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        '''Linked-list Node'''
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def test(self, board: List[List[str]]) -> bool:
        seen_r = defaultdict(set)
        seen_c = defaultdict(set)
        seen_sq = defaultdict(set)

        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '.':
                    continue
                if (
                    board[r][c] in seen_r[r]
                    or board[r][c] in seen_c[c]
                    or board[r][c] in seen_sq[(r // 3, c // 3)]
                ):
                    return False
                seen_r[r].add(board[r][c])
                seen_c[c].add(board[r][c])
                seen_sq[(r // 3, c // 3)].add(board[r][c])

        return True

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
            ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
        ],
        [
            ['8', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
        ],
        # Additional
        [
            ['.', '.', '.', '.', '5', '.', '.', '1', '.'],
            ['.', '4', '.', '3', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '3', '.', '.', '1'],
            ['8', '.', '.', '.', '.', '.', '.', '2', '.'],
            ['.', '.', '2', '.', '7', '.', '.', '.', '.'],
            ['.', '1', '5', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
            ['.', '2', '.', '9', '.', '.', '.', '.', '.'],
            ['.', '.', '4', '.', '.', '.', '.', '.', '.'],
        ],
    ]
    test.quantify(test_cases)
