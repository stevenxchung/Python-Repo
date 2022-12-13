from collections import defaultdict
import heapq
from math import inf
from time import time
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class Solution:
    def __init__(self, debug=False):
        self.stack = [] # (val, min_val)
        self.min = inf
        self.debug = debug


    def push(self, val: int) -> None:
        if val < self.min:
            self.min = val
        self.stack.append((val, self.min))

        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        res = self.stack[-1][0]
        if self.debug:
            print(res)
        return res
        

    def getMin(self) -> int:
        res = self.stack[-1][-1]
        if self.debug:
            print(res)
        return res


if __name__ == '__main__':
    test = Solution(debug=True)
    sol_start = time()
    test.push(-2)
    test.push(0)
    test.push(-3)
    test.getMin()  # return -3
    test.pop()
    test.top()    # return 0
    test.getMin()  # return -2
    print(f'Runtime for our solution: {time() - sol_start}')
