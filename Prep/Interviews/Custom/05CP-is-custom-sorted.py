'''
Write a function that returns whether a list of strings is sorted given a specific alphabet.

Input:
    words = ['cat', 'bat', 'tab']
    alphabet = ['c', 'b', 'a', 't']

Output: true
'''
from time import time


class Solution:
    def __init__(self, debug=False) -> None:
        self.debug = debug

    def is_custom_sorted(self, words, alphabet):
        if len(words) == 1 or not words:
            return True

        order = {c: i for i, c in enumerate(alphabet)}

        l = 0
        r = l + 1
        # Loop through words
        while r < len(words):
            i = 0
            j = 0
            while i < len(words[l]) and j < len(words[r]):
                if order[words[l][i]] < order[words[r][j]]:
                    # First is less than second, break and go to next pair of words
                    break
                if order[words[l][i]] > order[words[r][j]]:
                    # If first is greater than second character, return False
                    return False
                # Increment string index
                i += 1
                j += 1
            # Increment word index
            l += 1
            r += 1

        return True

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.is_custom_sorted(*case))
                else:
                    self.is_custom_sorted(*case)
        print(f'Runtime for our solution: {time() - sol_start}\n')


if __name__ == '__main__':
    test = Solution(debug=True)
    test_cases = [
        (['cat', 'bat', 'tab'], ['c', 'b', 'a', 't']),
        (['bat', 'cat', 'tab'], ['c', 'b', 'a', 't']),
    ]
    test.quantify(test_cases)
