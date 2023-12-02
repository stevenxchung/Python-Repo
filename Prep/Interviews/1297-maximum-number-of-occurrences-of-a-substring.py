'''
Given a string s, return the maximum number of occurrences of any substring under the following rules:

- The number of unique characters in the substring must be less than or equal to maxLetters.
- The substring size must be between minSize and maxSize inclusive.
'''
from collections import defaultdict
from time import time
from typing import List


class Solution:
    def maxFreq(
        self, s: str, maxLetters: int, minSize: int, maxSize: int
    ) -> int:
        '''
        - Variable sliding window based on constraints
        - Hashmap of 0-26 unicode key and frequency
        '''
        freq_map = defaultdict(int)
        for size in range(minSize, maxSize + 1):
            l = 0
            for r in range(size - 1, len(s)):
                arr = [0] * 26
                unique_chars = set()
                substr = s[l : r + 1]
                for c in substr:
                    unique_chars.add(c)
                    arr[ord(c) - ord('a')] += 1

                if len(unique_chars) > maxLetters:
                    # Characters must be unique up to maxLetters
                    continue

                # Generate unicode key
                k = "".join(map(str, arr))
                freq_map[k] += 1
                # Slide window right
                l += 1

        res = max(freq_map.values())
        return res

    def reference(
        self, s: str, maxLetters: int, minSize: int, maxSize: int
    ) -> int:
        return

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
