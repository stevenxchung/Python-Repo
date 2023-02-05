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

    def iterativeFib(self, n):
        stack = []
        stack.append(n)
        total = 0
        while len(stack) > 0:
            n = stack.pop()
            if n == 0:
                total += 0
            elif n == 1:
                total += 1
            else:
                stack.append(n - 1)
                stack.append(n - 2)
        return total


s = Solution()
# print(s.fibonacci(10))
print(s.iterativeFib(10))
