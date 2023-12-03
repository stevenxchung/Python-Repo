'''
In a special ranking system, each voter gives a rank from highest to lowest to all teams participating in the competition.

The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, we consider the second position to resolve the conflict, if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.

You are given an array of strings votes which is the votes of all voters in the ranking systems. Sort all teams according to the ranking system described above.

Return a string of all teams sorted by the ranking system.
'''
from collections import defaultdict
from time import time
from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        '''
        - Use hashmap w/ list to track team and rank values (each position)
        - Loop through votes and add to position for each team
        - Sort team according to rank values
        '''
        rank_map = defaultdict(list)

        for v in votes:
            for i, t in enumerate(v):
                if t not in rank_map:
                    rank_map[t] = [0] * len(v)
                rank_map[t][i] += 1

        res = sorted(rank_map.keys(), key=rank_map.get, reverse=True)

        return "".join(res)

    def reference(self, votes: List[str]) -> str:
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.rankTeams(case))
                else:
                    self.rankTeams(case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(case))
                else:
                    self.reference(case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        ["ABC", "ACB", "ABC", "ACB", "ACB"],
        ["WXYZ", "XYZW"],
        ["ZMNAGUEDSJYLBOPHRQICWFXTVK"],
    ]
    test.quantify(test_cases)
