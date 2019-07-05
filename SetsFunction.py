#sher
#Set function

#intersection
a = {1.2,3,4}
b = {3,4,5,6}
c = {3,4}
print(a.intersection(b))  #3,4
print(a.union(b)) # a and b with no repeating vals

#difference
print(a.difference(b)) #removes all the content that intersects a and b and content of b  1, 2
print(b.difference(a)) #5.6

#symmertic differece
print(a.symmetric_difference(b)) # give me a and b except the intersection part
# print(a.intersection_update(b))

#subset
print(a.issubset(b))  #false
print(c.issubset(a))  #true c is a subset of a
print(c.issubset(a)) #false
print(a.issuperset(c)) #true

print(a.isdisjoint(c)) #false because there is sometihng in common


#interesting question - concept remember that sets are unique !
s = {1,2,3,5,4,2,3,1}
# print(len(s),end='')
print(len(s))  #5
s.add(4)
s.add(3)
print(s)
# print(len(s)) #5

