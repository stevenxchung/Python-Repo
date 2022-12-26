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
    def test(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Use hashmap to store mapping
        node_map = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            node_map[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = node_map[curr]
            copy.next = node_map[curr.next]
            copy.random = node_map[curr.random]
            curr = curr.next

        return node_map[head]

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
    input1_1 = Node(7)
    input1_2 = Node(13)
    input1_3 = Node(11)
    input1_4 = Node(10)
    input1_5 = Node(1, None)
    input1_1.next = input1_2
    input1_2.next = input1_3
    input1_3.next = input1_4
    input1_4.next = input1_5
    input1_1.random = None
    input1_2.random = input1_1
    input1_3.random = input1_5
    input1_4.random = input1_3
    input1_5.random = input1_1

    input2_1 = Node(1)
    input2_2 = Node(2, None)
    input2_1.next = input2_2
    input2_1.random = input2_2
    input2_2.random = input2_2

    input3_1 = Node(3)
    input3_2 = Node(3)
    input3_3 = Node(3, None)
    input3_1.next = input3_2
    input3_2.next = input3_3
    input3_1.random = None
    input3_2.random = input3_1
    input3_3.random = None

    test_cases = [input1_1, input2_1, input3_1]
    test.quantify(test_cases)
