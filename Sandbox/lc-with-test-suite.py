from collections import Counter, defaultdict, deque
import heapq
from math import inf, sqrt
import queue
from time import time
from typing import List, Optional
import black


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
    def test(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        preq = {i: set() for i in range(numCourses)}
        # Create a graph for adjacency and traversing
        graph = defaultdict(set)
        for i, j in prerequisites:
            preq[i].add(j)
            graph[j].add(i)

        q = deque([])
        # Find starting location based on courses with no prereq
        for k, v in preq.items():
            if len(v) == 0:
                q.append(k)

        taken = []
        while q:
            pre = q.popleft()
            taken.append(pre)
            if len(taken) == numCourses:
                return taken

            for next_course in graph[pre]:
                # Remove prereq from the next course
                preq[next_course].remove(pre)
                # Taken all requirements so add next course to queue
                if not preq[next_course]:
                    q.append(next_course)

        return []

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
        # (2, [[1, 0]]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
        # (1, [])
    ]
    test.quantify(test_cases)
