# Leet 957

# If neighbors on both sides are opposite value then flip
# Assume neighbors on ends are inactive (0)


class Solution:
    def cellCompete(self, states, days):


states = [1, 0, 0, 0, 0, 1, 0, 0]
days = 1
sol = Solution()
print(sol.cellCompete(states, days))
