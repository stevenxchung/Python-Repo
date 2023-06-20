'''
Given a N x N grid, find the maximum number of connected colors. Return the color and the max.

Can you solve the problem iteratively?
Can you solve the problem recursively?
'''


class Solution:
    def __init__(self):
        self.colorStore = {}
        # For comparing last max connected colors
        self.maxStore = {}

    def maxConnect(self, grid):
        currentColor = ''
        #  Check for initial edge case
        if grid == [] or grid == None:
            return None

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                # If cell has not been visited
                if grid[i][j] != "#":
                    # Pass current color along to DFS
                    currentColor = grid[i][j]
                    self.runDFS(grid, i, j, currentColor)

                    if currentColor not in self.maxStore:
                        self.maxStore[currentColor] = self.colorStore[currentColor]
                    else:
                        self.maxStore[currentColor] = max(
                            self.maxStore[currentColor], self.colorStore[currentColor])

                    # Reset color store for next round of connected colors
                    self.colorStore = {}

        for key in self.maxStore:
            if self.maxStore[key] == max(self.maxStore.values()):
                return key, max(self.maxStore.values())

    def runDFS(self, grid, i, j, currentColor):

        if i < 0 or i >= len(
                grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != currentColor:
            return

        if currentColor not in self.colorStore:
            self.colorStore[currentColor] = 1
        else:
            self.colorStore[currentColor] += 1

        # Mark cell as visited
        grid[i][j] = "#"

        # Check adjacent colors
        self.runDFS(grid, i + 1, j, currentColor)
        self.runDFS(grid, i - 1, j, currentColor)
        self.runDFS(grid, i, j + 1, currentColor)
        self.runDFS(grid, i, j - 1, currentColor)


inputGrid = [
    ['g', 'g', 'b'],
    ['r', 'r', 'r'],
    ['r', 'g', 'b']
]
sol = Solution()
print(sol.maxConnect(inputGrid))
