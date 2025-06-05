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
    def test(self, root_a: TreeNode, root_b: TreeNode) -> bool:
        def dfs(a, b):
            if not a and not b:
                return True
            if not a or not b or a.val != b.val:
                return False

            return dfs(a.left, b.left) and dfs(a.right, b.right)

        return dfs(root_a, root_b)

    def reference(self, root_a: TreeNode, root_b: TreeNode) -> bool:
        q1 = deque([root_a])
        q2 = deque([root_b])

        while q1 and q2:
            n1 = q1.popleft()
            n2 = q2.popleft()

            # Check if trees match
            if n1.val != n2.val:
                return False
            if (
                (n1.left and not n2.left)
                or (not n1.left and n2.left)
                or (n1.right and not n2.right)
                or (not n1.right and n2.right)
            ):
                # One of the branches is null
                return False

            if n1.left and n2.left:
                q1.append(n1.left)
                q2.append(n2.left)

            if n1.right and n2.right:
                q1.append(n1.right)
                q2.append(n2.right)

        return True

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
    test_cases = [
        (
            TreeNode(
                5,
                TreeNode(3),
                TreeNode('0x45'),
            ),
            TreeNode(
                5,
                TreeNode(3, TreeNode('0x45')),
            ),
        ),
        (
            TreeNode(
                7,
                TreeNode(23, TreeNode(5), TreeNode(4)),
                TreeNode(8, TreeNode(21), TreeNode(15)),
            ),
            TreeNode(
                7,
                TreeNode(23, TreeNode(5), TreeNode(4)),
                TreeNode(8, TreeNode(21), TreeNode(15)),
            ),
        ),
    ]
    test.quantify(test_cases)
