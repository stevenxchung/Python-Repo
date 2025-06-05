'''
A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.

Given the array reservedSeats containing the numbers of seats already reserved, for example, reservedSeats[i] = [3,8] means the seat located in row 3 and labelled with 8 is already reserved.

Return the maximum number of four-person groups you can assign on the cinema seats. A four-person group occupies four adjacent seats in one single row. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be adjacent, but there is an exceptional case on which an aisle split a four-person group, in that case, the aisle split a four-person group in the middle, which means to have two people on each side.
'''

from time import time
from typing import List


class Solution:
    def maxNumberOfFamilies(
        self, n: int, reservedSeats: List[List[int]]
    ) -> int:
        '''
        - Each row can have one or two allocations
        - If seats 2-5 and/or 6-9 not reserved, then add 2 or 1
        - If 4-7 not reserved, then add 1
        - Otherwise, no four-person group is allocated
        '''
        row_map = {n + 1: set() for n in range(n)}
        for r, c in reservedSeats:
            row_map[r].add(c)

        left = {2, 3, 4, 5}
        right = {6, 7, 8, 9}
        mid = {4, 5, 6, 7}

        res = 0
        for r in range(1, n + 1):
            if not (row_map[r] & left) and not (row_map[r] & right):
                res += 2
            elif not (row_map[r] & left) or not (row_map[r] & right):
                res += 1
            elif not (row_map[r] & mid):
                res += 1

        return res

    def reference(self, n: int, reservedSeats: List[List[int]]) -> int:
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.maxNumberOfFamilies(*case))
                else:
                    self.maxNumberOfFamilies(*case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

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
        (3, [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]),
        (2, [[2, 1], [1, 8], [2, 6]]),
        (4, [[4, 3], [1, 4], [4, 6], [1, 7]]),
    ]
    test.quantify(test_cases)
