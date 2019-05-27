#Create a linear search function which finds element in this case 4
#author sher khan

def linear_search(li, element):
    for counter in range(len(li)):  # iterate through list
        if li[counter] == element : #checks if value at indexes is equal to element (4)
            return counter     #if true then returns the counter
        else:
            return -1    #not found



li = [2,10,12,6,8,9]
index = linear_search(li, 4)  #passed li and element we want to find in list whcih is 4
print(index)

#Important concepts :
# immutable -> means you can not change to memory, you can only change reference . For example x = 4 -
# x is references to 4 , lets say x = 6 , x reference to 4 is deleted now x references to 6 .

#mutable -> example list - > if list1 and list2 pointing to same reference (a list) . Let says you make change
# is list2 . The changes will be reflected in list1 as well .

list1 = [1,2,3,4,5]
list2 = list1  #point to same reference
print(list1, list2)  # both list same bc point of same reference
list1[2] = 4   #here changed value of index 2 == 4
print(list1, list2)  #the change at index 2 == 4 is reflected in both lists

list2 = [3,4,10,12]  # now list2 points different reference
print(list2)
list2[1] = 6 # change the value of  index at 1 to 6
print(list2) # the change is only relected in list2
