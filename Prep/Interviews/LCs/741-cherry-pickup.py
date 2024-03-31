'''
You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.

- 0 means the cell is empty, so you can pass through,
- 1 means the cell contains a cherry that you can pick up and pass through, or
- -1 means the cell contains a thorn that blocks your way.

Return the maximum number of cherries you can collect by following the rules below:

- Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
- After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
- When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
- If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.
'''
from copy import deepcopy
from math import inf
from time import time
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        '''
        - Given grid is N x N so rows and columns are the same
        - DFS starting from (0, 0) and moving to (n - 1, n - 1)
        - Can only move down or right from (0, 0)
        - Instead of moving up or left from (n - 1, n - 1), simulate two DFS walks starting from (r1, c1) = (0, 0) and (r2, c2) = (0, 0) w/ total of four options and compute max for all options
        '''
        N = len(grid)
        cache = {}

        def dfs(grid, N, r1, c1, r2, c2):
            if r1 >= N or c1 >= N or r2 >= N or c2 >= N:
                # Out of bounds
                return -inf
            if (r1, c1, r2, c2) in cache:
                # Return the cached result
                return cache[(r1, c1, r2, c2)]

            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                # Blocked by thorns
                return -inf
            elif r1 == r2 and c1 == c2:
                # Prevent duplicate if sample spot
                max_cherries = grid[r2][c2]
            else:
                # Pick up cherries on both paths
                max_cherries = grid[r1][c1] + grid[r2][c2]

            # Goal reached, grab whatever is available
            if r1 == N - 1 and c1 == N - 1:
                return grid[r1][c1]
            if r2 == N - 1 and c2 == N - 1:
                return grid[r2][c2]

            max_cherries += max(
                [
                    # Can both go down
                    dfs(grid, N, r1 + 1, c1, r2 + 1, c2),
                    # Can both go right
                    dfs(grid, N, r1, c1 + 1, r2, c2 + 1),
                    # Can split (down and right)
                    dfs(grid, N, r1 + 1, c1, r2, c2 + 1),
                    # Can split (right and down)
                    dfs(grid, N, r1, c1 + 1, r2 + 1, c2),
                ]
            )

            # Cache the cherries picked up each time
            cache[(r1, c1, r2, c2)] = max_cherries
            return max_cherries

        # Run DFS with memoization
        dfs(grid, N, 0, 0, 0, 0)
        if len(cache) == 0 or cache[(0, 0, 0, 0)] < 0:
            # Return if cache is empty or blocked by thorns
            return 0

        return cache[(0, 0, 0, 0)]

    def reference(self, grid: List[List[int]]) -> int:
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                # Create deep copy
                copy = deepcopy(case)
                if i == 0:
                    print(self.cherryPickup(copy))
                else:
                    self.cherryPickup(copy)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                # Create deep copy
                copy = deepcopy(case)
                if i == 0:
                    print(self.reference(copy))
                else:
                    self.reference(copy)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        [[0, 1, -1], [1, 0, -1], [1, 1, 1]],
        [[1, 1, -1], [1, -1, 1], [-1, 1, 1]],
    ]
    test.quantify(test_cases)
