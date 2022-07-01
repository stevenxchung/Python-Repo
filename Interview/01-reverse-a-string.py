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

    # def reverseStringIterative(self, s):
    #     newS = ''
    #     for c in s:
    #         newS = c + newS
    #     return newS

    # def reverseStringIterative(self, s):
    #     newStr = ''
    #     stack = list(s)
    #     while len(stack):
    #         lastItem = stack.pop()
    #         newStr += lastItem[-1]
    #     return newStr

    def reverseStringIterative(self, string):
        answer = ''
        stack = [string]
        while len(stack):
            item = stack.pop()
            answer += item[-1]

            nextItem = item[:-1]
            if len(nextItem):
                stack.append(nextItem)
        return answer


input = 'Reverse'
sol = Solution()
# print(sol.reverseStringRecursive(input))
print(sol.reverseStringIterative(input))
