'''
Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
'''
import copy
from math import inf
from time import time
from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        total_costs = copy.deepcopy(grid)

        # Find location of people
        people_location = []
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    people_location.append((i, j))

        def get_dist(x1, y1):
            # Determine total distance to all locations
            total_dist = 0
            for x2, y2 in people_location:
                total_dist += abs(x1 - x2) + abs(y1 - y2)
            return total_dist

        # Compute total costs for every point to all locations
        for i in range(ROWS):
            for j in range(COLS):
                total_costs[i][j] = get_dist(i, j)

        # Find the best meeting point or point with min cost
        res, min_cost = None, inf
        for i in range(ROWS):
            for j in range(COLS):
                if total_costs[i][j] < min_cost:
                    res = (i, j)
                    min_cost = total_costs[i][j]

        return res, min_cost

    def reference(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        row_counts, col_counts = [0] * ROWS, [0] * COLS
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    row_counts[i] += 1
                    col_counts[j] += 1

        def get_dist(arr_counts):
            i, j = 0, len(arr_counts) - 1
            dist = 0
            while i < j:
                k = min(arr_counts[i], arr_counts[j])
                dist += k * (j - i)
                arr_counts[i] -= k
                arr_counts[j] -= k
                if arr_counts[i] == 0:
                    i += 1
                if arr_counts[j] == 0:
                    j -= 1

            return dist

        return get_dist(row_counts) + get_dist(col_counts)

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.minTotalDistance(case))
                else:
                    self.minTotalDistance(case)
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
    test = Solution()
    test_cases = [[[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]], [[1, 1]]]
    test.quantify(test_cases)
