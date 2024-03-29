'''
Given an array of random numbers use merge sort to sort array from least to greatest.
'''


class Solution:
    def mergeSort(self, arr):
        print('Splitting', arr)
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            self.mergeSort(L)
            self.mergeSort(R)

            # Initialize indices
            i = j = k = 0

            # Check left and right arrays
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # Check for leftover variables
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

        print('Merging:', arr)
        return arr


# Test merge sort
test = [5, 9, 0, 7, 3]
sol = Solution()
print('Final:', sol.mergeSort(test))
