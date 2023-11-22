'''
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.
'''
from collections import deque
from time import time


class Solution:
    def minKnightMoves(
        self, n: int, start_x: int, start_y: int, end_x: int, end_y: int
    ) -> int:
        moves = [
            [2, 1],
            [1, 2],
            [-2, 1],
            [-1, 2],
            [2, -1],
            [1, -2],
            [-2, -1],
            [-1, -2],
        ]

        queue = [(start_x, start_y, 0)]
        visited = set()
        visited.add((start_x, start_y))

        while queue:
            x, y, dist = queue[0]
            queue.pop(0)

            if x == end_x and y == end_y:
                return dist

            for dx, dy in moves:
                r = x + dx
                c = y + dy

                if (0 <= r <= n and 0 <= c <= n) and (r, c) not in visited:
                    # If in bounds and not visited
                    visited.add((r, c))
                    queue.append((r, c, dist + 1))

    def reference(
        self, n: int, start_x: int, start_y: int, end_x: int, end_y: int
    ) -> int:
        # Define the possible moves a knight can make
        moves = [
            (2, 1),
            (1, 2),
            (-2, 1),
            (-1, 2),
            (2, -1),
            (1, -2),
            (-2, -1),
            (-1, -2),
        ]

        # Use absolute values for the coordinates to make it work for any quadrant
        start_x, start_y, end_x, end_y = (
            abs(start_x),
            abs(start_y),
            abs(end_x),
            abs(end_y),
        )

        # Create a set to keep track of visited squares
        visited = set()

        # Initialize a queue for BFS
        queue = deque([(0, 0, 0)])

        while queue:
            x, y, steps = queue.popleft()
            if x == end_x and y == end_y:
                return steps  # We've reached the target square

            for dx, dy in moves:
                new_x, new_y = x + dx, y + dy
                # Check if the new square is within the first quadrant
                if (
                    0 <= new_x <= n
                    and 0 <= new_y <= n
                    and (new_x, new_y) not in visited
                ):
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y, steps + 1))

        return (
            -1
        )  # This line should not be reached, as the answer is guaranteed to exist

    def quantify(self, test_cases, runs=10000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.minKnightMoves(*case))
                else:
                    self.minKnightMoves(*case)
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
    test_cases = [(10, 0, 0, 2, 1), (10, 0, 0, 5, 5)]
    test.quantify(test_cases)
