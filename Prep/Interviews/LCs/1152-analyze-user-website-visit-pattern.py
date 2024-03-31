'''
You are given two string arrays username and website and an integer array timestamp. All the given arrays are of the same length and the tuple [username[i], website[i], timestamp[i]] indicates that the user username[i] visited the website website[i] at time timestamp[i].

A pattern is a list of three websites (not necessarily distinct).

- For example, ['home', 'away', 'love'], ['leetcode', 'love', 'leetcode'], and ['luffy', 'luffy', 'luffy'] are all patterns.

The score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.

- For example, if the pattern is ['home', 'away', 'love'], the score is the number of users x such that x visited 'home' then visited 'away' and visited 'love' after that.
- Similarly, if the pattern is ['leetcode', 'love', 'leetcode'], the score is the number of users x such that x visited 'leetcode' then visited 'love' and visited 'leetcode' one more time after that.
- Also, if the pattern is ['luffy', 'luffy', 'luffy'], the score is the number of users x such that x visited 'luffy' three different times at different timestamps.

Return the pattern with the largest score. If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.
'''
from collections import defaultdict
import heapq
from itertools import combinations
from time import time
from typing import List


class Solution:
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
        tups = list(zip(timestamp, username, website))
        sorted_tups = sorted(tups)

        user_history = defaultdict(list)
        for _, u, w in sorted_tups:
            user_history[u].append(w)

        pattern_count = defaultdict(int)
        for history in user_history.values():
            # combinations() generates all possible patterns given a list
            combos = set(combinations(history, 3))
            for combo in combos:
                pattern_count[combo] += 1

        # Invert for max heap implementation
        patterns_as_list = list(
            zip([-n for n in pattern_count.values()], pattern_count.keys())
        )
        heapq.heapify(patterns_as_list)

        return heapq.heappop(patterns_as_list)[1]

    def reference(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(*self.mostVisitedPattern(*case))
                else:
                    self.mostVisitedPattern(*case)
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
        (
            [
                'joe',
                'joe',
                'joe',
                'james',
                'james',
                'james',
                'james',
                'mary',
                'mary',
                'mary',
            ],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [
                'home',
                'about',
                'career',
                'home',
                'cart',
                'maps',
                'home',
                'home',
                'about',
                'career',
            ],
        ),  # ['home','about','career']
        (
            ['ua', 'ua', 'ua', 'ub', 'ub', 'ub'],
            [1, 2, 3, 4, 5, 6],
            ['a', 'b', 'a', 'a', 'b', 'c'],
        ),  # ['a','b','a']
    ]
    test.quantify(test_cases)
