#dictionary - key - value. You  can use whatever key you want to use and whatever value you want to store.

# a ={"the":1, "abc": 2, "cat":10000}
# print(a)
# print(len(a)) #len is 3
# print(type(a))
#
# b = a.copy()
# print(b)
#
# c = dict([("The",1), ("cat", 2)])
# print(c)
#
# d = dict.fromkeys(["abc",10,2])
# print(d) #value are none of the keys

k = {1:2, 3:4, 'list':[1,23], "dict": {1:2}}
print(k)

#access
# print(k[0]) # error bc there is no key 0
print(k[3]) # 4

print(k.get('li')) # return none bc there is no key li .
print(k.get("list", 0)) # will return the value if the key is present otherwise the second argument
print(k.get("li",0))
print(k.keys())
print(k.values())
print(k.items()) #get ALL the key value pair.

# for loop
for i in k:
    print(i, k[i])  #key value pairs using for loop

for c in k.values():
    print(c)

print("list" in k) #true bc list is in dictionary k
print(1 in k)
print(3 in k)

#checking the values it will not work because this only works for KEY not VALUE.
print(2 in k)

#adding a tuple into a dict
k["tuple"] = (1,2,3,4)
print(k)

#updates existing dict with b key/values whatever is common b values are used
b = {3:5, "the":4, 2:100}
k. update(b)
print(k)
#removing
k.pop("tuple")
print(k)
del k[1] #deletes key 1 and its values
print(k)