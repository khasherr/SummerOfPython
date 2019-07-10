#Sher Khan
#This program pushes 0's at the end - bubble sort concept but ascending
def sort(array):
    length = len(array)
    for i in range (length-1):
        for j in range (length -1 -i):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
                print(array)


# numberofinput = int(input())
# array = [int (x) for x in input().split()]
# # sorted = sort(array)
# print(sorted)

#test
array = [0,0,1,3,4]
print(sort(array))