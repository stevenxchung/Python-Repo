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
    def test(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            res[0] = max(res[0], left + right)

            return 1 + max(left, right)

        dfs(root)
        return res[0]

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
        TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)),
        TreeNode(1, TreeNode(2)),
    ]
    test.quantify(test_cases)
