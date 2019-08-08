#Sher Khan
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printTreeDetailed(root):
    if root is None:
       return
    print(root.data, end=":")

    if root.left != None:
            print("left child is ", root.left.data, end=",")

       #checks if the right node is not none and prints the data
    if root.right != None:
            print("right child is", root.right.data,end=",")

        #empty line
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)


def treeInput():
    rootData = int(input())

    #this is important if nothing is enter through input then it returns -1
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root


#write a function to find the largest element in binary tree
#if root is none then return -1
#other wise find the largest in the left substree
#find the largest in right subtree
#largest of all is max(left, right, root.data)
# root children has no data returns -1 to the root
def largestData(root):
    if root == None:
        return -1
    largestLeftSide =largestData(root.left)
    largestRightSide = largestData(root.right)
    largestOfAll= max(largestLeftSide,largestRightSide,root.data)
    return largestOfAll


root = treeInput()
printTreeDetailed(root)
print()
#call the largestData fucntion
print(largestData(root))