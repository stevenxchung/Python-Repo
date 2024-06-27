'''
Given a JSON string below, parse the keys and values into a dictionary.

input = '{ "hello": "world", "foo": 23.45, "bar": true, "baz": ["bat"] }'

out = parseJson(input)
out['hello'] => 'world'
'''

from collections import defaultdict
from typing import Dict


class Solution:
    def parseJson(self, s: str) -> Dict:
        res = defaultdict()
        curr_k, curr_v = None, None
        l = 0
        while l < len(s):
            if s[l] == " ":
                l += 1
                continue

            r = l + 1
            if s[l] == '"' and curr_k is None:
                # Find key
                while r < len(s) and s[r] != ":":
                    r += 1
                curr_k = s[l + 1 : r - 1]
            elif s[l] == '"' and curr_v is None:
                # Find string value
                while r < len(s) and s[r] != '"':
                    r += 1
                curr_v = s[l + 1 : r]
            elif s[l].isdigit() and curr_v is None:
                # Find float value
                while r < len(s) and s[r] != ',':
                    r += 1
                curr_v = s[l:r]
            elif s[l].isalpha() and curr_v is None:
                # Find boolean value
                while r < len(s) and s[r] != ',':
                    r += 1
                curr_v = s[l:r]
            elif s[l] == '[' and curr_v is None:
                # Find list value
                while r < len(s) and s[r] != ']':
                    r += 1
                curr_v = s[l : r + 1]
            # Set l to next element
            l = r + 1

            # Reset key and value
            if curr_k and curr_v:
                res[curr_k] = curr_v
                curr_k, curr_v = None, None

        print(res)
        return res


input = '{ "hello": "world", "foo": 23.45, "bar": true, "baz": ["bat"] }'
test = Solution()
out = test.parseJson(input)
print(out['hello'])
