'''
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}

According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."
'''
from time import time
from typing import List


def build_tree(nums: List[int]) -> 'Node':
    def dfs(i):
        if i >= len(nums) or nums[i] is None:
            return None

        node = Node(nums[i])
        node.left = dfs(2 * i + 1)
        node.right = dfs(2 * i + 2)

        if node.left:
            node.left.parent = node
        if node.right:
            node.right.parent = node

        return node

    return dfs(0)


def find_node_ref(root: 'Node', node_val: int) -> 'Node':
    def dfs(node):
        if not node:
            return None
        if node.val == node_val:
            return node

        return dfs(node.left) or dfs(node.right)

    res = dfs(root)
    return res


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_nodes = []
        q_nodes = []
        while p:
            p_nodes.append(p)
            p = p.parent
        while q:
            q_nodes.append(q)
            q = q.parent

        # Decide which node we use to traverse up tree
        if len(p_nodes) > len(q_nodes):
            # p is further away from root than node
            q_nodes = dict.fromkeys(q_nodes)
            for p_node in p_nodes:
                if p_node in q_nodes:
                    return p_node
        else:
            # Otherwise, q is further away from root than node
            p_nodes = dict.fromkeys(p_nodes)
            for q_node in q_nodes:
                if q_node in p_nodes:
                    return q_node

    def reference(self, p: 'Node', q: 'Node') -> 'Node':
        p_ref, q_ref = p, q

        while p_ref and q_ref and p_ref != q_ref:
            p_ref = p_ref.parent
            q_ref = q_ref.parent

        res = p_ref or q_ref
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.lowestCommonAncestor(*case))
                else:
                    self.lowestCommonAncestor(*case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

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
    tree1 = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    tree2 = build_tree([1, 2])
    test_cases = [
        (
            find_node_ref(tree1, 5),
            find_node_ref(tree1, 1),
        ),  # 3
        (
            find_node_ref(tree1, 5),
            find_node_ref(tree1, 4),
        ),  # 5
        (
            find_node_ref(tree2, 1),
            find_node_ref(tree2, 2),
        ),  # 1
    ]
    test.quantify(test_cases)
