from StackLL import Stack

s = Stack()
s.push(10)
s.push(20)
s.push(100)
print(s.top())

while s.isEmpty() is False:
    print(s.pop())
print(s.top())