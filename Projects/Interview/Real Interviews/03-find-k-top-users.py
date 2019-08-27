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


inputLog = [
    {'0001', ['A', 'B', 'C']},
    {'0002', ['A', 'C']},
    {'0001', ['C']},
    {'0003', ['A']},
]
k = 2
sol = Solution()
print(sol.topKUsers(inputLog, k))
