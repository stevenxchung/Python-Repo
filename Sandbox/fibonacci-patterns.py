# From https://youtu.be/B0NtAFf4bvU?t=811
from time import time


class Solution:
    def fib(self, n):
        if n < 3:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    def fib_top_down_dp(self, n, memo={}):
        if n in memo:
            return memo[n]
        if n < 3:
            return 1
        else:
            res = self.fib_top_down_dp(n - 1) + self.fib_top_down_dp(n - 2)
            memo[n] = res
            return res

    def fib_bottom_up_dp(self, n):
        if n < 3:
            return 1
        res = [0] * (n + 1)
        res[1], res[2] = 1, 1
        for i in range(3, n + 1):
            res[i] = res[i - 1] + res[i - 2]
        return res[n]

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.fib(case))
                else:
                    self.fib(case)
        print(f'Runtime for our solution: {time() - sol_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.fib_top_down_dp(case))
                else:
                    self.fib_top_down_dp(case)
        print(f'Runtime for reference: {time() - ref_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.fib_bottom_up_dp(case))
                else:
                    self.fib_bottom_up_dp(case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [n for n in range(1, 9)]
    test.quantify(test_cases)
