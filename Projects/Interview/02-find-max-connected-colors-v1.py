'''
Given a N x N grid, find the maximum number of connected colors.

Can you solve the problem iteratively?
Can you solve the problem recursively?
'''


class Solution:
    def __init__(self):
        self.currentMax = 0
        self.trueMax = 0

    def maxConnect(self, grid):
        #  Check for initial edge case
        if grid == [] or grid == None:
            return None

    def runDFS(self, grid, i, j):

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '#':
            return


inputGrid = [
    ['r', 'g', 'b'],
    ['r', 'r', 'r'],
    ['b', 'g', 'r']
]
sol = Solution()
print(sol.maxConnect(inputGrid))
