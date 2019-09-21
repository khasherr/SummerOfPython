#Sher

#Queue using inbuilt Queue and LIFO queue
import queue

#LIFO.QUEUE is LAST IN FIRST OUT type queue.
q = queue.LifoQueue()
q.put(100)
q.put(2)
q.put(200)

while (q.empty() is False):
    print(q.get()) #will prints 200, 2, 1000
