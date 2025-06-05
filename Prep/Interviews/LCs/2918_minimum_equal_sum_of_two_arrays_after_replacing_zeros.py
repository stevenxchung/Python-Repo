'''
You are given two arrays nums1 and nums2 consisting of positive integers.

You have to replace all the 0's in both arrays with strictly positive integers such that the sum of elements of both arrays becomes equal.

Return the minimum equal sum you can obtain, or -1 if it is impossible.
'''

from time import time
from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        - Total up sums and zeros
        - Return if sums equal or if an increase is possible
        - Otherwise return -1 if either side has no zeros
        '''
        sum1, sum2 = 0, 0
        z1_count, z2_count = 0, 0

        for n1 in nums1:
            if n1 == 0:
                sum1 += 1
                z1_count += 1
            else:
                sum1 += n1

        for n2 in nums2:
            if n2 == 0:
                sum2 += 1
                z2_count += 1
            else:
                sum2 += n2

        if sum1 == sum2:
            return sum1
        elif sum1 > sum2:
            if z2_count == 0:
                # Not possible to increase sum2
                return -1
            # We may increase sum2 zeros to equal sum1
            return sum1

        if z1_count == 0:
            # Not possible to increase sum1
            return -1
        # We may increase sum1 zeros to equal sum2
        return sum2

    def reference(self, nums1: List[int], nums2: List[int]) -> int:
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.minSum(*case))
                else:
                    self.minSum(*case)
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
    test_cases = [([3, 2, 0, 1, 0], [6, 5, 0]), ([2, 0, 2, 0], [1, 4])]
    test.quantify(test_cases)
