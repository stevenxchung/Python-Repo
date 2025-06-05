'''
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.
'''

from time import time
from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        '''
        - Loop in reverse and track max height
        - Add to result if current height > max height
        - Update max height and return results in order
        '''
        res = []
        h_max = 0

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > h_max:
                h_max = heights[i]
                res.append(i)

        res.sort()
        return res

    def reference(self, heights: List[int]) -> List[int]:
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.findBuildings(case))
                else:
                    self.findBuildings(case)
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
    test_cases = [[4, 2, 3, 1], [4, 3, 2, 1], [1, 3, 2, 4], [2, 2, 2, 2]]
    test.quantify(test_cases)
