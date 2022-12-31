from collections import Counter, defaultdict, deque
import heapq
from math import inf, sqrt
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
    def test(self, matrix: List[List[int]], target: int) -> bool:
        row = None
        l, r = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        # Find row
        while top <= bottom:
            mid = (top + bottom) // 2
            if target > matrix[mid][r]:
                top = mid + 1
            elif target < matrix[mid][l]:
                bottom = mid - 1
            else:
                row = mid
                break

        if row == None:
            return False

        # Regular binary search
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True

        return False

    def reference():
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.test(*case))
                else:
                    self.test(*case)
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
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13),
        # Additional
        ([[1], [3]], 1),
        ([[1], [3], [5]], 3),
    ]
    test.quantify(test_cases)
