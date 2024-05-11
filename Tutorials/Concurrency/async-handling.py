import asyncio
from decimal import Decimal
import random
import time


class Solution:
    def __init__(self, t_sleep=0.1, debug=False) -> None:
        self.debug = debug
        self.t_sleep = t_sleep
        self.res = []

    async def fetch_data(self, n: int):
        if self.debug:
            print('Fetching...')
        await asyncio.sleep(self.t_sleep)
        if self.debug:
            print('Done fetching!')

        return random.choice([{f'data {n}': f'test {n}'}, [], [Decimal('999')]])

    async def test(self, n: int) -> str:
        # Calls but gathers aggregated results from coroutine
        tasks = [self.fetch_data(i) for i in range(n)]
        self.res = await asyncio.gather(*tasks)

        if self.debug:
            print(self.res)

        return 'Done'

    def reference(self, n: int):
        for i in range(n):
            if self.debug:
                print(i)
            time.sleep(self.t_sleep)

    def quantify(self, test_cases, runs=1):
        sol_start = time.time()
        for i in range(runs):
            for case in test_cases:
                res = asyncio.run(self.test(case))
                if i == 0:
                    print(res)
                else:
                    res
        print(f'Runtime for our solution: {time.time() - sol_start}')

        ref_start = time.time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(case))
                else:
                    self.reference(case)
        print(f'Runtime for reference: {time.time() - ref_start}')


if __name__ == '__main__':
    test = Solution(debug=False)
    test_cases = [10, 9, 8, 7, 6]
    test.quantify(test_cases)
