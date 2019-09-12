'''
Given:
Preorder traversal: node, left, right
Inorder traversal: left, node, right
Postorder traversal: left, right, node

Write DFS for each traversal
Follow up: can you do it iteratively?
'''


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Initialize nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.right = node2
node2.left = node3
node1.dfs('preorder')
node1.dfs('inorder')
node1.dfs('postorder')
