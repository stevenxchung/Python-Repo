'''
A BST (binary search tree) is a binary tree where:
  a. The value in each node to its left subtree is less than the current node
  b. The value in each node to its right subtree is greater than the current node

Looking up a value takes O(log(n)) if the tree is balanced and O(h) is the height of the tree

Implement the following:
1. Search in a BST
2. Insert into a BST
3. Delete Node in a BST
'''


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Return the subtree where the key is found
    def returnSubtree(self, node, key):
        currentNode = node
        # Base case
        if currentNode.val == key:
            return currentNode
        # If less than key we know that we have to go right
        elif currentNode.val < key:
            return self.returnSubtree(currentNode.right, key)
        # If greater than key we have to go left
        elif currentNode.val > key:
            return self.returnSubtree(currentNode.left, key)

    def printTree(self):
        node = self
        queue = []
        queue.append(node)

        print('Printing BST in Level Order:', end=' ')
        while len(queue) > 0:

            print(queue[0].val, end=' ')
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        print()


# Test
node2 = Node(2, Node(1), Node(3))
head = Node(4, node2, Node(6))
head.printTree()  # 4, 2, 6, 1, 3
head.returnSubtree(head, 2).printTree()
