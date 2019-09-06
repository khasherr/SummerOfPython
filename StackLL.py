#Sher
#Implementation  of stack using LL
from NodeLL import Node
class Stack:
    def __init__(self):
        #private variavles, head initially pointing to none
        self.__head = None
        #count variable
        self.__count = 0
     #
    def push(self, element):
        #created new node
        newNode = Node(element)
        #setting the head  so that it points to the head
        newNode.next = self.__head
        #head is the new node
        self.__head = newNode
        self.__count = self.__count +1


    def pop(self):
        if self.isEmpty is True:
            print("Stack is empty ! ")
            return
        # store the head in variable data
        # move the head to head.next if head become none then stack is empoty
        data = self.__head.data
        self.__head =self.__head.next
        #decrease the count
        self.__count = self.__count - 1
        return data


    def top(self):
        if self.isEmpty() is True:
            print("stack is empty")
            return
        data = self.__head.data
        return data


    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size() == 0