'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

- For examples, if arr = [2,3,4], the median is 3.
- For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.

You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10^-5 of the actual value will be accepted.
'''
from bisect import bisect_left, insort
from time import time
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        l = 0
        for r in range(l + k, len(nums) + 1):
            window = sorted(nums[l:r])
            if k % 2 != 0:
                # Not even, take the median
                res.append(window[len(window) % 2])
            else:
                # Even, take the mean
                mean = (
                    window[(len(window) % 2) - 1]
                    + window[(len(window) % 2) + 1]
                ) / sum(window)
                res.append(mean)
            l += 1

        return res

    def reference(self, nums: List[int], k: int) -> List[float]:
        res = []
        window = sorted(nums[:k])

        def find_median(nums: List[int], k: int) -> float:
            if k & 1:
                return nums[k // 2]
            else:
                return (nums[k // 2] + nums[k // 2 - 1]) / 2

        # Get initial median value
        res.append(find_median(window, k))
        # Start at i = 1 and loop until we are k from the end
        for i in range(1, len(nums) - k + 1):
            # Move window to the right
            window.pop(bisect_left(window, nums[i - 1]))
            insort(window, nums[i + k - 1])
            res.append(find_median(window, k))

        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.medianSlidingWindow(*case))
                else:
                    self.medianSlidingWindow(*case)
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
        ([1, 3, -1, -3, 5, 3, 6, 7], 3),
        ([1, 2, 3, 4, 2, 3, 1, 4, 2], 3),
    ]
    test.quantify(test_cases)
