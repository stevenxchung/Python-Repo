from collections import defaultdict
import heapq
from math import inf
from time import time
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Node:
    def __init__(self, key=0, val=0):
        '''Doubly Linked-list Node'''
        self.key, self.val = key, val
        self.prev = self.next = None


class Solution:
    def __init__(self, debug=False):
        self.debug = debug
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        '''
        - Loop through each char in input string
        - Find chars by traversing through child maps
        - If '.' is encountered, can select any char in map
        '''

        def dfs(i, node):
            if i == len(word):
                return node.is_end
            elif word[i] == '.':
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True

            if word[i] not in node.children:
                return False
            node = node.children[word[i]]

            return dfs(i + 1, node)

        res = dfs(0, self.root)
        if self.debug:
            return print(f'word={word} : {res}')
        return res


if __name__ == '__main__':
    test = Solution(debug=True)
    sol_start = time()
    test.addWord('bad')
    test.addWord('dad')
    test.addWord('mad')
    test.search('pad')  # return False
    test.search('bad')  # return True
    test.search('.ad')  # return True
    test.search('b..')  # return True

    # Additional
    print('\nAdditional testing...')
    test = Solution(debug=True)
    test.addWord('a')
    test.addWord('a')
    # true, true, false, true, false, false
    test.search('.')
    test.search('a')
    test.search('aa')
    test.search('a')
    test.search('.a')
    test.search('a.')

    test.addWord('at')
    test.addWord('and')
    test.addWord('an')
    test.addWord('add')
    # true, false
    test.search('a')
    test.search('.at')

    test.addWord('bat')
    # true, true, false, false, true, true
    test.search('.at')
    test.search('an.')
    test.search('a.d.')
    test.search('b.')
    test.search('a.d')
    test.search('.')
    print(f'Runtime for our solution: {time() - sol_start}\n')
