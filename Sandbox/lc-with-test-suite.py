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
    def test(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(position[i], speed[i]) for i in range(len(position))]
        arr.sort(reverse=True)

        stack = []
        for x, v in arr:
            # Time it takes to get to target given position and speed
            t = (target - x) / v
            if len(stack) == 0 or t > stack[-1]:
                # When stack is empty or car at back is slower than car at front then it will become a new fleet
                stack.append(t)

        return len(stack)

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
        (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]),
        (10, [3], [3]),
        (100, [0, 2, 4], [4, 2, 1]),
    ]
    test.quantify(test_cases)
