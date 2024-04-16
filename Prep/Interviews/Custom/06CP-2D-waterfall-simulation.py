'''
Print n iterations of a 2D waterfall simulation. Some constraints include:
- Lowercase letters are particles of water
- ' ' are empty spaces
- Any other character is an obstacle
- Water moves downward but randomly left or right if obstacle (if possible)
- Particles may only move one space during an iteration
'''

import json
import random
from time import time
from typing import List


class Solution:
    def waterfall_simulation(self, arr: List[str], n: int) -> List[str]:
        ROWS, COLS = len(arr), len(arr[0])

        def random_move_x(i: int, j: int):
            j_next = j + random.choice([1, -1])
            if 0 <= j_next < COLS and arr[i][j_next] == ' ':
                arr[i][j], arr[i][j_next] = arr[i][j_next], arr[i][j]
                return j_next

            # Random choice didn't work
            if 0 <= j + 1 < COLS and arr[i][j + 1] == ' ':
                j_next = j + 1
            elif 0 <= j - 1 < COLS and arr[i][j - 1] == ' ':
                j_next = j - 1
            else:
                j_next = j

            arr[i][j], arr[i][j_next] = arr[i][j_next], arr[i][j]
            return j_next

        def one_iteration():
            particle_move = set()
            for i in range(ROWS - 1, -1, -1):
                for j in range(COLS - 1, -1, -1):
                    if (i, j) in particle_move:
                        continue
                    if arr[i][j] == ' ' and (arr[i - 1][j]).isalpha():
                        arr[i][j], arr[i - 1][j] = arr[i - 1][j], arr[i][j]
                        particle_move.add((i, j))
                    elif arr[i][j] != ' ' and (arr[i - 1][j]).isalpha():
                        j_next = random_move_x(i - 1, j)
                        particle_move.add((i, j_next))
            return arr

        def preprocess_input(input_arr: List[str]):
            arr = []
            for s in input_arr:
                temp_arr = list(s)
                arr.append(temp_arr)
            return arr

        res = []
        arr = preprocess_input(arr)
        # Render output for n iterations
        for _ in range(n):
            res.append([''.join(s_list) for s_list in one_iteration()])

        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(
                        json.dumps(self.waterfall_simulation(*case), indent=2)
                    )
                else:
                    self.waterfall_simulation(*case)
        print(f'Runtime for our solution: {time() - sol_start}\n')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        (
            [
                '| a b c d |',
                '| --  -   |',
                '|   = ==  |',
                '|         |',
                '___________',
            ],
            6,
        )
    ]
    test.quantify(test_cases)
