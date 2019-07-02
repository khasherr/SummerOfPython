#Sher Khan

#create tuples
c = (1,2)
d = 3,4

#triversing in tuple
for i in c:
    print(i)

#membersship
print(1 in c) #will print true because 1 is in c
print(1 in d) #false because 1 is not d

#add tuple
f = c +d
print(f)

#c is a tuple so is d and both tuples stored in l so in is tuple of tuple
l = (c, d)
print(l)

#you can do min and max
print(min(c)) #1
print(max(d)) #4

#tricky question
j = (1,4,2,"sher",(10,20))
print(min(j)) #1 error because you can not compare string with integer
k = (1,2,3,(1,20))
print(min(k)) #2 error becuase you can not compare tuple with int

#list to tuple cast
n = [12,4,5,6,7,10]
print(tuple(n)) #will print tuple(12,4,5,6,7,10)