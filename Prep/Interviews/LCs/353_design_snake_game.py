'''
Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

You are given a list of food’s positions in row-column order. When a snake eats the food, its length and the game’s score both increase by 1.

Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.

When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.
'''
from collections import deque
import heapq
from time import time
from typing import List


class Solution:
    def snakeGame(
        self, width: int, height: int, food: List[List[int]]
    ) -> List[int]:
        '''
        - Setup grid w/ snake at upper left corner
        - Food locations can be a queue
        - BFS w/ heap to find food, exit if all food is eaten
        - Heap can be Manhattan distance to food
        - Track current length of the snake until game ends (-1)
        '''
        ROWS, COLS = height, width
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Load food as a queue
        q_food = deque(food)
        rf, cf = q_food.popleft()
        # Starting at top left
        heap = [(rf + cf, 0, 0)]

        len_snake = 0
        res = []
        while len_snake != len(food):
            _, r1, c1 = heapq.heappop(heap)
            if (r1, c1) == (rf, cf):
                # Snake eats food
                len_snake += 1
                res.append(len_snake)
                if q_food:
                    # Queue could be empty but last food not eaten yet
                    rf, cf = q_food.popleft()
            elif (r1, c1) != (0, 0):
                # Snake continues with same length
                # Do not count starting point
                res.append(len_snake)

            for dr, dc in moves:
                r2, c2 = r1 + dr, c1 + dc
                w2 = abs(rf - r2) + abs(cf - c2)
                if r2 < 0 or c2 < 0 or r2 >= ROWS or c2 >= COLS:
                    continue
                heapq.heappush(heap, (w2, r2, c2))

        # Add -1 once food runs out
        res.append(-1)
        return res

    def reference(
        self, width: int, height: int, food: List[List[int]]
    ) -> List[int]:
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.snakeGame(*case))
                else:
                    self.snakeGame(*case)
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
    test_cases = [(3, 2, [[1, 2], [0, 1]])]
    test.quantify(test_cases)
