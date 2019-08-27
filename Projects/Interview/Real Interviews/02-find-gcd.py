# Write an algorithm to determine the GCD of N positive integers


class Solution:
    def findGCD(self, n, arr):
        # Assume sorted
        gcd = arr[0]
        for i, num in enumerate(arr):
            # If an element has remainder, return 1
            if num % gcd != 0:
                return 1
        # Otherwise, the first element is the GCD
        return gcd


# n = 5
# arr = [2, 3, 4, 5, 6]
n = 5
arr = [2, 4, 6, 8, 10]
sol = Solution()
print(sol.findGCD(n, arr))
