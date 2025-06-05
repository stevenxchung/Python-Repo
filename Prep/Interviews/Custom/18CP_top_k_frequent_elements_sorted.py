"""
Original: https://leetcode.com/problems/top-k-frequent-elements/description/

Given an integer array nums and an integer k, return the k most frequent elements sorted from most to least frequent.
"""

from collections import Counter

from time import time
from typing import List


class Solution:
    def test(self, words: List[str], k: int) -> List[str]:
        count_map = Counter(words)

        # i (freq) -> 0, 1, 2, ...
        # Bucket -> [[], [], [], ...]
        max_freq = max(count_map.values())
        buckets = [[] for _ in range(max_freq + 1)]
        for word, count in count_map.items():
            buckets[count].append(word)

        for i in range(len(buckets)):
            if len(buckets[i]) > 0:
                buckets[i].sort()

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for j in range(len(buckets[i])):
                if len(res) == k:
                    return res
                res.append(buckets[i][j])

        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.test(*case))
                else:
                    self.test(*case)
        print(f"Runtime for our solution: {time() - sol_start}\n")


if __name__ == "__main__":
    test = Solution()

    test_cases = [
        (["i", "love", "kubernetes", "i", "love", "coding"], 2),
        (
            [
                "the",
                "day",
                "is",
                "sunny",
                "the",
                "the",
                "the",
                "sunny",
                "is",
                "is",
            ],
            4,
        ),
    ]
    test.quantify(test_cases)
