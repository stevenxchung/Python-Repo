'''
Find the top K active users from AWS service log.

Log sample:
ID | Activity
0001 | service A, service B, service C
0002 | service A, service C
0001 | service C
0003 | service A

Top two users would yield user 0001 with 4 service calls and user 0002 with 2 service calls
'''


class Solution:
    def topKUsers(self, log, k):
        # Track user and service requests
        userActivity = {}
        for logLine in log:
            user = list(logLine.keys())[0]
            requests = len(list(logLine.values())[0])
            if user not in userActivity:
                userActivity[user] = requests
            else:
                userActivity[user] += requests

        # Retreive top k users
        topUsers = []
        while k > 0:
            topUsers.append(max(userActivity, key=len))
            maxKey = max(userActivity, key=len)
            del userActivity[maxKey]
            k -= 1

        return topUsers


inputLog = [
    {'0001': ['A', 'B', 'C']},
    {'0002': ['A', 'C']},
    {'0001': ['C']},
    {'0003': ['A']},
]
k = 2
sol = Solution()
print(sol.topKUsers(inputLog, k))
