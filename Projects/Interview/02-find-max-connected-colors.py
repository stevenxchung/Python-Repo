'''
Given a N x N grid, find the maximum number of connected colors.

Can you solve the problem iteratively?
Can you solve the problem recursively?
'''


class Solution:
    def __init__(self, colorStore):
        self.colorStore = {}
        maxCount = 0
        currentCount = 0

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
                    if currentCount > maxCount:
                        maxCount = currentCount

    def runDFS(self, grid, i, j, currentColor):
        currentCount = 0

        isOutOfBounds = (i < 0 or i >= len(
            grid) or j < 0 or j <= len(grid[i]))
        if isOutOfBounds or grid[i][j] != currentColor:
            return

            # if currentColor in self.colorStore:
            #   self.colorStore[currentColor] = 1
            # else:
            #   self.colorStore[currentColor] += 1

            currentCount += 1

            grid[i][j] = "#"
            runDFS(grid, i + 1, j, currentColor)
            runDFS(grid, i - 1, j, currentColor)
            runDFS(grid, i, j + 1, currentColor)
            runDFS(grid, i, j - 1, currentColor)


inputGrid = [
    ['r', 'g', 'b'],
    ['r', 'r', 'r'],
    ['g', 'g', 'r']
]
sol = Solution()
# print(sol.maxConnect(inputGrid))
