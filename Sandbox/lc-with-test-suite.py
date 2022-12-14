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
    def test(self, n: int) -> List[str]:
        res = []

        def dfs(l, r, substr):
            if r == 0:
                # Closed parenthesis all used up
                res.append(substr)
                return
            elif l == 0:
                # Add a closed parentheses
                dfs(l, r - 1, substr + ')')
            elif l == r:
                # Add an open parentheses
                dfs(l - 1, r, substr + '(')
            else:
                # Otherwise add both parentheses
                dfs(l - 1, r, substr + '(')
                dfs(l, r - 1, substr + ')')

            return

        dfs(n, n, '')
        return res

    def reference():
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.test(case))
                else:
                    self.test(case)
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
    test_cases = [3, 1]
    test.quantify(test_cases)
