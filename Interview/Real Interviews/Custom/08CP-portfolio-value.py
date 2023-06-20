'''
Write a function that determines the daily portfolio value across M stocks given an input:
- List of M stocks (rows) N prices over time (columns)
- Not all stocks have a price change on each day
'''
from time import time
from typing import List, Tuple


class Solution:
    def portfolio_values(
        self, daily_prices: List[List[Tuple[str, int]]]
    ) -> List[Tuple[str, int]]:
        dates = set()
        for stock_row in daily_prices:
            for date, _ in stock_row:
                if date not in dates:
                    dates.add(date)
        dates = sorted(dates)

        res = []
        # To track position for each stock
        pos = {i: 0 for i in range(len(daily_prices))}  # {row: column}
        for date in dates:
            port_val = 0
            for i, stock_row in enumerate(daily_prices):
                if pos[i] >= len(stock_row):
                    # End of row already, carry last stock price over
                    port_val += stock_row[pos[i] - 1][-1]
                    continue

                stock_date, price = stock_row[pos[i]][0], stock_row[pos[i]][-1]
                if stock_date == date:
                    port_val += price
                    pos[i] += 1
                elif stock_date > date and pos[i] > 0:
                    # If prices did not change, carry last stock price over
                    port_val += stock_row[pos[i] - 1][-1]

            # Add daily portfolio value
            res.append((date, port_val))

        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.portfolio_values(case))
                else:
                    self.portfolio_values(case)
        print(f'Runtime for our solution: {time() - sol_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        [
            [('5/1', 100), ('5/5', 200)],
            [('5/5', 50), ('5/8', 100)],
            [('5/1', 200), ('5/8', 100)],
        ]
    ]
    test.quantify(test_cases)
