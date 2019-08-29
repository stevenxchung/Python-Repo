'''
Convert the Fibonacci function from recursive to iterative
'''


class Solution:
    def fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)


s = Solution()
print(s.fibonacci(10))
