#sher
#sets - has some data that you will use basically collection of data with no particular order
#how many words are unique ? sets ! mantaining something unique - just keys no values

#diff bw sets and dictionary - > dictionary key value pair and sets just key.

d = {"banana", "abc", 23}
print(type(d))

print(2 in d ) #false because 2 is not in d
print(23 in d)  #true

#iterating
for s in d:
    print (s) #will print content of d at random order (no order) order is not mantained

print(len(d)) # 3

#updating
d.add("oranges")
print(d) #adds oranges to the front of d

b= {"mark", "luke"}
d.update(b)
print(d)   #adds content of b to d now b like union if not present

d.remove("mark") #removes mark
print(d)
# d.remove("dskhdkhdk") #key error no key named that
# print(d)
d.discard(23) # discard works same as remove
print(d)

d.discard("kldhkdhdk") #unlike remove this key does not exists but does not give me an error when i run it
print(d)


