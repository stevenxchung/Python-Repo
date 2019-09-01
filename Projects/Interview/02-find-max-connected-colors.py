'''
Given a N x N grid, find the maximum number of connected colors.

Can you solve the problem iteratively?
Can you solve the problem recursively?
'''


class Solution:
    def __init__(self):
        self.colorStore = {}

    def maxConnect(self, grid):
        currentColor = ''
        if grid == []:
            return None
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                # If cell has not been visited
                if grid[i][j] != "#":
                    currentColor = grid[i][j]
                    self.runDFS(grid, i, j, currentColor)

        return max(self.colorStore.values())

    def runDFS(self, grid, i, j, currentColor):

        if i < 0 or i >= len(
                grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != currentColor:
            return

        if currentColor not in self.colorStore:
          self.colorStore[currentColor] = 1
        else:
          self.colorStore[currentColor] += 1

        grid[i][j] = "#"

        self.runDFS(grid, i + 1, j, currentColor)
        self.runDFS(grid, i - 1, j, currentColor)
        self.runDFS(grid, i, j + 1, currentColor)
        self.runDFS(grid, i, j - 1, currentColor)


inputGrid = [
    ['r', 'g', 'b'],
    ['r', 'r', 'r'],
    ['g', 'g', 'r']
]
sol = Solution()
print(sol.maxConnect(inputGrid))
