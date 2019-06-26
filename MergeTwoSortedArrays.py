#Sher Khan

#Merge Sort - 2 arrays - 1) sort them 2) compare i & j 3) append to the new array 4) append the left overs
def mergeSort(array1, array2):
    i = 0  #pointer for array 1
    j = 0  #pointer for array 2
    len1 = len(array1)
    len2 = len(array2)
    finalArray = []   #finalarray is empty
    while((i < len1) & (j < len2)):
        if (array1[i] < array2[j]):  #checks if value at array1 is less than value at array 2
            finalArray.append(array1[i])  #add the the value to the new array
            i = i+1
        else:
            finalArray.append(array2[j])   #else add the j value in the second array
            j = j+1   #increment j

    while(i < len1):   # condition for dont want left over elements
        finalArray.append(array1[i])  #append the left over elements to array
        i = i+1  #increment
    while(j < len2):    #condition for dont want left over elment in array2
        finalArray.append(array2[j])   #append the element in array2 to the final array
        j = j +1   #increment

    return finalArray



n1 = int(input())
array1 = list(int(i)for i in input().strip().split(' '))

n2 = int(input())
array2 = list(int(i)for i in input().strip().split(' '))

# array1.sort()
# array2.sort()

finalArray = mergeSort(array1, array2)
print(*finalArray)

#test
# array1 = [1,4,9,10]
# array2 = [2,3,6,7,8]
# finalArray = mergeSort(array1,array2)
# print(*finalArray)  #the star removes the brackets