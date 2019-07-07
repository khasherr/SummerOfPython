#Sher
#finds sum of the array recursively

# #takes array and length as argument
def sum_array(arr, n):
    #if length of array is 1 means that there is just 1 wavlue in array so just return the valuue at that index
    if len(arr) == 1:
        return arr[0]
    #recursive step find the sum of the array from index 1 ---n and add value of the index at 0. It also takes length of array
    #as argument
    return arr[0]+sum_array(arr[1:],n)

arr = [1,2,3,4]
print(sum_array(arr,4)) #the length of array is 4 because len(arr) === 4

def sumArray(arr,n):
    # Please add your code here
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sumArray(arr[1:],n)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000) #in python you can set recursion depth limit
n=int(input()) #takes input from suer
arr=list(int(i) for i in input().strip().split(' ')) #splits the array on basis of space
print(sumArray(arr,n))
