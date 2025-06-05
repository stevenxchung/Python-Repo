"""
Given a game of tic-tac-toe and known end states, find the total number of possible board configurations (including states in-between start and finish) that could be had.
"""

from time import time
from typing import List


class Solution:
    def test(self, board: List[int]) -> int:
        end_state_indexes = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        moves = []

        def is_end(board, player):
            for state in end_state_indexes:
                if all(board[i] == player for i in state):
                    return True
            return False

        def dfs(board, player):
            if (
                0 not in board
                or is_end(board, player)
                or is_end(board, -player)
            ):
                moves.append(board[:])
                return

            for i in range(len(board)):
                if board[i] == 0:
                    board[i] = player
                    dfs(board, -player)
                    board[i] = 0

        dfs(board, 1)
        return len(moves)

    def quantify(self, test_cases, runs=1):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.test(case))
                else:
                    self.test(case)
        print(f"Runtime for our solution: {time() - sol_start}\n")


if __name__ == "__main__":
    test = Solution()
    test_cases = [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
    test.quantify(test_cases)
