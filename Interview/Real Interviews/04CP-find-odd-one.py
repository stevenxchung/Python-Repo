'''
*Custom problem
Given a series of strings, find the string where the distances between each neighboring character in the string is different from the rest of the strings.
'''
from time import time
from typing import List


class Solution:
    def find_odd_one(self, series: List[str]) -> str:
        counts = {}
        dists = {}
        for s in series:
            i, j = 0, 1
            char_dist = []
            while j < len(s):
                char_dist.append(ord(s[i]) - ord(s[j]))
                i += 1
                j += 1

            if str(char_dist) not in counts:
                counts[str(char_dist)] = 1
                dists[str(char_dist)] = s
            else:
                counts[str(char_dist)] += 1

        # The key with the minimum count is the odd one
        odd_one = dists[min(counts, key=counts.get)]

        return odd_one

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.find_odd_one(case))
                else:
                    self.find_odd_one(case)
        print(f'Runtime for our solution: {time() - sol_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [['ABC', 'DEF', 'GHI', 'QWE']]
    test.quantify(test_cases)
