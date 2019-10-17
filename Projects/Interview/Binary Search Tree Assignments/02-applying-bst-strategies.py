'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def findMin(self, node):
        if node.left is None and node.right is None:
            return node
        elif node.left is None:
            return self.findMin(node.right)
        else:
            return self.findMin(node.left)

    def minHeapify(self):
        node = self
        arr = []
        queue = []
        queue.append(node)

        while len(queue) > 0:

            node = queue.pop(0)
            arr.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        
        arr.sort()
        return arr

    def printTree(self):
        node = self
        queue = []
        queue.append(node)

        print('Printing BST:', end=' ')
        while len(queue) > 0:

            print(queue[0].val, end=' ')
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        print()


# Test
head = Node(4, Node(5, Node(2), None), Node(8))
head.printTree()  # 4, 5, 8, 2
print('Minimum value in BST:', head.findMin(head).val)
print(head.minHeapify())
