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


inputGrid = [
    ['r', 'g', 'b'],
    ['r', 'r', 'r'],
    ['g', 'g', 'r']
]
sol = Solution()
# print(sol.maxConnect(inputGrid))
