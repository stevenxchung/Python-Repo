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
import heapq
from math import inf


class InMemoryDB:
    def __init__(self, debug=False):
        self.debug = debug
        # { key: { field: (value, created_at_ts, t_expire) } }
        self.store = defaultdict(dict)
        # { created_at_ts: { (key, field): (value, t_expire) } }
        self.ts_store = defaultdict(dict)
        # Insert and retrieve values in log(n) time
        # [ (t_expire, created_at_ts, key, field) ]
        self.ttl_heap = []

    def set(self, timestamp: int, key: str, field: str, value: int):
        self.store[key][field] = (value, timestamp, inf)
        self.ts_store[timestamp][(key, field)] = (value, inf)
        if self.debug:
            print(f'set(t={timestamp}): {self.store}')

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
            if self.debug:
                print(f'put(t={timestamp}): {False}')
            return False

        created_on_ts = self.store[key][field][1]
        self.store[key][field] = (newValue, created_on_ts, inf)
        self.ts_store[created_on_ts][(key, field)] = (newValue, inf)
        if self.debug:
            print(f'put(t={timestamp}): {True}')
        return True

    def delete(
        self, timestamp: int, key: str, field: str, expectedValue: int
    ) -> bool:
        if (
            key not in self.store
            or field not in self.store[key]
            or self.store[key][field][0] != expectedValue
        ):
            if self.debug:
                print(f'delete(t={timestamp}): {False}')
            return False

        created_on_ts = self.store[key][field][1]
        del self.store[key][field]
        del self.ts_store[created_on_ts][(key, field)]
        if self.debug:
            print(f'delete(t={timestamp}): {True}')
        return True

    def get(self, timestamp: int, key: str, field: str) -> str:
        res = ''
        if key not in self.store or field not in self.store[key]:
            if self.debug:
                print(f'get(t={timestamp}): {res}')
            return res

        res = self.store[key][field]
        if self.debug:
            print(
                f'get(t={timestamp}): value={res[0]}, ts={res[1]}, t_expire={res[2]}'
            )
        return str(res)

    def scan(self, timestamp: int, key: str) -> str:
        res = ''
        if key not in self.store:
            if self.debug:
                print(f'scan(t={timestamp}): {res}')
            return ''

        temp = []
        for f, obj in self.store[key].items():
            temp.append(f'{f}({obj[0]})')

        temp.sort()
        res = ', '.join(temp)
        if self.debug:
            print(f'scan(t={timestamp}): {res}')
        return res

    def prefix_scan(self, timestamp: int, key: str, prefix: str):
        res = ''
        if key not in self.store:
            if self.debug:
                print(f'prefix_scan(t={timestamp}): {res}')
            return ''

        temp = []
        for f, obj in self.store[key].items():
            if f.startswith(prefix):
                temp.append(f'{f}({obj[0]})')

        temp.sort()
        res = ', '.join(temp)
        if self.debug:
            print(f'prefix_scan(t={timestamp}): {res}')
        return res

    def _delete_expired_records(self, current_time: int):
        '''
        In a real in-memory DB, this is likely done through a periodic cron job.
        For this exercise, we trigger on each function call where TTL is utilized.
        '''
        while len(self.ttl_heap) > 0 and self.ttl_heap[0][0] <= current_time:
            _, ts, key, field = heapq.heappop(self.ttl_heap)
            del self.store[key][field]
            del self.ts_store[ts][(key, field)]
            if len(self.store[key]) == 0:
                # Delete key entry if no more records
                del self.store[key]
            if len(self.ts_store[ts]) == 0:
                # Delete timestamp entry if no more records
                del self.ts_store[ts]

    def set_w_ttl(
        self, timestamp: int, key: str, field: str, value: int, ttl: int
    ):
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

        if self.debug:
            print(f'set_w_ttl(t={timestamp}): {self.store}')
        return

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
            if self.debug:
                print(f'put_w_ttl(t={timestamp}): {False}')
            return False

        t_expire = timestamp + ttl
        _, created_on_ts, prev_t_expire = self.store[key][field]
        self.store[key][field] = (newValue, created_on_ts, t_expire)
        self.ts_store[created_on_ts][(key, field)] = (newValue, t_expire)

        # Remove previous value from heap before adding to prevent duplicates
        self.ttl_heap.remove((prev_t_expire, created_on_ts, key, field))
        heapq.heapify(self.ttl_heap)
        heapq.heappush(self.ttl_heap, (t_expire, created_on_ts, key, field))

        if self.debug:
            print(f'put_w_ttl(t={timestamp}): {True}')
        return True

    def get_w_ts(self, timestamp: int, time: int) -> str:
        # Run delete job for time-based methods
        self._delete_expired_records(timestamp)
        res = ''
        if time not in self.ts_store:
            if self.debug:
                print(f'get_w_ts(t={timestamp}): {res}')
            return res

        res = [
            f'value={v[0]}, t_expire={v[1]}'
            for v in self.ts_store[time].values()
        ]
        if self.debug:
            print(f'get_w_ts(t={timestamp}): {res}')
        return str(res)


print('Testing Part 1...')
test = InMemoryDB(debug=True)
test.set(0, 'A', 'B', 4)
test.set(1, 'A', 'C', 6)
test.put(2, 'A', 'B', 4, 9)
test.put(3, 'A', 'C', 4, 9)
test.delete(4, 'A', 'C', 6)
test.get(5, 'A', 'C')
test.get(6, 'A', 'B')


print('\nTesting Part 2...')
test = InMemoryDB(debug=True)
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
test = InMemoryDB(debug=True)
test.set_w_ttl(0, 'A', 'B', 4, 2)
test.set_w_ttl(1, 'A', 'C', 6, 4)
test.put_w_ttl(2, 'A', 'B', 4, 9, 1)
test.put_w_ttl(3, 'A', 'C', 4, 9, 1)
test.put_w_ttl(4, 'A', 'C', 6, 9, 1)

print('\nTesting Part 4...')
test = InMemoryDB(debug=True)
test.set_w_ttl(0, 'A', 'B', 4, 4)
test.set_w_ttl(0, 'A', 'C', 6, 4)
test.set_w_ttl(1, 'B', 'B', 4, 5)
test.set_w_ttl(1, 'B', 'C', 6, 5)
test.put_w_ttl(2, 'A', 'B', 4, 9, 8)
test.put_w_ttl(3, 'A', 'C', 4, 9, 8)
test.get_w_ts(4, 0)
test.get_w_ts(5, 1)
test.get_w_ts(6, 0)
test.get_w_ts(7, 1)
test.get_w_ts(8, 0)
test.get_w_ts(9, 1)
test.get_w_ts(10, 0)
