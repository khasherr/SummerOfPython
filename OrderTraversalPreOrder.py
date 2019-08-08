import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#this function was given
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

#I only implemented preOder Function:
#base case if root is none
#recursion steps preoder (left subtree) preorder(right subtree)
#give the result to the root and the root will add its own value
#for input purposes -1 means that no children of the root
def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    # ROOT LEFT RIGHT
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root == None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)


# Main
#remeber preoder is root, left child , right child -1 means no child
# input: 8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
# result: 8 3 1 6 4 7 10 14 13
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
preOrder(root)