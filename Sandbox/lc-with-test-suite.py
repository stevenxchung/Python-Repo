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


# class Node:
#     def __init__(self, val=0, neighbors=None):
#         '''Graph Node'''
#         self.val = val
#         self.neighbors = neighbors if neighbors != None else []


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        '''Linked-list Node'''
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def test(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        p1, p2 = l1, l2
        res1, res2 = '', ''
        while p1:
            res1 += f'{p1.val}'
            p1 = p1.next
        while p2:
            res2 += f'{p2.val}'
            p2 = p2.next

        sum_res = [int(n) for n in f'{int(res1) + int(res2)}'][::-1]

        p = ListNode()
        res = p
        for n in sum_res:
            p.next = ListNode(n)
            p = p.next

        return res.next

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
        (
            ListNode(2, ListNode(4, ListNode(3))),
            ListNode(5, ListNode(6, ListNode(4))),
        ),
        (ListNode(0), ListNode(0)),
        (
            ListNode(
                9,
                ListNode(
                    9,
                    ListNode(
                        9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
                    ),
                ),
            ),
            ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
        ),
    ]
    test.quantify(test_cases)
