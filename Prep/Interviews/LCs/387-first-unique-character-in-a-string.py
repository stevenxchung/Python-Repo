'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''

from collections import Counter
from time import time


class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        - Count map {char: count}
        - Return first occurrence if unique (count == 1)
        '''
        count_map = Counter(s)
        for i, c in enumerate(s):
            if count_map[c] == 1:
                return i

        return -1

    def reference(self, s: str) -> int:
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.firstUniqChar(case))
                else:
                    self.firstUniqChar(case)
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
    test_cases = ['leetcode', 'loveleetcode', 'aabb']
    test.quantify(test_cases)
