'''
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
'''
from time import time
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = list(words[0])
        for word in words[1:]:
            local = []
            for c in word:
                # Only carry over intersect
                if c in common:
                    local.append(c)
                    common.remove(c)
            common = local

        return common

    def reference(self, words: List[str]) -> List[str]:
        if len(words) < 2:
            return words

        common = set(words[0])  # Make a set from first string
        res = []
        for c in common:
            # Count min frequency of every letter in every word
            n = min([a_word.count(c) for a_word in words])
            if n:
                # If n > 0 , we append this letter n times
                res += [c] * n

        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.commonChars(case))
                else:
                    self.commonChars(case)
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
    test_cases = [['bella', 'label', 'roller'], ['cool', 'lock', 'cook']]
    test.quantify(test_cases)
