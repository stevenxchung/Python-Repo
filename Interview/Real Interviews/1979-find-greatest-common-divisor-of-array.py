'''
Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
'''
from time import time
from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return

    def reference(self, nums: List[int]) -> int:
        a, b = min(nums), max(nums)
        while a:
            a, b = b % a, a
        return b

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.findGCD(case))
                else:
                    self.findGCD(case)
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
    test_cases = [
        [2, 5, 6, 9, 10],
        [7, 5, 6, 8, 3],
        [3, 3]
    ]
    test.quantify(test_cases)
