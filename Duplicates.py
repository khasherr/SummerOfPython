
#how it works - brute force method - compare first element with all elements
# array = [1,2,1,2,3]
# index =  0 1 2 3 4
#1st for loop trivase the array
# 2nd for loop to compare the elements

def findDuplicate(list):
    for i in range(0, len(list)): #triverses the array
        for j in range(i+1, len(list)): #comparions with 0th element
            if((list[i] == list[j]) & (i !=j)): #i != j so that element does not compare itself with counter. counter =4, element 4
                print (list[i])

number_of_input = int(input())
list = [int (x) for x in input().split(' ')]
findDuplicate(list)