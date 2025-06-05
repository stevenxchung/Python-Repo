from time import time
from typing import List


class TreeNode:
    def __init__(self, key=None, val=0, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class TreeMap:
    def __init__(self, debug=False):
        self.debug = debug
        self.root = None

    def insert(self, key: int, val: int) -> None:
        '''
        Inserts a key-value TreeNode into the BST ordered by keys.
        '''
        if not self.root:
            self.root = TreeNode(key, val)

        def dfs(key, val, node):
            if not node:
                # Add to end
                return TreeNode(key, val)
            elif key < node.key:
                node.left = dfs(key, val, node.left)
            elif key > node.key:
                node.right = dfs(key, val, node.right)
            else:
                # If key already exists, update value to new value
                return TreeNode(key, val, node.left, node.right)

            return node

        self.root = dfs(key, val, self.root)

    def get(self, key: int) -> int:
        '''
        Returns the value mapped to input key or -1 if not found.
        '''

        def dfs(key, node):
            if not node:
                return -1
            elif key < node.key:
                node.left = dfs(key, node.left)
            elif key > node.key:
                node.right = dfs(key, node.right)

            return -1 if node.left == -1 or node.right == -1 else node.val

        res = dfs(key, self.root)
        if self.debug:
            print(f'get(): {res}')

        return res

    def getMin(self) -> int:
        '''
        Returns value mapped to the smallest input key.
        '''

        def dfs(prev, node):
            if not prev and not node:
                return -1
            if not node:
                return prev.val

            return dfs(node, node.left)

        res = dfs(None, self.root)
        if self.debug:
            print(f'getMin(): {res}')

        return res

    def getMax(self) -> int:
        '''
        Returns value mapped to the largest input key.
        '''

        def dfs(prev, node):
            if not prev and not node:
                return -1
            if not node:
                return prev.val

            return dfs(node, node.right)

        res = dfs(None, self.root)
        if self.debug:
            print(f'getMax(): {res}')

        return res

    def remove(self, key: int) -> None:
        '''
        Removes a key-value TreeNode from the BST ordered by keys.
        '''
        if not self.root:
            return

        def get_min_node(node):
            return get_min_node(node.left) if node and node.left else node

        def dfs(key, node):
            if not node:
                return

            if key < node.key:
                node.left = dfs(key, node.left)
            elif key > node.key:
                node.right = dfs(key, node.right)
            else:
                # Single node case
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left

                # Swap current node with next in-order node
                min_node = get_min_node(node.right)
                node.key, node.val = min_node.key, min_node.val
                node.right = dfs(node.key, node.right)

            return node

        self.root = dfs(key, self.root)

    def getInorderKeys(self) -> List[int]:
        '''
        Returns an array of the keys in the tree in ascending order.
        '''
        res = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            res.append(node.key)
            dfs(node.right)

            return

        dfs(self.root)
        if self.debug:
            print(f'getInorderKeys(): {res}')

        return res


if __name__ == '__main__':
    sol_start = time()
    print('##### Test 1 #####')
    test = TreeMap(debug=True)
    test.insert(1, 2)
    test.get(1)
    test.insert(4, 0)
    test.getMin()
    test.getMax()

    print('\n##### Test 2 #####')
    test = TreeMap(debug=True)
    test.insert(1, 2)
    test.insert(4, 2)
    test.insert(3, 7)
    test.insert(2, 1)
    test.getInorderKeys()
    test.remove(1)
    test.getInorderKeys()
    test.remove(2)
    test.getInorderKeys()
    test.remove(3)
    test.getInorderKeys()
    test.remove(4)
    test.getInorderKeys()

    print('\nAdditional testing...')
    test = TreeMap(debug=True)
    test.insert(5, 0)
    test.insert(3, 0)
    test.insert(8, 0)
    test.insert(2, 0)
    test.insert(4, 0)
    test.insert(6, 0)
    test.insert(9, 0)
    test.insert(4, 4)
    test.insert(5, 5)
    test.getInorderKeys()
    test.remove(1)
    test.getInorderKeys()
    test.remove(2)
    test.getInorderKeys()
    test.remove(3)
    test.getInorderKeys()
    test.remove(8)
    test.getInorderKeys()

    print(f'Runtime for our solution: {time() - sol_start}\n')
