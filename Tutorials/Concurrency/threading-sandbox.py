import threading
import time


class Solution:
    def __init__(self, debug=False) -> None:
        self.debug = debug

    def count(self, limit):
        for i in range(1, limit + 1):
            if self.debug:
                print(i)
            time.sleep(0.01)

    def test(self, n) -> str:
        for _ in range(n):
            x = threading.Thread(target=self.count, args=(n,))
            x.start()
        # Wait for thread to finish processing
        x.join()
        return 'Done'

    def reference(self, n) -> str:
        self.count(n)
        return 'Done'

    def quantify(self, test_cases, runs=1):
        sol_start = time.time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.test(case))
                else:
                    self.test(case)
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
    test_cases = [10]
    test.quantify(test_cases)
