'''
A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.

- For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.leetcode.com was visited 9001 times.

Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain in the input. You may return the answer in any order.
'''

from collections import defaultdict
from time import time
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        '''
        - Split each input at whitespace
        - Start with whole domain and add to count map
        - Reduce domain to next '.' each time and add to count map
        '''
        count_map = defaultdict(int)

        for cpd in cpdomains:
            count_as_str, domain = cpd.split(' ')
            count = int(count_as_str)
            count_map[domain] += count
            i_periods = [i for i, c in enumerate(domain) if c == '.']
            for idx in i_periods:
                count_map[domain[idx + 1 :]] += count

        return [f'{v} {k}' for k, v in count_map.items()]

    def reference(self, cpdomains: List[str]) -> List[str]:
        count_map = defaultdict(int)
        for s in cpdomains:
            count, s = s.split()
            count = int(count)
            count_map[s] += count
            pos = s.find('.') + 1
            while pos > 0:
                count_map[s[pos:]] += count
                pos = s.find('.', pos) + 1

        return [f'{i} {x}' for x, i in count_map.items()]

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.subdomainVisits(case))
                else:
                    self.subdomainVisits(case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(case))
                else:
                    self.reference(case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        ["9001 discuss.leetcode.com"],
        [
            "900 google.mail.com",
            "50 yahoo.com",
            "1 intel.mail.com",
            "5 wiki.org",
        ],
    ]
    test.quantify(test_cases)
