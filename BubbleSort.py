#Sher Khan
#Bubble sort -

def bubblesort (array):
    length = len(array);
    for i in range (length-1):
        for j in range (length -1 -i): #bc 1 pass last element sorted. 2nd pass second last element sorted

            if array[j] > array[j+1]: #checks value of adjacent elements
                array[j], array[j+1] = array[j+1], array[j] #swaps
                print(array);

#
#
# numberofInput = int(input())
# array = [int (x) for x in input().split()]
# sorted = bubblesort(array)
# print(sorted)
#

#test
array = [-3,2,1,4]
bubblesort(array);
