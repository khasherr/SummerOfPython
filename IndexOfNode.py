class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


#just implemented linear search function
def linearSearch(head, n):
    #  Given a linked list and an integer n you need to find and return index
    #  where n is present in the LL. Do this iteratively. Return -1 if n is not
    #  present in the LL. Indexing of nodes starts from 0.

    current_node = head
    count= 0
    while current_node and current_node.data !=n:
         count = count + 1
         current_node = current_node.next
    if current_node is None:
      return -1
    return count

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
data=int(input())
index = linearSearch(l, data)
print(index)