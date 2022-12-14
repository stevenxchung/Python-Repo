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
    def test(self, tokens: List[str]) -> int:
        stack = []
        ops = set(['+', '-', '*', '/'])
        for i in range(len(tokens)):
            if tokens[i] in ops:
                a, b = stack.pop(), stack.pop()
                if tokens[i] == '+':
                    stack.append(int(a) + int(b))
                elif tokens[i] == '-':
                    stack.append(int(b) - int(a))
                elif tokens[i] == '*':
                    stack.append(int(a) * int(b))
                else:
                    stack.append(int(b) / int(a))
            else:
                stack.append(tokens[i])

        return stack.pop()

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
    test_cases = [
        ['2', '1', '+', '3', '*'],
        ['4', '13', '5', '/', '+'],
        ['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']
    ]
    test.quantify(test_cases)
