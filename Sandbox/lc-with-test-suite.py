from collections import Counter, defaultdict, deque
import copy
import heapq
from math import ceil, inf, sqrt
import re
from time import time
from typing import List, Optional, Tuple


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
        '''Graph node'''
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         '''Special linked-list node'''
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution:
    def test(self, tasks: List[str], n: int) -> int:
        '''
        - Use hashmap to count tasks
        - Use count to represent the task in max-heap
        - Loop and add to time as long as heap or queue is not empty
        - Pop tasks off heap and add to queue with cooldown time
        - Add tasks from queue to heap once cooldown expires
        '''
        freq_map = Counter(tasks)
        heap = [-count for count in freq_map.values()]
        heapq.heapify(heap)

        t = 0
        q = deque()
        while heap or q:
            t += 1
            if not heap:
                # Out of tasks, get latest time from top
                _, t = q[0]
            else:
                # Reduce count for the specific task (max-heap)
                count = heapq.heappop(heap) + 1
                if count != 0:
                    q.append([count, t + n])

            if q and q[0][-1] == t:
                # Add back task to heap once cooldown is over
                heapq.heappush(heap, q.popleft()[0])

        return t

    def reference(self):
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.test(*case))
                else:
                    self.test(*case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

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
