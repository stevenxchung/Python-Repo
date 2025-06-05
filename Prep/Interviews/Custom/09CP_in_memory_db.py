'''
Create an InMemoryDB() data structure with the following features:

Part 1 - support basic operations to manipulate records, fields, and values within fields:
- set(timestamp, key, field, value)
- put(timestamp, key, field, expectedValue, newValue)
- delete(timestamp, key, field, expectedValue)
- get(timestamp, key, field)

Part 2 - support displaying a record's fields based on a filter:
- scan(timestamp, key)
- prefix_scan(timestamp, key, prefix)

Part 3: support the TTL(Time-To-Live) settings for records:
- set_w_ttl(timestamp, key, field, value, ttl)
- put_w_ttl(timestamp, key, field, expectedValue, newValue, ttl)

Part 4: support look-back operations to retrieve values stored at a specific timestamp in the past
- get_w_ts(timestamp, key, time)
'''

from collections import defaultdict
from functools import wraps
import heapq
from math import inf


def log_io(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        arg_str = ', '.join(
            [repr(a) for a in args] + [f'{k}={v!r}' for k, v in kwargs.items()]
        )
        print(f'{func.__name__}({arg_str}) -> {result!r}')
        return result

    return wrapper


class InMemoryDB:
    def __init__(self):
        # { key: { field: (value, created_at_ts, t_expire) } }
        self.store = defaultdict(dict)
        # { created_at_ts: { (key, field): (value, t_expire) } }
        self.ts_store = defaultdict(dict)
        # Insert and retrieve values in log(n) time
        # [ (t_expire, created_at_ts, key, field) ]
        self.ttl_heap = []

    @log_io
    def set(self, timestamp: int, key: str, field: str, value: int) -> str:
        self.store[key][field] = (value, timestamp, inf)
        self.ts_store[timestamp][(key, field)] = (value, inf)

        return ''

    @log_io
    def put(
        self,
        timestamp: int,
        key: str,
        field: str,
        expectedValue: int,
        newValue: int,
    ) -> bool:
        if (
            key not in self.store
            or field not in self.store[key]
            or self.store[key][field][0] != expectedValue
        ):
            return False

        created_on_ts = self.store[key][field][1]
        self.store[key][field] = (newValue, created_on_ts, inf)
        self.ts_store[created_on_ts][(key, field)] = (newValue, inf)

        return True

    @log_io
    def delete(
        self, timestamp: int, key: str, field: str, expectedValue: int
    ) -> bool:
        if (
            key not in self.store
            or field not in self.store[key]
            or self.store[key][field][0] != expectedValue
        ):
            return False

        del self.store[key][field]

        return True

    @log_io
    def get(self, timestamp: int, key: str, field: str) -> str:
        res = ''
        if key not in self.store or field not in self.store[key]:
            return res

        res = self.store[key][field]

        return str(res[0])

    @log_io
    def scan(self, timestamp: int, key: str) -> str:
        res = ''
        if key not in self.store:
            return ''

        temp = []
        for f, obj in self.store[key].items():
            temp.append(f'{f}({obj[0]})')

        temp.sort()
        res = ', '.join(temp)

        return res

    @log_io
    def prefix_scan(self, timestamp: int, key: str, prefix: str):
        res = ''
        if key not in self.store:
            return ''

        temp = []
        for f, obj in self.store[key].items():
            if f.startswith(prefix):
                temp.append(f'{f}({obj[0]})')

        temp.sort()
        res = ', '.join(temp)

        return res

    @log_io
    def _delete_expired_records(self, current_time: int):
        '''
        In a real in-memory DB, this is likely done through a periodic cron job.
        For this exercise, we trigger on each function call where TTL is utilized.
        '''
        while len(self.ttl_heap) > 0 and self.ttl_heap[0][0] <= current_time:
            _, _, key, field = heapq.heappop(self.ttl_heap)
            del self.store[key][field]
            if len(self.store[key]) == 0:
                # Delete key entry if no more records
                del self.store[key]

    @log_io
    def set_w_ttl(
        self, timestamp: int, key: str, field: str, value: int, ttl: int
    ) -> str:
        # Run delete job for time-based methods
        self._delete_expired_records(timestamp)

        t_expire = timestamp + ttl

        if key in self.store and field in self.store[key]:
            _, created_on_ts, prev_t_expire = self.store[key][field]
            self.store[key][field] = (value, created_on_ts, t_expire)
            self.ts_store[created_on_ts][(key, field)] = (
                value,
                t_expire,
            )
            # Remove previous value from heap before adding to prevent duplicates
            self.ttl_heap.remove((prev_t_expire, created_on_ts, key, field))
            heapq.heapify(self.ttl_heap)
            heapq.heappush(self.ttl_heap, (t_expire, created_on_ts, key, field))
        else:
            # New record
            self.store[key][field] = (value, timestamp, t_expire)
            self.ts_store[timestamp][(key, field)] = (value, t_expire)
            heapq.heappush(self.ttl_heap, (t_expire, timestamp, key, field))

        return ''

    @log_io
    def put_w_ttl(
        self,
        timestamp: int,
        key: str,
        field: str,
        expectedValue: int,
        newValue: int,
        ttl: int,
    ):
        # Run delete job for time-based methods
        self._delete_expired_records(timestamp)
        if (
            key not in self.store
            or field not in self.store[key]
            or self.store[key][field][0] != expectedValue
        ):
            return False

        t_expire = timestamp + ttl
        _, created_on_ts, prev_t_expire = self.store[key][field]
        self.store[key][field] = (newValue, created_on_ts, t_expire)

        # Remove previous value from heap before adding to prevent duplicates
        self.ttl_heap.remove((prev_t_expire, created_on_ts, key, field))
        heapq.heapify(self.ttl_heap)
        heapq.heappush(self.ttl_heap, (t_expire, created_on_ts, key, field))

        return True

    @log_io
    def get_w_ts(self, timestamp: int, time: int) -> str:
        # Run delete job for time-based methods
        self._delete_expired_records(timestamp)
        res = ''
        if time not in self.ts_store:
            return res

        res = [
            f't={time}, key={k[0]}, field={k[1]}, value={v[0]}, ttl={v[1] - time}'
            for k, v in self.ts_store[time].items()
        ]

        return str(res)


if __name__ == '__main__':
    print('Testing Part 1...')
    test = InMemoryDB()
    test.set(0, 'A', 'B', 4)
    test.set(1, 'A', 'C', 6)
    test.put(2, 'A', 'B', 4, 9)
    test.put(3, 'A', 'C', 4, 9)
    test.delete(4, 'A', 'C', 6)
    test.get(5, 'A', 'C')
    test.get(6, 'A', 'B')

    print('\nTesting Part 2...')
    test = InMemoryDB()
    test.set(0, 'A', 'B', 4)
    test.set(1, 'A', 'C', 6)
    test.scan(2, 'A')
    test.scan(3, 'B')
    test.set(4, 'B', 'bar', 1)
    test.set(5, 'B', 'baz', 2)
    test.set(6, 'B', 'foo', 3)
    test.prefix_scan(7, 'B', 'ba')
    test.prefix_scan(8, 'B', 'f')
    test.prefix_scan(9, 'B', 'a')

    print('\nTesting Part 3...')
    test = InMemoryDB()
    test.set_w_ttl(0, 'A', 'B', 4, 2)
    test.set_w_ttl(1, 'A', 'C', 6, 4)
    test.put_w_ttl(2, 'A', 'B', 4, 9, 1)
    test.put_w_ttl(3, 'A', 'C', 4, 9, 1)
    test.put_w_ttl(4, 'A', 'C', 6, 9, 1)
    test.put_w_ttl(5, 'A', 'C', 6, 9, 1)

    print('\nTesting Part 4...')
    test = InMemoryDB()
    test.set_w_ttl(0, 'A', 'B', 4, 4)
    test.set_w_ttl(1, 'A', 'C', 6, 4)
    test.set_w_ttl(2, 'B', 'B', 4, 5)
    test.set_w_ttl(3, 'B', 'C', 6, 5)
    test.put_w_ttl(4, 'A', 'B', 4, 9, 8)
    test.put_w_ttl(5, 'A', 'C', 4, 9, 8)
    test.get_w_ts(6, 0)
    test.get_w_ts(7, 1)
    test.get_w_ts(8, 2)
    test.get_w_ts(9, 3)
    test.get_w_ts(10, 4)
    test.get_w_ts(11, 5)
    test.get_w_ts(12, 6)
