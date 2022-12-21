from collections import Counter, defaultdict, deque
import heapq
from math import inf, sqrt
import queue
from time import time
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors != None else []


class Solution:
    def test(self, tasks: List[str], n: int) -> int:
        counts = list(Counter(tasks).values())
        max_freq = max(counts)
        # Number of times max frequency occurs
        n_max_freq = counts.count(max_freq)
        # Unit of time cannot be less than number of tasks
        return max(len(tasks), (max_freq - 1) * (n + 1) + n_max_freq)

    def reference():
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.test(*case))
                else:
                    self.test(*case)
        print(f'Runtime for our solution: {time() - sol_start}')

        # ref_start = time()
        # for i in range(0, runs):
        #     for case in test_cases:
        #         if i == 0:
        #             print(self.reference(*case))
        #         else:
        #             self.reference(*case)
        # print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        (['A', 'A', 'A', 'B', 'B', 'B'], 2),
        (['A', 'A', 'A', 'B', 'B', 'B'], 0),
        (['A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'], 2),
    ]
    test.quantify(test_cases)
