'''
You are given two strings s and t of equal length n. You can perform the following operation on the string s:

- Remove a suffix of s of length l where 0 < l < n and append it at the start of s.
For example, let s = 'abcd' then in one operation you can remove the suffix 'cd' and append it in front of s making s = 'cdab'.

You are also given an integer k. Return the number of ways in which s can be transformed into t in exactly k operations.

Since the answer can be large, return it modulo 109 + 7.
'''
from time import time
from typing import List

MOD = 10**9 + 7
P = 31
PMOD = 496822652529863993


class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        '''
        - DP, how many ways to sum up k integers in [1, n) that add up to i modulo n?
        - Find which rotations of s result in t
        - Find how many ways k integers in [1, n) can add up to some i modulo n
        '''
        n = len(s)

        s_hash = 0
        for c in s:
            s_hash *= P
            s_hash += ord(c) - ord('a')
            s_hash %= PMOD

        t_hash = 0
        for c in t:
            t_hash *= P
            t_hash += ord(c) - ord('a')
            t_hash %= PMOD

        # Rabin-Karp
        res = 0
        largest_power = pow(P, n - 1, PMOD)
        fk1 = (pow((n - 1), k, MOD) - (-1) ** k) * pow(n, -1, MOD)  # f(k, 1)
        for i, c in enumerate(t):
            # Cyclic substring found
            if s_hash == t_hash:
                res += fk1 if i != 0 else fk1 + (-1) ** k
                res %= MOD

            # Shift t
            int_c = ord(c) - ord('a')
            t_hash -= largest_power * int_c
            t_hash = (t_hash % PMOD + PMOD) % PMOD

            t_hash *= P
            t_hash += int_c
            t_hash %= PMOD

        return res

    def add(self, x: int, y: int) -> int:
        x += y
        if x >= MOD:
            x -= MOD
        return x

    def mul(self, x: int, y: int) -> int:
        return int(x * y % MOD)

    def getZ(self, s: str) -> List[int]:
        n = len(s)
        z = [0] * n
        left = right = 0
        for i in range(1, n):
            if i <= right and z[i - left] <= right - i:
                z[i] = z[i - left]
            else:
                z_i = max(0, right - i + 1)
                while i + z_i < n and s[i + z_i] == s[z_i]:
                    z_i += 1
                z[i] = z_i
            if i + z[i] - 1 > right:
                left = i
                right = i + z[i] - 1
        return z

    def matrixMultiply(
        self, a: List[List[int]], b: List[List[int]]
    ) -> List[List[int]]:
        m = len(a)
        n = len(a[0])
        p = len(b[0])
        r = [[0] * p for _ in range(m)]
        for i in range(m):
            for j in range(p):
                for k in range(n):
                    r[i][j] = self.add(r[i][j], self.mul(a[i][k], b[k][j]))
        return r

    def matrixPower(self, a: List[List[int]], y: int) -> List[List[int]]:
        n = len(a)
        r = [[0] * n for _ in range(n)]
        for i in range(n):
            r[i][i] = 1
        x = [a[i][:] for i in range(n)]
        while y > 0:
            if y & 1:
                r = self.matrixMultiply(r, x)
            x = self.matrixMultiply(x, x)
            y >>= 1
        return r

    def reference(self, s: str, t: str, k: int) -> int:
        # Reference: https://leetcode.com/problems/string-transformation/solutions/4024648/solutions-with-c-java-and-python/
        n = len(s)
        dp = self.matrixPower([[0, 1], [n - 1, n - 2]], k)[0]
        s += t + t
        z = self.getZ(s)
        m = n + n
        result = 0
        for i in range(n, m):
            if z[i] >= n:
                result = self.add(result, dp[0] if i - n == 0 else dp[1])
        return result

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.numberOfWays(*case))
                else:
                    self.numberOfWays(*case)
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
    test_cases = [('abcd', 'cdab', 2), ('ababab', 'ababab', 1)]
    test.quantify(test_cases)
