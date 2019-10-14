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
        # Edge case
        if currentNode is None:
            print('Value does not exist in this BST')
            return None
        # Base case
        if currentNode.val == key:
            return currentNode
        # If less than key we know that we have to go right
        elif currentNode.val < key:
            return self.returnSubtree(currentNode.right, key)
        # If greater than key we have to go left
        elif currentNode.val > key:
            return self.returnSubtree(currentNode.left, key)

    def insertIntoBST(self, val):
        node = self
        queue = []
        queue.append(node)

        # Queue based iterative solution
        while len(queue) > 0:

            node = queue.pop(0)

            if node.val < val:
                queue.append(node.right)
            elif node.val > val:
                queue.append(node.left)

            # If one of these conditions is true, the right or left node should point to the new node
            if node.val < val and node.right is None:
                node.right = Node(val)
                return
            elif node.val > val and node.left is None:
                node.left = Node(val)
                return

    def deleteInBST(self, val):
        node = self
        queue = []
        queue.append(node)

        while len(queue) > 0:

            node = queue.pop(0)

            if node.val < val:
                queue.append(node.right)
            elif node.val > val:
                queue.append(node.left)

            if node.val == val:
                if node.left is None and node.right is None:
                    node = None
                    return
                elif self.left.val == val:
                    self.left = Node(node.right.val, node.left, None)
                    return
                else:
                    self.right = Node(node.right.val, node.left, None)
                    return

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
# node2 = Node(2, Node(1), Node(3))
# head = Node(4, node2, Node(6))
# head.printTree()  # 4, 2, 6, 1, 3
# head.returnSubtree(head, 2).printTree()
# head.returnSubtree(head, 5)
# head.insertIntoBST(5)
# head.printTree()

# Test deleting a node
node3 = Node(3, Node(2), Node(4))
node6 = Node(6, None, Node(7))
head = Node(5, node3, node6)
head.printTree()  # 5, 3, 6, 2, 4, 7
# head.deleteInBST(3)
head.deleteInBST(6)
head.printTree()  # 5, 3, 7, 2, 4
