'''
You are asked to design a file system which provides two functions:

- createPath(path, value): Creates a new path and associates a value to it if possible and returns True. Returns False if the path already exists or its parent path doesn't exist.
- get(path): Returns the value associated with a path or returns -1 if the path doesn't exist.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

Implement the two functions.
'''
from time import time


class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {}


class Solution:
    def __init__(self, debug=False):
        self.debug = debug
        self.trie = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        folders = [f for f in path.split('/') if f]
        print('Checking if path already exists or if parent not exist...')
        path_exists = self.get(path) != -1
        prefix = path[: path.rfind('/')]
        parent_not_exists = self.get(prefix) == -1

        if path_exists or parent_not_exists:
            if self.debug:
                print(f'Create path status: {False}')
            return False

        node = self.trie
        for f in folders:
            if f not in node.children:
                node.children[f] = TrieNode(value)
            node = node.children[f]

        if self.debug:
            print(f'Create path status: {True}')
        return True

    def get(self, path: str) -> int:
        res = -1
        folders = [f for f in path.split('/') if f]

        node = self.trie
        for f in folders:
            if f not in node.children:
                if self.debug:
                    print(f'Value at path `{path}`: {res}')
                return res
            node = node.children[f]

        res = node.val
        if self.debug:
            print(f'Value at path `{path}`: {res}')

        return res


if __name__ == '__main__':
    sol_start = time()
    print('Example 1')
    test = Solution(debug=True)
    # Return True
    test.createPath("/a", 1)
    # Return 1
    test.get("/a")

    print('\nExample 2')
    test = Solution(debug=True)
    # Return True
    test.createPath("/leet", 1)
    # Return True
    test.createPath("/leet/code", 2)
    # Return 2
    test.get("/leet/code")
    # Return false because the parent path "/c" doesn't exist.
    test.createPath("/c/d", 1)
    # Return -1 because this path doesn't exist.
    test.get("/c")

    print(f'Runtime for our solution: {time() - sol_start}\n')
