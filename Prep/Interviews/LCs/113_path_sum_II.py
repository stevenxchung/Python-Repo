'''
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
'''

from time import time
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(
        self, root: Optional[TreeNode], targetSum: int
    ) -> List[List[int]]:
        '''
        - DFS traverse tree until target reached (must do pre-check)
        - Track path and total on each recursion
        - Continue until all options exhausted
        '''
        res = []

        def dfs(node, path, total):
            if not node:
                return

            # Pre-check to avoid adding duplicate paths
            if (
                not node.left
                and not node.right
                and total + node.val == targetSum
            ):
                path.append(node.val)
                res.append(path[:])
                return

            dfs(node.left, path + [node.val], total + node.val)
            dfs(node.right, path + [node.val], total + node.val)

            return

        dfs(root, [], 0)
        return res

    def reference(
        self, root: Optional[TreeNode], targetSum: int
    ) -> List[List[int]]:
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.pathSum(*case))
                else:
                    self.pathSum(*case)
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
                TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None),
                TreeNode(
                    8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))
                ),
            ),
            22,
        ),
        (TreeNode(1, TreeNode(2), TreeNode(3)), 5),
        (TreeNode(1, TreeNode(2)), 0),
    ]
    test.quantify(test_cases)
