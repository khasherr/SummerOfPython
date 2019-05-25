

myList = [1,2, "Sher", "Mark", 2.5]

#looping over list  - range

for counter in range(len(myList)):
    print(myList[counter])

#Without the range function
for element in myList:
    print (element)

for element in myList[2:]:  #slice start from second index
    print (element)

for element in myList[2:4]: # from 2- 3 exlcuding 4 index
    print(element)
