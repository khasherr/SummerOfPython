#Sher
#Here implementing Queue using 2 stacks. Queue is FIFO and Stacks is LIFO
# The concept is to use 2 stacks 1) for enqueue (push) and 2) for dequeue (pop)
# once elements are enqueue into stack1 you can not pop it right away because stack
# are LIFO, you want FIFO behaviour. So you trasnfer element from S1 to S2
# and then you pop them out and it will be in FIFO DS.
class QueueWithTwoStacks:
    def __init__(self):
        self.__stack1 =[]
        self.__stack2 = []

    def enqueue(self,data):
    #pop element of stack1 and append those element into stack2
        while(len(self.__stack1) != 0):
            self.__stack2.append(self.__stack1.pop())
    #after pop new element will pushed into stack1
        self.__stack1.append(data)

    #pop element from stack2 and append into stack1
        while(len(self.__stack2) != 0):
            self.__stack1.append(self.__stack2.pop())





    #if stack is empty return -1 else pop the element from stack1
    def dequeue(self):
        if (len(self.__stack1) == 0):
            return -1
        return self.__stack1.pop()


    #if stack is empty return -1 else return the last element of stack
    def front(self):
        if (len(self.__stack1) == 0):
            return -1
        return self.__stack1[-1]

    #size if the len of stack
    def size(self):
        return len(self.__stack1)

    #stack size is 0
    def isEmpty(self):
       return self.size()==0

q = QueueWithTwoStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

while(q.isEmpty() is False):
    print(q.front())
    q.dequeue()