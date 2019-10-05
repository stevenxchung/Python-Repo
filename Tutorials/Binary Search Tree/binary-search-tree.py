'''
Given a binary search tree is a binary tree where all values to the right are bigger than the values to the left: implement a binary search tree
'''


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTreeBFS(self):
        node = self
        queue = []
        queue.append(node)

        print('BFS: ', end='')
        while len(queue) > 0:
            # Since we are using a queue pop off the first element in the queue and set to node
            print(queue[0].val, end=' ')
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)
        print()

    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return search(root.right, key)
        else:
            return search(root.left, key)

    def binarySearch(self, arr, l, r, x):
        # Code here
        return


# Test binary search
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node2 = Node(2, node4, node5)
node3 = Node(3, node6, node7)
head = Node(1, node2, node3)
head.printTreeBFS()  # 1, 2, 3, 4, 5, 6, 7
