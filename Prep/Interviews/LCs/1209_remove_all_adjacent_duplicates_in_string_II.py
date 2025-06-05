'''
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.
'''

from time import time


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''
        - Track [char, count] in a stack
        - Increment count if the next character is a duplicate
        - Pop from the top of the stack whenever count == k
        - Reconstruct string from stack
        '''
        stack = []
        for c in s:
            if len(stack) > 0:
                if stack[-1][0] == c:
                    stack[-1][-1] += 1
                else:
                    stack.append([c, 1])

                if stack[-1][-1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])

        res = ''
        for c, count in stack:
            for _ in range(count):
                res += c

        return res

    def reference(self, s: str, k: int) -> str:
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.removeDuplicates(*case))
                else:
                    self.removeDuplicates(*case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(*case))
                else:
                    self.reference(*case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        ("abcd", 2),
        ("deeedbbcccbdaa", 3),
        ("pbbcggttciiippooaais", 2),
    ]
    test.quantify(test_cases)
