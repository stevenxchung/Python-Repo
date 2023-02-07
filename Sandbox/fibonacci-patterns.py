# From https://youtu.be/B0NtAFf4bvU?t=811
from time import time


class Solution:
    def __init__(self, debug=False) -> None:
        self.debug = debug

    def fib(self, n):
        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)

    def fib_top_down_dp(self, n, cache={}):
        if n <= 1:
            return n
        if n in cache:
            return cache[n]

        cache[n] = self.fib_top_down_dp(n - 1) + self.fib_top_down_dp(n - 2)
        return cache[n]

    def fib_bottom_up_dp(self, n):
        if n <= 1:
            return n

        # Initialize cache
        cache = [0] * (n + 1)
        cache[1], cache[2] = 1, 1

        # Will not need to loop until n = 3
        for i in range(3, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[n]

    def fib_bottom_up_dp_neetcode(self, n):
        if n < 2:
            return n

        cache = [0, 1]
        i = 2
        while i <= n:
            temp = cache[1]
            cache[1] = cache[0] + cache[1]
            cache[0] = temp
            i += 1

        return cache[1]

    def quantify(self, test_cases, runs=50000):
        # sol_start = time()
        # for i in range(runs):
        #     for case in test_cases:
        #         if i == 0 and self.debug:
        #             print(self.fib(case))
        #         else:
        #             self.fib(case)
        # print(f'Runtime for our solution: {time() - sol_start}')

        # ref_start = time()
        # for i in range(0, runs):
        #     for case in test_cases:
        #         if i == 0 and self.debug:
        #             print(self.fib_top_down_dp(case))
        #         else:
        #             self.fib_top_down_dp(case)
        # print(f'Runtime for reference: {time() - ref_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0 and self.debug:
                    print(self.fib_bottom_up_dp(case))
                else:
                    self.fib_bottom_up_dp(case)
        print(f'Runtime for reference: {time() - ref_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0 and self.debug:
                    print(self.fib_bottom_up_dp_neetcode(case))
                else:
                    self.fib_bottom_up_dp_neetcode(case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution(debug=False)
    test_cases = [n for n in range(20)]
    test.quantify(test_cases)
