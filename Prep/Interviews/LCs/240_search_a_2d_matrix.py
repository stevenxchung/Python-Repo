'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.
'''

from time import time
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        - All right elements greater than current
        - All top element less than current
        - Apply binary search column-wise if target in rage
        '''
        ROWS, COLS = len(matrix), len(matrix[0])

        for R in range(ROWS):
            if matrix[R][0] <= target <= matrix[R][-1]:
                l, r = 0, COLS - 1
                while l <= r:
                    m = (l + r) // 2
                    if matrix[R][m] == target:
                        return True
                    elif matrix[R][m] < target:
                        l = m + 1
                    else:
                        r = m - 1

        return False

    def reference(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        r, c = ROWS - 1, 0
        while r >= 0 and c < COLS:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                r -= 1
            else:
                c += 1

        return False

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.searchMatrix(*case))
                else:
                    self.searchMatrix(*case)
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
        (
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            5,
        ),
        (
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            20,
        ),
    ]
    test.quantify(test_cases)
