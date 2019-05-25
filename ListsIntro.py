#whats the difference btweeen list and arrays
# arrays - homogeneous datatype
#list - heterogenus type
#list stores references of elements and references are stored continously (
# example if first reference is 100 the next one will be 104, 108, 112. etc by 4 byte

#concept of resizing - when you initialize a list the length will doubled thats how you can append





#create a list
#list = [1,2,3,4,5]
#print(type(list))

myList = [1,2,3,4,"maxi", 2.5]


#Access
print(myList[0])

#you can not do it iwll give you range out of bound error
#myList[6] = 9

#slicing
print(myList[1:3]) #gives values of index from 1 - 2 excluding 3rd index - [2,3]
print(myList[1:])  #prints entire list from 1 index

#append --> added to the last  and insert--> kay, value pair
myList.append("man") #will insert it at last
print(myList)

myList.insert(0, 10)  #inserts 10 and zeroth index you can do it at any index and insert value
print(myList)

myList.insert(10, "this is last value") #10th index does not exist just pushes to the last eitherway
print(myList)

myList.append([10,11,12])  #appends [10,11,12] at the end of the list in form of object
print(myList)

# extend inserts multiple elements into the list
myList.extend([9,10,11]) #this will insert 9,10,11 exludedly not like not list object
print(myList)

#removing elements - remove(element) - removes that specific element from list if present
myList.remove(10)  #removes 10 from list - remove iff element present in list . If have 2 same elements in list the first one will be removed
print(myList)

#pop function - list.pop() removes element from last, list.pop(5) removes element at index 5. Can only remove whatevewr is present at list
myList.pop()
print(myList) #removes 11

myList.pop(2) #remove element at index2
print(myList)  #removes 3

#length - tells you how many elements are present
len(myList)

#negative indexes start at very l