import asyncio
import time


class Solution:
    def __init__(self, debug=False) -> None:
        self.debug = debug
        self.res = []

    async def fetch_data(self, n: int):
        if self.debug:
            print('Fetching...')
        await asyncio.sleep(0.5)
        if self.debug:
            print('Done fetching!')

        return {f'data {n}': f'test {n}'}

    async def print_numbers(self, n: int):
        for i in range(n):
            if self.debug:
                print(i)
                await asyncio.sleep(0.5)

    async def test(self, n: int) -> str:
        # Calls and waits one at a time
        # for i in range(n):
        #     data = await self.fetch_data(i)
        #     self.res.append(data)

        # Calls but gathers aggregated results from coroutine
        tasks = [self.fetch_data(i) for i in range(n)]
        self.res = await asyncio.gather(*tasks)

        if self.debug:
            print(self.res)

        return 'Done'

    def reference():
        return

    def quantify(self, test_cases, runs=1):
        sol_start = time.time()
        for i in range(runs):
            for case in test_cases:
                loop = asyncio.run(self.test(case))
                if i == 0:
                    print(loop)
                else:
                    loop
        print(f'Runtime for our solution: {time.time() - sol_start}')

        # ref_start = time.time()
        # for i in range(0, runs):
        #     for case in test_cases:
        #         if i == 0:
        #             print(self.reference(case))
        #         else:
        #             self.reference(case)
        # print(f'Runtime for reference: {time.time() - ref_start}')


if __name__ == '__main__':
    test = Solution(debug=True)
    test_cases = [10, 9, 8, 7, 6]
    test.quantify(test_cases)
