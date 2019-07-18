#Sher
#finding length of linkedlist - just implemented code def length code
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# I only implemented the length function
def length(head):
    #############################
    # Implement your code here to find the length of linked list#
    #############################
    #initialized count to zero
    count = 0
    #while there is head
    while(head):
        #head is the next data is list - head is moving
      head = head.next
        #each time there is a data add to the count
      count = count+1
    return count

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
len=length(l)
print(len)