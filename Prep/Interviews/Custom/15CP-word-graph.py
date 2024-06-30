'''
Given a configuration of connected nodes where each node is denoted by a character and a count map of how many times a character can be repeated, return the total number of unique words which can be created.
'''

from collections import defaultdict
from typing import List


class Node:
    def __init__(self, val='', neighbors=None):
        '''Graph node'''
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.count_map = {
            'p': 2,
            'o': 2,
            'r': 1,
            'n': 1,
            'a': 1,
            'c': 1,
        }

    def isWord(self, word):
        # return "popcorn" == word
        return word

    def solver(self, nodes: List[Node]) -> List[str]:
        words = []
        seen_words = set()
        char_count = defaultdict(int)

        def dfs(node, substr):
            if (
                substr in seen_words
                or char_count[node.val] > self.count_map[node.val]
            ):
                # Skip if repeat word or character count exceeded
                return

            if self.isWord(substr):
                words.append(substr)
                seen_words.add(substr)

            for nei in node.neighbors:
                # Add character
                char_count[nei.val] += 1
                substr += nei.val

                dfs(nei, substr)

                # Remove character
                char_count[nei.val] -= 1
                substr = substr[:-1]

            return

        for n in nodes:
            dfs(n, n.val)
        return words


if __name__ == '__main__':
    p1 = Node('p')
    o1 = Node('o')
    r = Node('r')
    n = Node('n')
    a = Node('a')
    p2 = Node('p')
    o2 = Node('o')
    c = Node('c')
    p1.neighbors.extend([r, n, a, o1])
    o1.neighbors.extend([p1, n, a, p2])
    r.neighbors.extend([p1, n, o2])
    n.neighbors.extend([p1, o1, r, a, o2, c])
    a.neighbors.extend([p1, o1, n, p2, o2, c])
    p2.neighbors.extend([o1, a, c])
    o2.neighbors.extend([r, n, a, c])
    c.neighbors.extend([n, a, p2, o2])
    nodes = [p1, o1, r, n, a, p2, o2, c]

    test = Solution()
    print(len(test.solver(nodes)))
