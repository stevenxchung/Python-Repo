# Resources from the following links:
# https://www.geeksforgeeks.org/dfs-traversal-of-a-tree-using-recursion/
# https://www.geeksforgeeks.org/level-order-tree-traversal/


from time import time
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def test(self, node: Optional[TreeNode]) -> List[int]:
        inorder, preorder, postorder = [], [], []

        def inorder_dfs(node):
            if not node:
                return

            inorder_dfs(node.left)
            inorder.append(node.val)
            inorder_dfs(node.right)

        def preorder_dfs(node):
            if not node:
                return

            preorder.append(node.val)
            preorder_dfs(node.left)
            preorder_dfs(node.right)

        def postorder_dfs(node):
            if not node:
                return

            postorder_dfs(node.left)
            postorder_dfs(node.right)
            postorder.append(node.val)

        inorder_dfs(node)
        preorder_dfs(node)
        postorder_dfs(node)
        return inorder, preorder, postorder

    def reference(self, node: Optional[TreeNode]) -> List[int]:
        res = []

        q = [node]

        while q:
            node = q.pop(0)
            res.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.test(case))
                else:
                    self.test(case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(case))
                else:
                    self.reference(case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    ]
    test.quantify(test_cases)
