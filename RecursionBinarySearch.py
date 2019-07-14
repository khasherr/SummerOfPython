#Sher
#Lets say you want to compare an elements in list of 1000 elements - in linear search it will take
# 1000 comparison because you have to go through every element and check
#But in Binary search 1) the list is sorted (this is must condition for binary search)
# and in bineary search each comparison halfs the list - so 1000 --> 500 --> 250 --> 125 --> so on till you reach element

#KEEP IN MIND BINARY SEARCH THE ARRAY NEEDS TO BE SORTED !
#takes a = list, x = number we want to find
def binarySearch(a, x, startIndex, endIndex):
   #if both indexes crosses means that elements we want to find is not in the list
    if startIndex > endIndex:
        return -1
   #finds mid of list - integer division
    mid = (startIndex+endIndex)//2

     #if value at mid == the number we want to find then remind the index
    if a[mid] == x:
        return mid
    #if the the value at mid is greater the number we want to find - means we have to look into int he
    #lower half of the array. So we start from startIndex and end at the number before mid which is endIndex-1
    elif a[mid] > x:
        return binarySearch(a,x, startIndex, endIndex-1)
    else:
        #if the value at mid is less then the number we want to find that means we have to look into
        # upperhalf of the list. So changed the startIndex -- to the 1 index ahead of mid -- whcih is startIndex+1
        #start from startIndex+1 and end at the normal endIndex
        return binarySearch(a,x,startIndex+1, endIndex)

a = [1,5,6,7,8]
a.sort()
x = 9
#0,4 means length of the array in this case the startIndex of a is 0 and endIndex of a is 4
print(binarySearch(a,x,0,4))