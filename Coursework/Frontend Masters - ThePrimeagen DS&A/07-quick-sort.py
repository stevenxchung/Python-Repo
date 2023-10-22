import heapq
import math
import re
from collections import Counter, defaultdict, deque
from copy import deepcopy
from math import ceil, inf, sqrt
from time import time
from typing import Dict, List, Optional, Tuple


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
    def test(self, nums: List[int]) -> List[int]:
        def quicksort(arr, low, high):
            if low < high:
                mid = partition(arr, low, high)
                quicksort(arr, low, mid)
                quicksort(arr, mid + 1, high)

        def partition(arr, low, high):
            pivot = arr[low + (high - low) // 2]
            i = low
            j = high
            while i <= j:
                while arr[i] < pivot:
                    i += 1
                while arr[j] > pivot:
                    j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
            return i - 1

        quicksort(nums, 0, len(nums) - 1)
        return nums

    def reference(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            res = []
            i, j = 0, 0

            # Compare elements from both halves and merge
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1

            # Append remaining elements, if any
            res.extend(left[i:])
            res.extend(right[j:])

            return res

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            # Divide the array into two halves
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            # Recursively sort the two halves
            left_sorted = merge_sort(left)
            right_sorted = merge_sort(right)

            # Merge the sorted halves
            return merge(left_sorted, right_sorted)

        return merge_sort(nums)

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                # Create deep copy
                copy = deepcopy(case)
                if i == 0:
                    print(self.test(copy))
                else:
                    self.test(copy)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                # Create deep copy
                copy = deepcopy(case)
                if i == 0:
                    print(self.reference(copy))
                else:
                    self.reference(copy)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [[9, 3, 7, 4, 69, 420, 42]]
    test.quantify(test_cases)
