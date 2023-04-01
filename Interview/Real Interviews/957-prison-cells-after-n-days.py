'''
There are 8 prison cells in a row and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.

You are given an integer array cells where cells[i] == 1 if the ith cell is occupied and cells[i] == 0 if the ith cell is vacant, and you are given an integer n.

Return the state of the prison after n days (i.e., n such changes described above).
'''
from time import time
from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        return

    def reference(self, cells: List[int], n: int) -> List[int]:
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """

        def next(state):
            return tuple(
                [
                    1
                    if i > 0
                    and i < len(state) - 1
                    and state[i - 1] == state[i + 1]
                    else 0
                    for i in range(len(state))
                ]
            )

        seen = {}
        state = tuple(cells)
        i = 0
        remaining = 0
        while i < n:
            if state in seen:
                cycle = i - seen[state]
                remaining = (n - i) % cycle
                break
            seen[state] = i
            state = next(state)
            i += 1

        while remaining > 0:
            state = next(state)
            remaining -= 1
        return state

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.prisonAfterNDays(*case))
                else:
                    self.prisonAfterNDays(*case)
        print(f'Runtime for our solution: {time() - sol_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(*case))
                else:
                    self.reference(*case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        ([0, 1, 0, 1, 1, 0, 0, 1], 7),
        ([1, 0, 0, 1, 0, 0, 1, 0], 1000000000),
    ]
    test.quantify(test_cases)
