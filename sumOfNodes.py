#Sher
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#implemented sum of all node function the rest was ggiven
def sumOfAllNodes(root):
    # Given a binary tree, find and return the sum of all nodes.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################

    #if root is not none
    if root != None:
        # recursive do the work on left subtree and do work on right subtree give me the addition of both and add it up with
        #value at root.data
        return ((sumOfAllNodes(root.left)) + (sumOfAllNodes(root.right))) + root.data
    return 0


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
print  (sumOfAllNodes(root))