#sher
#2d arrays rows and columns

#This list contains 4 rows and 4 columns  4 x 4 structure
li = [[1,2,3,4],[5.6,7,8],[9,10,11,12],[13,14,15,16]]

#prints out the content of list at index 0 = [1,2,3,4]
print(li[0])

#prints at the value of list at index 0 with column 1 and answr is 2
print(li[0][1])

#updated the element at index 0 and column 1 to be 15
li[0][1] = 12
print(li[0][1])

#How are 2d list stored ??
# in this example li = [[1,2,3,4],[5.6,7,8],[9,10,11,12],[13,14,15,16]] - lists of lists each index is a list
# index stores references to the list for example somewhere the list [1,2,3,4] will be stored and will have address
# li[0] will hold that address which has reference to the list 1,2,3,4. So li = [addressof li[0], addressof li[1] etc]


#new list here we have r = 2 c = 2
c = [[1,2,3], [4,5,6]]
print(c[0])
print(id(c[0])) #ref address of first list 0th index [1,2,3]
print(id(c[1])) #ref address of second list 1st index [4.5.6]

c[1] = "sher"
print(c[1])
print(c) #[[1, 2, 3], 'sher'] not a list because 1st part is a list and second part a string . Now li[1] is point to string  not list

#jagged list means number of rows and columns are not same
li = [[1,2,3,4],[5,6],[7,8,9]] #here we have 3 rows but the columns are differe some of them have 4 columns 2 columns and 3 columns
print(li[1][3])


