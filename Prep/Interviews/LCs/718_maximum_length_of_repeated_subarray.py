'''
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
'''

from time import time
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        - Initialize 2D N + 1 * M + 1 matrix
        - Use DP to traverse matrix and track longest subarray
        '''
        if not nums1 and not nums2:
            return 0

        # dp[r][c] is the length of longest common subarray ending with nums[r] and nums[c]
        ROWS, COLS = len(nums1) + 1, len(nums2) + 1
        cache = [[0] * (COLS) for _ in range(ROWS)]
        for r in range(ROWS - 2, -1, -1):
            for c in range(COLS - 2, -1, -1):
                if nums1[r] == nums2[c]:
                    cache[r][c] = cache[r + 1][c + 1] + 1
                else:
                    cache[r][c] = max(cache[r + 1][c], cache[r][c + 1])

        return cache[0][0]

    def reference(self, nums1: List[int], nums2: List[int]) -> int:
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.findLength(*case))
                else:
                    self.findLength(*case)
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
        ([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]),
        ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
    ]
    test.quantify(test_cases)
