'''
Given a string s, return the maximum number of occurrences of any substring under the following rules:

- The number of unique characters in the substring must be less than or equal to maxLetters.
- The substring size must be between minSize and maxSize inclusive.
'''

from time import time
from typing import Counter


class Solution:
    def maxFreq(
        self, s: str, maxLetters: int, minSize: int, maxSize: int
    ) -> int:
        '''
        - Count map {substr: count} to track max substring occurrences
        - Add to count when substring is <= maxLetters
        '''
        count = Counter()

        for i in range(len(s) - minSize + 1):
            t = s[i : i + minSize]
            if len(set(t)) <= maxLetters:
                count[t] += 1

        return max(count.values()) if count else 0

    def reference(
        self, s: str, maxLetters: int, minSize: int, maxSize: int
    ) -> int:
        count = Counter(s[i : i + minSize] for i in range(len(s) - minSize + 1))
        return max([count[w] for w in count if len(set(w)) <= maxLetters] + [0])

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.maxFreq(*case))
                else:
                    self.maxFreq(*case)
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
        ("aababcaab", 2, 3, 4),
        ("aaaa", 1, 3, 3),
    ]
    test.quantify(test_cases)
