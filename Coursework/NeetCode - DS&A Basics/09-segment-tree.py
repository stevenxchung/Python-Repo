from time import time
from typing import List


class STNode:
    def __init__(self, total: int, L: int, R: int):
        self.total = total
        self.left, self.right = None, None
        self.L, self.R = L, R

    def update(self, index: int, val: int) -> bool:
        '''
        Find index to update value and recursively update range totals.
        '''
        if self.L == self.R == index:
            # Index found
            self.total = val
            return True
        elif self.L == self.R != index:
            return False

        left, right = None, None
        M = (self.L + self.R) // 2
        if index <= M:
            # Examine left side [L, M]
            left = self.left.update(index, val)
        else:
            # Examine right side [M + 1, R]
            right = self.right.update(index, val)

        self.total = self.left.total + self.right.total

        return left or right

    def rangeQuery(self, L: int, R: int) -> int:
        '''
        Return range totals for a given range.
        '''
        if L == self.L and R == self.R:
            return self.total

        M = (self.L + self.R) // 2
        if R <= M:
            # Select left range [L, M] since <= median
            return self.left.rangeQuery(L, R)
        elif L > M:
            # Select right range [M + 1, R] since > median
            return self.right.rangeQuery(L, R)
        else:
            # Otherwise, range is within bounds
            return self.left.rangeQuery(L, M) + self.right.rangeQuery(M + 1, R)


class SegmentTree:
    def __init__(self, nums: List[int], debug=False):
        self.debug = debug
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums: List[int], L: int, R: int):
        '''
        Recursively build a segment tree from segment tree nodes.
        '''
        if L == R:
            # Return if single element
            return STNode(nums[L], L, R)

        # Split range in half
        M = (L + R) // 2
        node = STNode(0, L, R)
        node.left = self.build(nums, L, M)
        node.right = self.build(nums, M + 1, R)
        node.total = node.left.total + node.right.total
        return node

    def update(self, index: int, val: int) -> None:
        res = self.root.update(index, val)
        if self.debug:
            print(f'update({index}, {val}): {res}')

    def query(self, L: int, R: int) -> int:
        res = self.root.rangeQuery(L, R)
        if self.debug:
            print(f'query({L}, {R}): {res}')
        return res


if __name__ == '__main__':
    sol_start = time()
    print('##### Test 1 #####')
    test = SegmentTree([1, 2, 3, 4, 5], debug=True)
    test.query(0, 2)
    test.query(2, 4)
    test.update(3, 0)
    test.query(2, 4)

    print('\n##### Test 2 #####')
    test = SegmentTree([-1, 2, 4], debug=True)
    test.query(0, 1)
    test.query(1, 2)
    test.update(2, 3)
    test.query(0, 2)

    print('\nAdditional testing...')
    test = SegmentTree([1, 2, 3, 4, 5], debug=True)
    test.query(0, 2)
    test.query(2, 4)
    test.update(5, 0)
    test.query(2, 4)

    print(f'Runtime for our solution: {time() - sol_start}\n')
