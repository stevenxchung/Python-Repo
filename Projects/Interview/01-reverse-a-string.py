'''
Reverse a string using recursion

Follow up: implement iteratively
'''


class Solution:
    def reverseString(self, s):
        if s == '':
            return s
        print(s[0])
        return self.reverseString(s[1:]) + s[0]


input = 'Reverse'
sol = Solution()
print(sol.reverseString(input))
