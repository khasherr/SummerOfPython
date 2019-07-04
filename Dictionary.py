#Sher
#Dictionaries
#in list you access data as li[0] etc
#motivation lets say you have we list ["the", "a", "the"..etc] what is tje frequency of the ??
#one way to do this is by sorting but its takes time.

#in dictionary you can do something like d["the"] = 1 d["a"] = 1 d["the"] = 2 (the got repeated 2 times in list above)
#dictionary = key, value flexible    list = key is fixed ! dictionaries are mutable meaning you add remove update data

a = { }
print(type(a)) #dictionary

k = {"the": 1, "a": 7, "sher":4}
print(k) # prints key and their values in k
print(len(k)) #prints 3
b = k.copy() #copies content of k into b
print(b)
print(id(a), id(b)) #stored in different mem location

#another way to create dictionary
c = dict([{"sher:",1},{"mark",3}])
print(c) #prints the value, key order

#another way to way to create dictionary
j = dict.fromkeys(["abc", "sher", 1])
print(j) #prints the key and values as none
j = dict.fromkeys(["abc", "sher", 1], 2000)
print(j) #init every key with value of 2000

