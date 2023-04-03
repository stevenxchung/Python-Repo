from time import time
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PrintTree:
    def preorder_dfs(self, node: Optional[TreeNode]) -> List[int]:
        output = {}

        def dfs(node: Optional[TreeNode], output: List, level: int):
            if not node:
                return
            if level not in output:
                output[level] = node.val
            dfs(node.left, output, level + 1)
            dfs(node.right, output, level + 1)

        dfs(node, output, 1)
        return list(output.values())

    def bfs(self, node: Optional[TreeNode]) -> List[int]:
        output = []
        # {[first_node_at_level_n, ..., last_node_at_level_n], ...}
        temp = {}
        # (node, level)
        queue = [(node, 1)]
        while queue:
            node_temp, level = queue.pop(0)
            if level > 1:
                if level in temp:
                    temp[level].append(node_temp.val)
                else:
                    temp[level] = [node_temp.val]

            if node_temp.left:
                queue.append((node_temp.left, level + 1))
            if node_temp.right:
                queue.append((node_temp.right, level + 1))

        # Rearrange nodes in list
        temp_list = []
        for arr in temp.values():
            temp_list.append(arr[0])
        temp_list.reverse()
        output = temp_list + [node.val]

        for arr in temp.values():
            output.append(arr[-1])

        return output

    def reference(self, node: Optional[TreeNode]) -> List[int]:
        output_left = {}
        output_right = {}

        def left_dfs(node: Optional[TreeNode], output: List, level: int):
            if not node:
                return
            left_dfs(node.left, output, level + 1)
            if level not in output:
                output[level] = node.val
            left_dfs(node.right, output, level + 1)

        def right_dfs(node: Optional[TreeNode], output: List, level: int):
            if not node:
                return
            right_dfs(node.right, output, level + 1)
            if level not in output:
                output[level] = node.val
            right_dfs(node.left, output, level + 1)

        left_dfs(node, output_left, 1)
        right_dfs(node, output_right, 1)
        return list(output_left.values()) + list(output_right.values())[2::-1]

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.bfs(case))
                else:
                    self.bfs(case)
        print(f'Runtime for our solution: {time() - sol_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(case))
                else:
                    self.reference(case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = PrintTree()
    test_cases = [
        TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(9))),
            TreeNode(3, TreeNode(6), TreeNode(7, TreeNode(15))),
        ),
        TreeNode(
            1,
            TreeNode(2, TreeNode(4, TreeNode(9))),
            TreeNode(3, TreeNode(6), TreeNode(7, None, TreeNode(15))),
        ),
    ]
    test.quantify(test_cases)
