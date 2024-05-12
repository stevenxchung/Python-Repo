import asyncio
import random
import threading
import time

from concurrent.futures import ThreadPoolExecutor
from decimal import Decimal


class Solution:
    def __init__(self, t_sleep=0.1, debug=False) -> None:
        self.debug = debug
        self.t_sleep = t_sleep
        self.res = []

    def fetch_data(self, n: int):
        if self.debug:
            print('Fetching...')
        # Simulate a synchronous delay
        time.sleep(self.t_sleep)
        if self.debug:
            print('Done fetching!')

        return random.choice([{f'data {n}': f'test {n}'}, [], [Decimal('999')]])

    def print_numbers(self, n: int):
        for i in range(n):
            if self.debug:
                print(i)
            # Simulate a synchronous delay
            time.sleep(self.t_sleep)

    async def to_thread(self, func, *args):
        # Required for threading synchronous functions
        with ThreadPoolExecutor() as pool:
            return await asyncio.get_event_loop().run_in_executor(
                pool, func, *args
            )

    def test(self, n: int) -> str:
        # Calls but gathers aggregated results from coroutine
        # tasks = [self.to_thread(self.fetch_data, i) for i in range(n)]
        # self.res = await asyncio.gather(*tasks)
        threads = []
        for i in range(n):
            thread = threading.Thread(target=self.fetch_data, args=(i,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        if self.debug:
            print(self.res)

        return 'Done'

    def reference(self, case):
        self.print_numbers(case)

    def quantify(self, test_cases, runs=1):
        sol_start = time.time()
        for i in range(runs):
            for case in test_cases:
                res = self.test(case)
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
    # Classic way (Python ~3.6) of handling async fetch
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # loop.run_until_complete(test.quantify(test_cases))
    # loop.close()
    test.quantify(test_cases)