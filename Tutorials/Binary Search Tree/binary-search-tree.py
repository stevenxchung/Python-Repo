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

    # Traversing a binary search tree using linked lists
    def search(self, root, key):
        # Base case reached, return the root node
        if root is None or root.val == key:
            return root

        if root.left is None or root.right is None:
            return None

        # If value is less than than key, we have to go right
        if root.right.val < key:
            return self.search(root.right, key)
        # Otherwise go left
        else:
            return self.search(root.left, key)


class ArraySolution:
    #  Traversing a binary search tree using arrays
    def binarySearch(self, arr, low, high, x):
        if x > arr[high] or x < arr[low]:
            return -1

        mid = 1 + (high - low) // 2

        if high >= 1:
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return self.binarySearch(arr, low, mid - 1, x)
            else:
                return self.binarySearch(arr, mid + 1, high, x)
        elif arr[low] == 0 and arr[high] == 0:
            return 0
        else:
            return -1


# Test binary search for linked lists
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node2 = Node(2, node4, node5)
node3 = Node(3, node6, node7)
head = Node(1, node2, node3)
head.printTreeBFS()  # 1, 2, 3, 4, 5, 6, 7
searchKey = 2
print('Searching node...', head.search(head, searchKey).val if head.search(
    head, searchKey) else head.search(head, searchKey))

# Test binary search for arrays
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Searching target...', ArraySolution(
).binarySearch(arr, 0, len(arr) - 1, 0))
