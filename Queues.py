#Sher

#Queue - first in first out (FIFO) DS.
#Methods available - 1) Enqueue means insert  2) Dequeue means pop 3) size 4) isEmpty 5) front
# Queue has front and rear end - element are inserted or enqueue at rear end
# dequeue means removed at front end


class QueueArray:
    def __init__(self):
        self.__arr = []
        self.__count = 0
        self.__front = 0

    #enqueue just inserts data appends the data into the array
    def enqueue(self, data):
        self.__arr.append(data)
        self.__count+=1

    def dequeue(self):
        #returns -1 if array is empty
        if self.__arr == 0:
            return -1
        #elements is the element at the front of the array
        element = self.__arr[self.__front]
        #increment
        self.__front += 1
        self.__count -= 1
        return element

     #size returns count of the element
    def size (self):
       return self.__count

    #checks if front is emoty returns -1 otherwise returns the element at front
    def front(self):
        if self.__front == 0:
            return -1
        return  self.__arr[self.__front]

    #when the array size is 0
    def isEmpty(self):
        return self.size() == 0

#remember FIFO first in and first out DS.
q = QueueArray()
q.enqueue(10)
q.enqueue(100)
q.enqueue(20000)
q.enqueue(2)
q.dequeue()  #10
q.dequeue()  #100

while (q.isEmpty() is False):
    print(q.front())  # prints 2000 2
    q.dequeue()