'''
Share
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''


class Solution:
    def countIslands(self, grid):
        if len(grid) == 0:
            return 0

        islands = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1:
                    # Run DFS and set all 1's adjacent to each other to 0
                    # Then increment islands
                    self.runDFS(grid, i, j)
                    islands += 1

        return islands

    def runDFS(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != 1:
            return

        grid[i][j] = 0
        self.runDFS(grid, i + 1, j)
        self.runDFS(grid, i - 1, j)
        self.runDFS(grid, i, j + 1)
        self.runDFS(grid, i, j - 1)


input = [
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 1, 1],
]
sol = Solution()
print(sol.countIslands(input))
