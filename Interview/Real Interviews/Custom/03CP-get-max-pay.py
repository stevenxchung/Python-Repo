'''
Given a set of intervals, find the max possible earnings.
'''
from math import inf
from time import time
from typing import List


class Solution:
    def get_max_pay(
        self,
        start_time: int,
        end_time: int,
        d_starts: List[int],
        d_ends: List[int],
        earnings: List[int],
    ) -> int:
        d_tuple = [
            (d_starts[i], d_ends[i], earnings[i]) for i in range(len(d_starts))
        ]
        d_tuple.sort()
        last = -inf
        last_max = 0
        max_pay = 0
        for i in range(len(d_tuple)):
            start, end, pay = d_tuple[i][0], d_tuple[i][1], d_tuple[i][2]
            if start < start_time or end > end_time:
                continue
            if start >= last:
                max_pay += pay
            else:
                # Reset on new interval
                last_max = max_pay
                max_pay = pay
            last = end

        if max_pay > 0:
            return max(max_pay, last_max)

        return -1

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.get_max_pay(*case))
                else:
                    self.get_max_pay(*case)
        print(f'Runtime for our solution: {time() - sol_start}')


if __name__ == '__main__':
    # Answer should be 6
    start_time, end_time = 0, 10
    d_starts = [2, 3, 4, 5, 7]
    d_ends = [6, 4, 6, 10, 11]
    earnings = [5, 2, 4, 1, 3]
    test = Solution()
    test_cases = [(start_time, end_time, d_starts, d_ends, earnings)]
    test.quantify(test_cases)
