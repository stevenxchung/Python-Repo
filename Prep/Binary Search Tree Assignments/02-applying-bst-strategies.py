'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Probably do not need this, good exercise to go through however
    def findMin(self, node):
        if node.left is None and node.right is None:
            return node
        elif node.left is None:
            return self.findMin(node.right)
        else:
            return self.findMin(node.left)

    # Return BST as an array from smallest to largest
    def minHeapify(self):
        node = self
        arr = []
        queue = []
        queue.append(node)

        # Traverse BST and add to queue and array
        while len(queue) > 0:

            node = queue.pop(0)
            arr.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        
        # Sort array from smallest to largest
        arr.sort()
        return arr

    # Since we based array from smallest to largest the 2nd largest would be based on the length of the tree minus the k value for example
    def kthLargest(self, k):
        treeAsArr = self.minHeapify()
        # Finding the value is O(1), but the entire process to get the kth largest value is O(n * log(n)) due to the sort() method
        return treeAsArr[len(treeAsArr) - k]

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
print('The largest element in the BST is:', head.kthLargest(1))
print('The 2nd largest element in the BST is:', head.kthLargest(2))
