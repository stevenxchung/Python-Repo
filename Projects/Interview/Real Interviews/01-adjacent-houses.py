# Leet 957

# If neighbors on both sides match then inactive (0)
# Otherwise, active (1)
# Assume neighbors on ends are inactive (0)


class Solution:
    def cellCompete(self, states, days):
        end = len(states) - 1
        prev = states
        while days:
          days -= 1
          new = []
          for i, state in enumerate(prev):
              # Is first element?
              if i == 0 and prev[1] == 0:
                  new.append(0)
                  # states[i] = flip[state]
              # Is last element?
              elif i == end and prev[end - 1] == 0:
                  new.append(0)
                  # states[i] = flip[state]
              # Meets condition?
              elif (i != 0 and i != 7) and prev[i - 1] == prev[i + 1]:
                  new.append(0)
                  # states[i] = flip[state]
              else:
                  new.append(1)
          # Store new states as previous for next iteration
          prev = new

        return new

# states = [1, 0, 0, 0, 0, 1, 0, 0]
# days = 1
states = [1, 1, 1, 0, 1, 1, 1, 1]
days = 2
sol = Solution()
print(sol.cellCompete(states, days))
