from math import inf
from time import time
from typing import List


class MinHeap:
    def __init__(self, debug=False):
        self.debug = debug
        self.heap = [-inf]

    def _heapify_up(self, i: int, arr: List[int]):
        i = len(arr) - 1
        p = i // 2
        while arr[i] < arr[p]:
            arr[i], arr[p] = arr[p], arr[i]
            i = p
            p = i // 2

    def _heapify_down(self, i: int, arr: List[int]):
        c = 2 * i
        while c < len(arr):
            if c + 1 < len(arr) and arr[c] > arr[c + 1]:
                # No changes, move to next element
                c += 1
            if arr[i] <= arr[c]:
                # Min heap property satisfied, break
                break
            arr[c], arr[i] = arr[i], arr[c]
            i = c
            c = 2 * i

    def push(self, val: int) -> None:
        '''
        Add new value to the heap.
        '''
        self.heap.append(val)
        # Heapify up until heap property is restored
        i = len(self.heap) - 1
        self._heapify_up(i, self.heap)

    def pop(self) -> int:
        '''
        Will remove and return the smallest element in the heap.
        If the heap is empty, return -1.
        '''
        if len(self.heap) == 1:
            if self.debug:
                print(f'pop(): {-1}')
            return -1

        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        res = self.heap.pop()

        # Heapify down until heap property is restored
        self._heapify_down(1, self.heap)

        if self.debug:
            print(f'pop(): {res}')
        return res

    def top(self) -> int:
        '''
        Will return the smallest element in the heap without removing it.
        If the heap is empty, return -1.
        '''
        res = self.heap[1] if len(self.heap) > 1 else -1
        if self.debug:
            print(f'top(): {res}')
        return res

    def heapify(self, nums: List[int]) -> None:
        '''
        Will build a minimum heap from nums.
        '''
        if len(nums) <= 1:
            return

        # Swap first element to last
        nums.append(nums[0])
        nums[0] = -inf

        # Find the middle
        m = (len(nums) - 1) // 2
        for i in range(m, 0, -1):
            # Heapify down until property is restored
            self._heapify_down(i, nums)

        self.heap = nums


if __name__ == '__main__':
    sol_start = time()
    print('##### Test 1 #####')
    test = MinHeap(debug=True)
    test.top()
    test.push(1)
    test.top()
    test.pop()
    test.pop()

    print('\n##### Test 2 #####')
    test = MinHeap(debug=True)
    test.heapify([1, 2, 3, 4, 5])
    test.pop()
    test.pop()
    test.pop()
    test.pop()
    test.pop()

    print('\nAdditional testing...')
    test = MinHeap(debug=True)
    test.heapify([])
    test.pop()

    print(f'Runtime for our solution: {time() - sol_start}\n')
