#Sher Khan
#insertion sort - just like sorting deck of cards with hands 1) pile sorted and second pile not sorted
#always compare to previous one elements in the deck.

def InsertionSort(array):
    length = len(array)
    #compare it with previous index, can not start at 0 because nothing previous to it.
    for index in range(1,length):
         j = index -1  #compare to the previous index
         value = array[index]  # value at index

         while(j>= 0 and array[j] > value):  #shifting elements till this condition holds
             array[j+1] = array[j]
             j = j -1

         array[j+1] = value    #correct position




array = [3,1,2,0,5]
InsertionSort(array)
print(array)