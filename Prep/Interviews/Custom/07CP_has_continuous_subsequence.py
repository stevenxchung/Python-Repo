'''
Determine whether or not an array contains a subarray with continuous increasing subsequence (nums[i] <= nums[i + 1]) that sums to the target value. Note that length == 1 counts if matches target.
'''

from time import time
from typing import List


class Solution:
    def has_valid_subsequence(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n == 0:
            return False

        l = 0  # Left end of window
        r = 0  # Right end of window
        total = nums[0]  # Sum of the window [l, r]

        while l < n and r < n:
            # Check if any endpoint, or the window sum, matches the target
            if nums[l] == target or nums[r] == target or total == target:
                return True

            # Try to grow the window rightward when valid
            if r + 1 < n:
                if nums[r + 1] < nums[r] and l < r + 1:
                    # Next element breaks non-decreasing property, so shrink from left
                    total -= nums[l]
                    l += 1
                else:
                    # Expand to the right, add element to sum
                    r += 1
                    total += nums[r]
            elif l != r:
                # Can't expand right; shrink window from left
                total -= nums[l]
                l += 1
            else:
                # Window can't move further
                break

        return total == target

    def reference(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        for start in range(n):
            current_sum = nums[start]
            if current_sum == target:
                return True

            for end in range(start + 1, n):
                if nums[end] < nums[end - 1]:
                    break  # Not non-decreasing anymore
                current_sum += nums[end]
                if current_sum == target:
                    return True

        return False

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
