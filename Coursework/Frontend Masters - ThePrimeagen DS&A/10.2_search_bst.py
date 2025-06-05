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
    def test(self, root: TreeNode, targets: List[int]) -> List[bool]:
        res = []

        def dfs(node, target):
            if not node:
                return False
            if node.val == target:
                return True
            elif node.val < target:
                # Go right to find greater number
                return dfs(node.right, target)
            # Otherwise, go left to find lesser number
            return dfs(node.left, target)

        for t in targets:
            res.append(dfs(root, t))

        return res

    def reference(self, root: TreeNode, targets: List[int]) -> bool:
        res = []

        def bfs(node, target):
            q = deque([node])
            while q:
                n = q.popleft()
                if n.val == target:
                    return True
                elif n.val > target and n.left:
                    q.append(n.left)
                elif n.val < target and n.right:
                    q.append(n.right)
            return False

        for t in targets:
            res.append(bfs(root, t))

        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.test(*case))
                else:
                    self.test(*case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(*case))
                else:
                    self.reference(*case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_tree = TreeNode(
        15,
        TreeNode(7, TreeNode(4)),
        TreeNode(
            51, TreeNode(25, None, TreeNode(37, TreeNode(32))), TreeNode(100)
        ),
    )
    test_cases = [
        (test_tree, [4, 7, 15, 25, 32, 37, 51, 100]),
        (test_tree, [1, 2, 3, 4, 5]),
    ]
    test.quantify(test_cases)
