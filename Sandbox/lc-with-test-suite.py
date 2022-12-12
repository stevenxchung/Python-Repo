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
    def test(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            return True

        seen = set()
        adj = {k : [] for k in range(n)}
        for a, b, in edges:
            adj[a].append(b)
        
        def dfs(node, prev):
            if node in seen:
                return False
            
            seen.add(node)
            for nei in adj[node]:
                if nei == prev:
                    # Skip false positive loop for neighbor
                    continue
                if not dfs(nei, node):
                    # Cycle detected
                    return False

            return True

        return dfs(0, -1) and len(seen) == n

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
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]]),
        # Additional
        (7, [[0, 1], [0, 2], [3, 5], [5, 6], [1, 4]]),
    ]
    test.quantify(test_cases)
