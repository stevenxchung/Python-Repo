from time import time
from typing import List


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

    def __tuple__(self):
        return (self.key, self.value)


class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def merge_sort_helper(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort_helper(arr[:mid])
            right = merge_sort_helper(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            res = []
            l, r = 0, 0

            # Append to lesser element to new array
            while l < len(left) and r < len(right):
                if left[l].key <= right[r].key:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1

            # Include leftover elements if leftovers
            if l < len(left):
                res.extend(left[l:])
            if r < len(right):
                res.extend(right[r:])

            return res

        return merge_sort_helper(pairs)

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print([pair.__tuple__() for pair in self.mergeSort(case)])
                else:
                    self.mergeSort(case)
        print(f'Runtime for our solution: {time() - sol_start}\n')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        [
            Pair(5, 'apple'),
            Pair(2, 'banana'),
            Pair(9, 'cherry'),
            Pair(1, "date"),
            Pair(9, "elderberry"),
        ],
        [Pair(3, 'cat'), Pair(2, 'dog'), Pair(3, 'bird')],
    ]
    test.quantify(test_cases)
