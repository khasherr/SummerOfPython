#Sher
#This program finds the first

# Test 0 - false 1 - true
# def FirstIndex (arr, number):
#     l = len(arr)
#     #means if the list is empty
#     if l == 0:
#         return 0
      #if array at 0th index is the number we want t find then return the number
#     if  arr[0] == number:
#         return 1;
      #look into the array from 1st index and see if we can find the number
#     return FirstIndex(arr[1:],number)
#
# arr = [1,4,6,7,8]
# # number = 2 #none
# number = 4 1
# print(FirstIndex(arr, number))

def firstIndex(arr, x):
    # Please add your code here
    l = len(arr)
    #means if the list is empty
    if l == 0:
        return -1
    if  arr[0] == x:
        return 0;
    return firstIndex(arr[1:],x)

# Main - this code was given
from sys import setrecursionlimit
setrecursionlimit(11000)
#takes input sizeof(array)
n=int(input())
#splits basis on space
arr=list(int(i) for i in input().strip().split(' '))
#the number we want to find
x=int(input())
print(firstIndex(arr, x))

