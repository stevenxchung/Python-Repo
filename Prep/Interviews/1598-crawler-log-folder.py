'''
The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

- "../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
- "./" : Remain in the same folder.
- "x/" : Move to the child folder named x (This folder is guaranteed to always exist).

You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.
'''
from time import time
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        '''
        - Loop through and track folder depth
        '''
        depth = 0
        for action in logs:
            if action == '../':
                depth -= 1
            elif action == './':
                continue
            else:
                depth += 1

        return depth if depth > 0 else 0

    def reference(self, logs: List[str]) -> int:
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.minOperations(case))
                else:
                    self.minOperations(case)
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
        ["d1/", "d2/", "../", "d21/", "./"],
        ["d1/", "d2/", "./", "d3/", "../", "d31/"],
        ["d1/", "../", "../", "../"],
    ]
    test.quantify(test_cases)
