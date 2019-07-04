#Sher
#Function in dictionary
a = {1:2, 3:4, "list":[1,3],"dict":{3:9} }
print(a) #prints a content

#how to access data in a rmr you can not do a[0] - you need to access them by key
#you  can use normal indexing but key has to be print in dictionary - if key is not present it will throw an error
#you can use .get function with key in the paramenter to return the value of specific key - if key is not present is will return none

# print(a[0]) #do not have key as 0
print(a[1]) #prints 1
print(a["list"]) #prints 1, 3
print(a.get("dict")) #prints 3,9
print(a.get("sher")) #interesting bc sher is not in a i.e not a key and it printed out none !
print(a.get("sher", "hey sher is not present as key ! dude ")) # will print the message not the key
print(a.get("dict", "yoo dict is not present in a as a key dude !")) #will print 3:9 because dict is present as key in a
#in short if key is present it will return the value otherwise it will return the message

print(a.keys()) #presents all the keys
print(a.values()) #presents the all the values
print(a.items()) #presents all the key, value pairs

for i in a:
    # print(i) #prints all the key one by one
    print(i,a[i]) #prints all the key, value
for k in a.values(): #iterates over the the values
    print(k) #prints values

#check if key is present in dictionary
print("lis" in a) #false because lis is not a key
print("sher" in a.values()) #false because sher is not one of the value
print(2 in a.values()) #true because 2 is one of the value

# d = {1:2, "abc":5, "def":7}
# print(d.get(0,5)) prints 5

#adding to dictionary
a["sher"] = {1,3,4,5} #added key, value pair
print(a) #adds sher, and its value to the last
# a["dog"] error you mean init to something

#updating dictionary
a[1] = 10 #updated where key = 1 to value 10
print(a)
b = {3:5, "the": 4, 2:100}
a.update(b) #means update a with b all the only new data will be created in a in this case 2:100 will be added and the:4 if something common b value is used!
print(a)


#removing  from dictionary
a.pop(1) #take key as argument
print(a) #1:10 is not in a anymore because we deleted

del a  #delete the dictionary
print(a)

a = {1:2,"list":[1,2],3:5}
b = {4:5,3:7}
a.update(b)
print(a[3])