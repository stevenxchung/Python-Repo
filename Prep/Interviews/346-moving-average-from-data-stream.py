'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

- MovingAverage(int size) Initializes the object with the size of the window size.
- double next(int val) Returns the moving average of the last size values of the stream.
'''
from time import time


class MovingAverage:
    def __init__(self, size: int, debug=False):
        self.window_size = size
        self.q = []
        self.debug = debug

    def next(self, val: int) -> float:
        self.q.append(val)
        if len(self.q) > self.window_size:
            self.q.pop(0)

        denominator = len(self.q)
        res = round(sum(self.q) / denominator, 5)
        if self.debug:
            print(res)
        return res


if __name__ == '__main__':
    test = MovingAverage(3, debug=True)  # None
    sol_start = time()
    test.next(1)  # 1.0
    test.next(10)  # 5.5
    test.next(3)  # 4.66667
    test.next(5)  # 6.0
    print(f'Runtime for our solution: {time() - sol_start}\n')
