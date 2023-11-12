'''
Two simple ways to code linked lists in python part 1.
'''


class LinkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


node1 = LinkedListNode(5)  # 5
node2 = LinkedListNode(10)  # 10
node3 = LinkedListNode(15)  # 15
node4 = LinkedListNode(20)  # 20

node1.nextNode = node2  # node1 -> node2
node2.nextNode = node3  # node2 -> node3
node3.nextNode = node4  # node3 -> node4

currentNode = node1
while True:
    print(currentNode.value, "->", end=" ")
    if currentNode.nextNode is None:
        print("None")
        break
    currentNode = currentNode.nextNode
