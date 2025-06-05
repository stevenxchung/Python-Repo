'''
Find the top K active users from AWS service log.

Log sample:
ID | Activity
0001 | service A, service B, service C
0002 | service A, service C
0001 | service C
0003 | service A

Top two users would yield user 0001 with 4 service calls and user 0002 with 2 service calls.
'''

from time import time
from typing import Dict, List


class Solution:
    def topKUsers(self, log: List[Dict], k: int) -> List[str]:
        users = {}
        for obj in log:
            user_id = list(obj.keys())[0]
            n_service_calls = len(list(obj.values())[0])
            if user_id not in users:
                users[user_id] = n_service_calls
            else:
                users[user_id] += n_service_calls

        top_n_users = []
        while k > 0:
            max_key = max(users, key=len)
            top_n_users.append(max_key)
            del users[max_key]
            k -= 1

        return top_n_users

    def topKUsersOld(self, log: List[Dict], k: int) -> List[str]:
        # Track user and service requests
        user_activity = {}
        for log_line in log:
            user = list(log_line.keys())[0]
            requests = len(list(log_line.values())[0])
            if user not in user_activity:
                user_activity[user] = requests
            else:
                user_activity[user] += requests

        # Retrieve top k users
        topUsers = []
        while k > 0:
            topUsers.append(max(user_activity, key=len))
            maxKey = max(user_activity, key=len)
            del user_activity[maxKey]
            k -= 1

        return topUsers

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.topKUsers(case[0], case[1]))
                else:
                    self.topKUsers(case[0], case[1])
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.topKUsersOld(case[0], case[1]))
                else:
                    self.topKUsersOld(case[0], case[1])
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    input_log = [
        {'0001': ['A', 'B', 'C']},
        {'0002': ['A', 'C']},
        {'0001': ['C']},
        {'0003': ['A']},
    ]
    test = Solution()
    test_cases = [
        (input_log, 2),
    ]
    test.quantify(test_cases)
