
#Sher
from Stack import Stack

# so I pushed 10 to the bottom, then 20, then 50 .
s = Stack()
s.push(10)
s.push(20)
s.push(50)
#popeped 50 out
s.pop()
#pushed 100 instead the current top is 100
s.push(100)
print(s.size())
print(s.top())

while s.isEmpty() is False:
    print(s.pop())

s.top() # nothing bc we popped out everything
