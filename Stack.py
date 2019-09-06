#Sher
# STACKS Abstract Datatype-  stacks of books - lIFO DS. Entry and Exit points are seen.
# methods push -> insert, pop -> delete, top -> access the top element of stack, size -> how many elemts presents
# isEmpty -> number of elements ins tacks
#recursion stack -> stored in stack memory . Stack can be implement via array and linked list
#testing of methods can be found in the StackTest.py

class Stack:

    #init function
    def __init__(self):
        #private and empty array to hold values
        self.__data = []

      #push inserts items into the array using the append method built in
    def push(self, item):
        self.__data.append(item)

     #pop deletes if the array is empty then prints that it is empty otherwise
     # it pops the data in the array
    def pop(self):
        if self.isEmpty():
            print("the stack is empty can pop anything")
        return self.__data.pop()

    #top is the last insert value . If the array is empty then there is nothing at the top
    #otherwsie returns the last element in the stack which can be found by len(self._data) -1
    def top(self):
        if self.isEmpty():
            print("Nothing at the top")
            return
        return self.__data[len(self.__data) -1]

     #returns the size of the stack
    def size(self):
        return len(self.__data)

    def isEmpty(self):
        return self.size() == 0









