'''
Original: https://leetcode.com/problems/odd-string-difference/description/

Given a series of strings, find the string where the distances between each neighboring character in the string is different from the rest of the strings.
'''

from collections import Counter
from time import time
from typing import List


class Solution:
    def find_odd_one(self, series: List[str]) -> str:
        count_map, res = Counter(), {}
        for s in series:
            char_dist = []
            for i in range(1, len(s)):
                char_dist.append(ord(s[i]) - ord(s[i - 1]))

            # Increment counter if necessary and add word to result map
            count_map[str(char_dist)] += 1
            res[str(char_dist)] = s

        # The key with the minimum count is the odd one
        odd_one = res[min(count_map, key=count_map.get)]

        return odd_one

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.find_odd_one(case))
                else:
                    self.find_odd_one(case)
        print(f'Runtime for our solution: {time() - sol_start}\n')


if __name__ == '__main__':
    test = Solution()
    test_cases = [['ABC', 'DEF', 'GHI', 'QWE']]
    test.quantify(test_cases)
