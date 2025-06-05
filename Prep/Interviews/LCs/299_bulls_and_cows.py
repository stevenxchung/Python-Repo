'''
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

- The number of "bulls", which are digits in the guess that are in the correct position.
- The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.

Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.
'''

from collections import Counter
from time import time


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        '''
        - Count map {digit: count} to track count of digits
        - When there is a match on index bulls += 1
        - When digit present in secret but not in correct location cows += 1
        '''
        bulls, cows = 0, 0
        count_map_s = Counter(secret)

        for i, c in enumerate(secret):
            if secret[i] == guess[i]:
                bulls += 1
                count_map_s[c] -= 1

        for i, c in enumerate(guess):
            if (
                guess[i] in count_map_s
                and c != secret[i]  # not in correct position
                and count_map_s[c] > 0  # digit still exists
            ):
                cows += 1
                count_map_s[c] -= 1

        return f'{bulls}A{cows}B'

    def reference(self, secret: str, guess: str) -> str:
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.getHint(*case))
                else:
                    self.getHint(*case)
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
    test_cases = [('1807', '7810'), ('1123', '0111')]
    test.quantify(test_cases)
