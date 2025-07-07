"""
There is an undirected graph with n nodes numbered from 0 to n - 1 (inclusive). You are given a 0-indexed integer array values where values[i] is the value of the ith node. You are also given a 0-indexed 2D integer array edges, where each edges[j] = [uj, vj, timej] indicates that there is an undirected edge between the nodes uj and vj, and it takes timej seconds to travel between the two nodes. Finally, you are given an integer maxTime.

A valid path in the graph is any path that starts at node 0, ends at node 0, and takes at most maxTime seconds to complete. You may visit the same node multiple times. The quality of a valid path is the sum of the values of the unique nodes visited in the path (each node's value is added at most once to the sum).

Return the maximum quality of a valid path.

Note: There are at most four edges connected to each node.
"""

from collections import defaultdict
from time import time
from typing import List


class Solution:
    def maximalPathQuality(
        self, values: List[int], edges: List[List[int]], maxTime: int
    ) -> int:
        """
        - DFS w/ set to track visited nodes on each recursion
        - Add to gain depending on if the node is already seen
        - Only continue to next node if time allows
        - Compute the round-trip quality when node == 0
        """
        adj_list = defaultdict(list)
        for a, b, t in edges:
            adj_list[a].append((b, t))
            adj_list[b].append((a, t))

        res = [0]

        def dfs(node, seen, gain, cost):
            if node == 0:
                res[0] = max(res[0], gain)

            for nei, t in adj_list[node]:
                if t <= cost:
                    # If time allows continue to the next node
                    dfs(
                        nei,
                        seen | set([nei]),
                        gain + (nei not in seen) * values[nei],
                        cost - t,
                    )
            return

        dfs(0, set([0]), values[0], maxTime)
        return res[0]

    def reference(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.maximalPathQuality(*case))
                else:
                    self.maximalPathQuality(*case)
        print(f"Runtime for our solution: {time() - sol_start}\n")

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(*case))
                else:
                    self.reference(*case)
        print(f"Runtime for reference: {time() - ref_start}")


if __name__ == "__main__":
    test = Solution()
    test_cases = [
        ([0, 32, 10, 43], [[0, 1, 10], [1, 2, 15], [0, 3, 10]], 49),
        ([5, 10, 15, 20], [[0, 1, 10], [1, 2, 10], [0, 3, 10]], 30),
        ([1, 2, 3, 4], [[0, 1, 10], [1, 2, 11], [2, 3, 12], [1, 3, 13]], 50),
    ]
    test.quantify(test_cases)
