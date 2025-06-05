'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
'''

from time import time


class Solution:
    def isValid(self, s: str) -> bool:
        '''
        - Use stack to track complement
        - If stack is empty then string is valid, otherwise string is not valid
        '''
        pairs = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in pairs:
                stack.append(c)
                continue
            if not stack or c != pairs[stack[-1]]:
                return False
            stack.pop()

        return len(stack) == 0

    def reference(self, s: str) -> bool:
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.isValid(case))
                else:
                    self.isValid(case)
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
        '()',
        '()[]{}',
        '(]',
        # Additional
        '(()',
        '[()',
        '(])',
    ]
    test.quantify(test_cases)
