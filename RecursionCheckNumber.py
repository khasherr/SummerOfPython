#Sher
#the program find given number x in an array

def checkNumber(arr, x):
    if len(arr) == 0: #checks if length of array is 0 means there are no elements in array
        return False;
    if arr[0] == x:  #if value at first index is equal to the number we want to find then return true
        return True;
    return  checkNumber(arr[1:],x) #check the entire entier starting from index 1 --n if we can find that number

arr= [1,3,4]
x = 5
if checkNumber(arr, x):
    print('true')
else:
    print('false')


#just needed to add the logic into the given template. I tested out the logic above before putting it here
def checkNumber(arr, x):
    # Please add your code here
     if len(arr) == 0:
         return False
     if arr[0] == x:
         return True
     return checkNumber(arr[1:],x)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input()) #size of the array
arr=list(int(i) for i in input().strip().split(' ')) #splits the array bassis on space
x=int(input()) # the number we want to find
if checkNumber(arr, x): #if numbber found print true else false
    print('true')
else:
    print('false')
