'''
Reverse a string using recursion

Follow up: implement iteratively
'''


class Solution:
    def reverseStringRecursive(self, s):
        if s == '':
            return s
        # print(s[0])
        return self.reverseStringRecursive(s[1:]) + s[0]

    def reverseStringIterative(self, s):
        newS = ''
        for c in s:
            newS = c + newS
        return newS


input = 'Reverse'
sol = Solution()
print(sol.reverseStringRecursive(input))
print(sol.reverseStringIterative(input))
