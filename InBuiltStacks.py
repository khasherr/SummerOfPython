#Sher

#inbuilt stack as list
# x = [1,2,3,4]
# x.append(5)
# print(x)
# x.pop()
# print(x)

# inBuilt Queue
import queue
q = queue.Queue()
#enqueue
q.put(10)
q.put(200)
q.put(1000)

#dequeue
while not q.empty():
    print(q.get()) #prints 10 200 1000

#STACK version of QUEUE
q = queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)
while not q.empty():
    print(q.get()) #prints 3 2 1



