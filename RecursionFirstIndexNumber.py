#Sher
#This program finds the first occurence of a numver in list

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
    smallerList = arr[1:]
    smallListCal = firstIndex(smallerList,x)

    if smallListCal == -1:
        return -1
    else:
        return smallListCal +1
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


#How it works:
#step 1: checks if len(list) == 0 if so returns -1 by len(list) == 0 its mean list is empty. So obvious list is empty .
#if not then proceeds to step 2:
#step 2: checks if list[index] == the number we want to find if so returns 0 means that yes we want found the number if not then
#proceed to step 3
#step 3: store the list from index 1 -- n into some variable (1 --n because we did not find the number at index[0]
#so in that smaller list repeat step1 -2 . If found return it and add to each returning call
#if not found then it will poinbt to empty list and return -1 after each returning call
