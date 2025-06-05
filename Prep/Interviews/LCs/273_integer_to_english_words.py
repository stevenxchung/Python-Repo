'''
Convert a non-negative integer num to its English words representation.
'''

from time import time


class Solution:
    def __init__(self):

        self.ones = [
            '',
            ' One',
            ' Two',
            ' Three',
            ' Four',
            ' Five',
            ' Six',
            ' Seven',
            ' Eight',
            ' Nine',
            ' Ten',
            ' Eleven',
            ' Twelve',
            ' Thirteen',
            ' Fourteen',
            ' Fifteen',
            ' Sixteen',
            ' Seventeen',
            ' Eighteen',
            ' Nineteen',
        ]
        self.tens = [
            '',
            ' Ten',
            ' Twenty',
            ' Thirty',
            ' Forty',
            ' Fifty',
            ' Sixty',
            ' Seventy',
            ' Eighty',
            ' Ninety',
        ]
        self.thousands = ['', ' Thousand', ' Million', ' Billion']

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        def dfs(n):
            if n < 20:
                return self.ones[n]
            elif n < 100:
                return self.tens[n // 10] + dfs(n % 10)
            elif n < 1000:
                return dfs(n // 100) + ' Hundred' + dfs(n % 100)
            else:
                for i in range(3, 0, -1):
                    if n >= 1000**i:
                        return (
                            dfs(n // (1000**i))
                            + self.thousands[i]
                            + dfs(n % (1000**i))
                        )

            return ''

        return dfs(num).lstrip()

    def reference(self, num: int) -> str:
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.numberToWords(case))
                else:
                    self.numberToWords(case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

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
    test_cases = [123, 12345, 1234567]
    test.quantify(test_cases)
