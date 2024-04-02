from time import time
from typing import List


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

    def __tuple__(self):
        return (self.key, self.value)


class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        states = []
        for r in range(len(pairs)):
            l = r - 1
            while l >= 0 and pairs[l].key > pairs[l + 1].key:
                pairs[l], pairs[l + 1] = pairs[l + 1], pairs[l]
                l -= 1
            states.append(pairs[:])

        return states

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    res = []
                    for state in self.insertionSort(case):
                        res.append([pair.__tuple__() for pair in state])
                    print(res)
                else:
                    self.insertionSort(case)
        print(f'Runtime for our solution: {time() - sol_start}\n')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        [Pair(5, 'apple'), Pair(2, 'banana'), Pair(9, 'cherry')],
        [Pair(3, 'cat'), Pair(3, 'bird'), Pair(2, 'dog')],
    ]
    test.quantify(test_cases)
