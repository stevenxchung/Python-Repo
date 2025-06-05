'''
Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.

Return the root of the Quad-Tree representing grid.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

- val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
- isLeaf: True if the node is a leaf node on the tree or False if the node has four children.

class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}

We can construct a Quad-Tree from a two-dimensional area using the following steps:

1. If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
2. If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
3. Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki (https://en.wikipedia.org/wiki/Quadtree).

Quad-Tree format:

You don't need to read this section for solving the problem. This is only if you want to understand the output format here. The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.
'''

from time import time
from typing import List


class Node:
    def __init__(
        self,
        val=False,
        is_leaf=False,
        top_left=None,
        top_right=None,
        bottom_left=None,
        bottom_right=None,
    ):
        self.val = val
        self.is_leaf = is_leaf
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        '''
        - DFS traverse the grid dividing the search space in half each time
        - Use the top left corner of the search space as source of comparison
        '''

        def same_values(r, c, w):
            # Check if values match top left square
            for i in range(r, r + w):
                for j in range(c, c + w):
                    if grid[i][j] != grid[r][c]:
                        return False
            return True

        def dfs(r, c, w):
            if same_values(r, c, w):
                # Leaf node path
                return Node(grid[r][c] == 1, True)

            node = Node(True, False)
            node.top_left = dfs(r, c, w // 2)
            node.top_right = dfs(r, c + w // 2, w // 2)
            node.bottom_left = dfs(r + w // 2, c, w // 2)
            node.bottom_right = dfs(r + w // 2, c + w // 2, w // 2)

            return node

        res = dfs(0, 0, len(grid))
        return res

    def reference(self, grid: List[List[int]]) -> 'Node':
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.construct(case).__dict__)
                else:
                    self.construct(case)
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
        [[0, 1], [1, 0]],
        [
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
        ],
    ]
    test.quantify(test_cases)
