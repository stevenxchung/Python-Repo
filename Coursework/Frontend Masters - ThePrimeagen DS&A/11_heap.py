import heapq
from collections import defaultdict
from math import inf
from time import time
from typing import List


class MinHeap:
    def __init__(self, heap=[], debug=False):
        self.heap = heap
        self.debug = debug

    def add_to_top(self, val: int):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def peek(self) -> int:
        res = self.heap[0] if self.heap else None
        if self.debug:
            print(f'Minimum: {res}')
        return res

    def pop_min(self) -> int:
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop(0)

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, i: int):
        # Starts from bottom when element is added to heap
        parent = (i - 1) // 2

        if i > 0 and self.heap[i] < self.heap[parent]:
            # Smaller element found, swap and recurse
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self._heapify_up(parent)

        return

    def _heapify_down(self, i: int):
        # Starts from top when top of heap is popped
        l = 2 * i + 1
        r = 2 * i + 2
        min_i = i

        if l < len(self.heap) and self.heap[l] < self.heap[min_i]:
            min_i = l
        if r < len(self.heap) and self.heap[r] < self.heap[min_i]:
            min_i = r

        if min_i != i:
            # New min found, swap and recurse
            self.heap[min_i], self.heap[i] = self.heap[i], self.heap[min_i]
            self._heapify_down(min_i)

        return


if __name__ == '__main__':
    test = MinHeap(debug=True)
    sol_start = time()
    test.add_to_top(1)
    test.add_to_top(3)
    test.add_to_top(2)
    test.add_to_top(5)
    test.add_to_top(4)
    test.add_to_top(6)
    test.peek()
    test.pop_min()
    test.peek()
    test.pop_min()
    test.peek()
    test.pop_min()
    test.peek()
    test.pop_min()
    test.peek()
    test.pop_min()
    test.peek()
    test.pop_min()
    test.peek()
    print(f'Runtime for our solution: {time() - sol_start}\n')
