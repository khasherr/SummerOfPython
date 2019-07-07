#Sher
#How to take input in 2D list

# str takes input and splits based on space by default so you will get something like ['number','number']
str = input().split()
# print(str)
n,m = int(str[0]), int(str[1])#integer part of str
print(n, m)
li = [[int(j)for j in input().split()] for i in range(n)]
print(li)

# how to take jagged list dont specify the number of columns
k = int(input()) #enter number of rows and based on this will you will have that much rows but different number of columns
lis = [[int(j)for j in input().split()] for i in range(k)]
print(lis)

# iterating over 2d list if number of columns is given
li = [[1,2,3,4],[5,6,6,7],[9,9,10,11]]
n = 3
m =  4
for i in range(n):
    for j in range(m):
        print(li[i][j], end = ' ') #prints the above li row wise
    print()

# what about jagged list ?
li = [[1,2,3],[5,6,6,7,9],[9,9,10,11,12,13,15]]
n = 3 # we know number of rows its fixed which is 3 but we do not know number of columns
for row in li: #we can use in operator iterates over rows in li
    for element in row: #iterate over elements in li
        print(element, end = " ") #every row in seperate line
    print()

#join
print("abc".join("ab")) #aabcb

