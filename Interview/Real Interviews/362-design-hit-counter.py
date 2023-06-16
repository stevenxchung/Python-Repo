'''
Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

- HitCounter() Initializes the object of the hit counter system.
- void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
- int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
'''
from time import time


class HitCounter:
    def __init__(self, debug=False):
        '''
        1, 2, 3, 300
        get at 4 = 3
        get at 300 = 4
        get at 301 = 3
        '''
        self.debug = debug
        self.stack = []  # (timestamp, hits)
        self.ts_to_hits = {}  # {timestamp: hits}

    def hit(self, timestamp: int) -> None:
        if self.stack and timestamp - self.stack[0][0] < 300:
            # Increment hit if interval is within 300 seconds
            self.stack.insert(0, (timestamp, self.stack[0][-1] + 1))
        else:
            # Otherwise, new hit starting with 1
            self.stack.insert(0, (timestamp, 1))
        # Track hits for easy access
        self.ts_to_hits[timestamp] = self.stack[0][-1]

    def getHits(self, timestamp: int) -> int:
        res = 0
        if timestamp in self.ts_to_hits:
            res = self.ts_to_hits[timestamp]
        else:
            # Count hits up to timestamp within a 300 second interval
            for ts, _ in self.stack[::-1]:
                if timestamp - ts < 300:
                    res += 1
        if self.debug:
            print(f'{res} hits @ timestamp {timestamp}')
        return res


if __name__ == '__main__':
    test = HitCounter(debug=True)
    sol_start = time()
    test.hit(1)  # hit at timestamp 1.
    test.hit(2)  # hit at timestamp 2.
    test.hit(3)  # hit at timestamp 3.
    test.getHits(4)  # get hits at timestamp 4, return 3.
    test.hit(300)  # hit at timestamp 300.
    test.getHits(300)  # get hits at timestamp 300, return 4.
    test.getHits(301)  # get hits at timestamp 301, return 3.
    print(f'Runtime for our solution: {time() - sol_start}\n')
