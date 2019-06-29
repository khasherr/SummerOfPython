
#sher khan
#this program pusesh zero at the end without changing the order
def pushZeroEnd(array):
    length = len(array)
    for i in range (length-1):
        for index in range (length-1):
            if array[index] == 0: #if value at index == 0 then
             array[index+1], array[index] = array[index], array[index+1] #swaps with the next
#
n1 = int(input())
array = [int (x) for x in input().strip().split(' ')]
pushZeroEnd(array)
print(*array)

#test
array = [0,0,1,2,4]
