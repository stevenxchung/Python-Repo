# Two simple ways to code linked lists in python

# Nodes
# 1. Value - anything: strings, integers, objects
# 2. The next node


class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


node1 = linkedListNode(5)  # 5
node2 = linkedListNode(10)  # 10
node3 = linkedListNode(15)  # 15
node4 = linkedListNode(20)  # 20

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
