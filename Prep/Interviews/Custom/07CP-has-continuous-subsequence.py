'''
Write a function that determines whether or not an array contains a subarray with continuous (nums[i] <= nums[i + 1]) subsequence (length == 1 counts if matches target) that sums to the target value.
'''
from time import time
from typing import List


class Solution:
    def has_valid_subsequence(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        l, r, total = 0, 0, nums[0]
        while l < len(nums) and r < len(nums):
            if nums[l] == target or nums[r] == target or total == target:
                # Target can be at either index or match total
                return True

            if r + 1 < len(nums):
                if nums[r + 1] < nums[r] and l < r + 1:
                    # If next number is less than current, move left index
                    total -= nums[l]
                    l += 1
                else:
                    # Move right index if possible
                    r += 1
                    total += nums[r]
            elif l != r:
                # Next right index is out-of-bounds so try moving left index
                total -= nums[l]
                l += 1
            else:
                # No more valid moves left
                break

        return total == target

    def gpt_solution(self, nums: List[int], target: int) -> bool:
        # set up a variable to track the sum of the subarray
        subarray_sum = 0

        # loop through the array and add each element to the subarray sum
        for num in nums:
            subarray_sum += num

            # if the sum is equal to the target, return true
            if subarray_sum == target:
                return True

            # if the sum is greater than the target, reset it to 0 and start over
            elif subarray_sum > target:
                subarray_sum = 0

        # if no increasing subarray sums to the target, return false
        return False

    def reference(self, nums: List[int], target: int) -> bool:
        # set up a variable to track the sum of the subarray
        subarray_sum = 0
        l, r = 0, 0

        # loop through the array and add each element to the subarray sum
        while r < len(nums):
            subarray_sum += nums[r]
            r += 1

            # if the sum is equal to the target, return true
            if subarray_sum == target:
                return True

            # if the sum is greater than the target, reset it to 0 and start over
            while subarray_sum > target:
                subarray_sum -= nums[l]
                l += 1

        # if no increasing subarray sums to the target, return false
        return subarray_sum == target

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.has_valid_subsequence(*case))
                else:
                    self.has_valid_subsequence(*case)
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
        ([1, 2, 2, 4], 4),  # True
        ([1, 2, 2, 1], 4),  # True
        ([1, 2, 3, 2], 4),  # False
        ([1, 1, 1, 4], 4),  # True
        ([2, 1, 1, 0], 4),  # False
        ([3, 2, 1, 4], 4),  # True
        ([0, 0, 0, 0], 4),  # False
        ([0, 1, 3, 1], 4),  # True
        ([1, -1, 2, 2], 4),  # True
        ([], 4),  # False
    ]
    test.quantify(test_cases)
