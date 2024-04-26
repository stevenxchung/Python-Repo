'''
Create an EnhancedSet() data structure with the following properties:
- No duplicates
- O(1) insertion
- O(1) deletion
- O(1) get random element

For insertion() and deletion(), return a boolean indicating if the operation was successful or not. Each element much have an equal chance of being randomly selected.
'''

from random import randint
from time import time


class Solution:
    def __init__(self, debug=False):
        self.debug = debug
        self.arr = []
        self.v2i_map = {}  # (value, index)

    def insertion(self, s: str) -> bool:
        if s in self.v2i_map:
            if self.debug:
                print(f'insertion({s}): {False}')
            return False
        self.arr.append(s)
        self.v2i_map[s] = len(self.arr) - 1
        if self.debug:
            print(f'insertion({s}): {True}')
        return True

    def deletion(self, s: str) -> bool:
        if s in self.v2i_map:
            i = self.v2i_map[s]
            # Swap for last element
            self.arr[i], self.arr[-1] = self.arr[-1], self.arr[i]
            self.arr.pop()
            del self.v2i_map[s]
            if self.debug:
                print(f'deletion({s}): {True}')
            return True

        if self.debug:
            print(f'deletion({s}): {False}')
        return False

    def get_random_element(self) -> str:
        i = randint(0, len(self.arr) - 1)
        if self.debug:
            print(f'get_random_element(): {self.arr[i]}')
        return self.arr[i]


if __name__ == '__main__':
    test = Solution(debug=True)
    sol_start = time()
    test.insertion('a')
    test.insertion('b')
    test.insertion('c')
    test.insertion('d')
    test.insertion('e')
    test.insertion('a')
    test.insertion('b')
    test.deletion('f')
    test.deletion('g')
    test.deletion('a')
    test.deletion('b')
    test.get_random_element()
    test.get_random_element()
    test.get_random_element()
    test.get_random_element()
    print(f'Runtime for our solution: {time() - sol_start}\n')
