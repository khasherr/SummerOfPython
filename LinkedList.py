#Sher
#what is a linked list - not stored in continuos memoery location
# 1  - 2 - 3 - 4 -5 - there is a link in between elements. Each elements in link list is called node. Each
#nodes are stored at different / specific reference number. Important part is connection in between nodes

#node will store 2 things  1) data and 2) the reference to next number example: 1 200 -> 2 350 -> 3 - 489
# so 1 is data and 200 is the reference to data 3 and so on  the last node will has none in their referenc because
#it will not be referencing to anything . Head - > reference to the 1st node [node] if I have refewrence to head
# i have complete linked list
class Node:

     def __init__(self,data):
       self.data = data
       self.next = None

a = Node(13) #a datafield = 13 nextfield == address of 9
b = Node(9)
a.next = b
# print(a.data)  #13
# print(b.data)  #9
# print(a.next) # prints address of  9
# print(b.next) #none because 9 is the last node and does not hold any reference to any number
# print(a.next.data) # will print 9 . This saying a.next --> reference of 9
# print(a)
# print(a.next)
# print(b) #prints refewrence to b
# print(b.data) #prints 9
print(b.next.data) #eror because there is no data after 9 its empty

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def printLL(head):
    while head is not None:
        print(head.data,end=" ")
        head = head.next



node1 = Node(10) # first node contains 10
node2 = Node(20)  #second node contains 20
node3 = Node(30)  #third node contains 30
node4 = Node(40)
node1.next = node2 # this means that node1 reference should be to the data in the of second node
print(node2)
print(node2.data)
node2.next = node3  #node 2 should reference to node3 data
print(node3)
print(node3.data)
node3.next = node4  #node 3 reference to node4 data
printLL(node2)  #will print from node 2 ----onwards to node node 4