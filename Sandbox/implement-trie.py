from distutils.log import debug
from time import time


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self, debug=False):
        self.root = TrieNode()
        self.debug = debug

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            # Update pointer
            curr = curr.children[c]
        # Label end of word
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                if self.debug:
                    print(False)
                return False
            curr = curr.children[c]

        if curr.is_end:
            if self.debug:
                print(True)
            return True

        if self.debug:
            print(False)
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                if self.debug:
                    print(False)
                return False
            curr = curr.children[c]

        if self.debug:
            print(True)
        return True


if __name__ == '__main__':
    test = Trie(debug=True)
    sol_start = time()
    test.insert('apple')
    test.search('apple')  # return True
    test.search('app')  # return False
    test.startsWith('app')  # return True
    test.insert('app')
    test.search('app')  # return True
    print(f'Runtime for reference: {time() - sol_start}')
