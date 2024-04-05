from time import time
from typing import List


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

    def __tuple__(self):
        return (self.key, self.value)


class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        def quick_sort_helper(arr, l, r):
            if l > r:
                return

            # Use right-most element as pivot
            pivot = arr[r]
            L = l
            for i in range(l, r):
                # Swap if less than pivot
                if arr[i].key < pivot.key:
                    arr[L], arr[i] = arr[i], arr[L]
                    L += 1

            # Move pivot to sorted position
            arr[r], arr[L] = arr[L], arr[r]

            quick_sort_helper(arr, l, L - 1)
            quick_sort_helper(arr, L + 1, r)

            return

        quick_sort_helper(pairs, 0, len(pairs) - 1)
        return pairs

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print([pair.__tuple__() for pair in self.quickSort(case)])
                else:
                    self.quickSort(case)
        print(f'Runtime for our solution: {time() - sol_start}\n')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        [Pair(3, 'cat'), Pair(2, 'dog'), Pair(3, 'bird')],
        [
            Pair(5, 'apple'),
            Pair(9, 'banana'),
            Pair(9, 'cherry'),
            Pair(1, "date"),
            Pair(9, "elderberry"),
        ],
    ]
    test.quantify(test_cases)
