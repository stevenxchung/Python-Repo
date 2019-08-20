# Leet 957

# If neighbors on both sides are opposite value then flip
# Assume neighbors on ends are inactive (0)


class Solution:
    def cellCompete(self, states, days):
        flip = {0: 1, 1: 0}
        end = len(states) - 1
        # newStates = []
        for i, state in enumerate(states):
            # Is first element?
            if i == 0 and states[1] == 0:
                states[i] = flip[state]
            # Is last element?
            elif i == end and states[end - 1] == 0:
                states[i] = flip[state]
            # Meets condition?
            elif states[i - 1] == states[i + 1]:
                states[i] = flip[state]

        return states

states = [1, 0, 0, 0, 0, 1, 0, 0]
days = 1
sol = Solution()
print(sol.cellCompete(states, days))
