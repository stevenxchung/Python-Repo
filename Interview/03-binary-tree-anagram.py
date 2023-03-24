'''
Given two binary trees, determine whether each level is an anagram to the comparing tree. Return data with level and nodes or each tree in JSON

Test case 1
      b
     /   \
    a     c
   / \   /  \
  c   o d   e

      b
     /   \
    a     p
   / \   /  \
  c   d o   e

return data in this format
[
  {1: ["b", "b"]},
  {3: ["code", "cdoe"]},
]

Test case 2
      a
     /   \
    a     c
     \   /  \
      o d   e

      b
     /   \
    a     p
   / \   /  \
  c   d o   e

return data in this format
[]

Test case 3
      a
     /   \
    a     c
     \   /  \
      o d   e
     /
    a

      b
     /   \
    a     p
     \   /  \
      d o    e
              \
               a

return data in this format
{
  {3: ["ode", "doe"]},
  {4: ["a", "a"]}
}
'''

from collections import defaultdict
from time import time
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bfs(self, tree: Optional[TreeNode]):
        # Return dict with levels
        res = defaultdict(list)
        q = [(tree, 1)]

        while q:
            node, level = q.pop(0)
            res[level].append(node.val)

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return res

    def test(
        self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        tree_map_1 = self.bfs(tree1)
        tree_map_2 = self.bfs(tree2)
        res = defaultdict(list)

        for k, v in tree_map_1.items():
            if k in tree_map_2 and set(tree_map_1[k]) == set(tree_map_2[k]):
                word1 = ''.join(tree_map_1[k])
                word2 = ''.join(tree_map_2[k])
                res[k].append(word1)
                res[k].append(word2)

        return res

    def reference(
        self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        return

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.test(*case))
                else:
                    self.test(*case)
        print(f'Runtime for our solution: {time() - sol_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(*case))
                else:
                    self.reference(*case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        (
            TreeNode(
                'b',
                TreeNode('a', TreeNode('c'), TreeNode('o')),
                TreeNode('c', TreeNode('d'), TreeNode('e')),
            ),
            TreeNode(
                'b',
                TreeNode('a', TreeNode('c'), TreeNode('d')),
                TreeNode('p', TreeNode('o'), TreeNode('e')),
            ),
        ),
        (
            TreeNode(
                'a',
                TreeNode('a', None, TreeNode('o')),
                TreeNode('c', TreeNode('d'), TreeNode('e')),
            ),
            TreeNode(
                'b',
                TreeNode('a', TreeNode('c'), TreeNode('d')),
                TreeNode('p', TreeNode('o'), TreeNode('e')),
            ),
        ),
        (
            TreeNode(
                'a',
                TreeNode('a', None, TreeNode('o', TreeNode('a'))),
                TreeNode('c', TreeNode('d'), TreeNode('e')),
            ),
            TreeNode(
                'b',
                TreeNode('a', None, TreeNode('d')),
                TreeNode(
                    'p', TreeNode('o'), TreeNode('e', None, TreeNode('a'))
                ),
            ),
        ),
    ]
    test.quantify(test_cases)
