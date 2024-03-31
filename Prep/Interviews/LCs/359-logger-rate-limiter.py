'''
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.
'''
from collections import defaultdict
from time import time


class Solution:
    def __init__(self, debug=False):
        self.debug = debug
        self.cache = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        '''
        - Use hashmap to track message and time since last seen
        '''
        res = False
        if message not in self.cache or (
            message in self.cache and timestamp - self.cache[message] >= 10
        ):
            self.cache[message] = timestamp
            res = True

        if self.debug:
            print(f'timestamp: {timestamp} | message: {message} | res: {res}')

        return res


if __name__ == '__main__':
    test = Solution(debug=True)
    sol_start = time()
    # logging string "foo" at timestamp 1
    test.shouldPrintMessage(1, "foo")  # returns True
    # logging string "bar" at timestamp 2
    test.shouldPrintMessage(2, "bar")  # returns True
    # logging string "foo" at timestamp 3
    test.shouldPrintMessage(3, "foo")  # returns False
    # logging string "bar" at timestamp 8
    test.shouldPrintMessage(8, "bar")  # returns False
    # logging string "foo" at timestamp 10
    test.shouldPrintMessage(10, "foo")  # returns False
    # logging string "foo" at timestamp 11
    test.shouldPrintMessage(11, "foo")  # returns True
    print(f'Runtime for our solution: {time() - sol_start}\n')
