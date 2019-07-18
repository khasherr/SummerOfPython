#Sher
#Implementation printing out linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        #function to print linkedlist
def printLL(head):
    while head != None:
        print(str(head.data))
        head = head.next
    print("None")
    return

def takeInput():
    #takes input string and splits them on basis of space and gets the integer part of string
    inputList = [int(element) for element in input().split()]
    #initialized head to none
    head = None
    tail = None
    #triversing through the inputList to create new nodes and find end of the list
    for currentData in inputList:
       #if currentData is -1 that means break out because reached end of the list
        if currentData == -1:
            break
        #otherwise create new node
        newNode = Node(currentData)
       #find the head
        if head is None:
            head = newNode
            #reference to last node
            tail = newNode
        else:
            # current = head
            # #triversing and building connection with nodes while the reference is not none
            # #create new nodes
            # while current.next != None:
            #     current = current.next
            # current.next = newNode
            tail.next = newNode
            #moved tail as well because tail is the last node
            tail = newNode

    return head
head = takeInput()
printLL(head)

#Whats happening ?
#1) we input list 1 2 3 4 5 -1
#2  the first element is not -1 so new node will be created  like this : data: None
#3 before the first element the the head was none, head will start pointing to 1
#4c current data will become 2, node for 2 will be created
#5 checks if head is none or not- as we know head is not None
#6 current.next will store reference to the second node
#7 current data will be 3 now - creates new node for it and by default node3.next == will store none

#important complexity -- taking input takes time O(N^2) implemented tail and head
# to reduce the complexity to 0(n) because all we need to know the reference to last node
#based on that we can move the tail and keep adding