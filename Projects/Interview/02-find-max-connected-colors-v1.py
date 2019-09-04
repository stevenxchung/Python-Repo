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
        currentColor = ''
        #  Check for initial edge case
        if grid == [] or grid == None:
            return None

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                # Check if grid has been visited
                if grid[i][j] != '#':
                    currentColor = grid[i][j]
                    self.recursiveDFS(grid, i, j, currentColor)

                self.trueMax = max(self.trueMax, self.currentMax)
                self.currentMax = 0

        return self.trueMax

    def runDFS(self, grid, i, j, currentColor):

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != currentColor:
            return

        # Increment max
        self.currentMax += 1
        # Mark cell as visited
        grid[i][j] = '#'

        self.runDFS(grid, i + 1, j, currentColor)
        self.runDFS(grid, i - 1, j, currentColor)
        self.runDFS(grid, i, j + 1, currentColor)
        self.runDFS(grid, i, j - 1, currentColor)

    def recursiveDFS(self, grid, i, j, currentColor):
        outOfBounds = (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]))
        iStack = []
        jStack = []
        iStack.append(i)
        jStack.append(j)

        while len(iStack) > 0 and len(jStack) > 0:

            if outOfBounds or grid[i][j] != currentColor:
                return

            self.currentMax += 1
            grid[i][j] = '#'

            while True:
                i += 1
                iStack.append(i)
                if outOfBounds or grid[i][j] != currentColor:
                    iStack.pop()
                    i = iStack[len(iStack) - 1]
                    break
                self.currentMax += 1
                grid[i][j] = '#'
            while True:
                i -= 1
                iStack.append(i)
                if outOfBounds or grid[i][j] != currentColor:
                    iStack.pop()
                    i = iStack[len(iStack) - 1]
                    break
                self.currentMax += 1
                grid[i][j] = '#'
            while True:
                j += 1
                jStack.append(j)
                if outOfBounds or grid[i][j] != currentColor:
                    jStack.pop()
                    j = jStack[len(jStack) - 1]
                    break
                self.currentMax += 1
                grid[i][j] = '#'
            while True:
                j -= 1
                jStack.append(j)
                if outOfBounds or grid[i][j] != currentColor:
                    jStack.pop()
                    j = jStack[len(jStack) - 1]
                    break
                self.currentMax += 1
                grid[i][j] = '#'


inputGrid = [
    ['g', 'g', 'b'],
    ['r', 'g', 'r'],
    ['b', 'g', 'g']
]
sol = Solution()
print(sol.maxConnect(inputGrid))
