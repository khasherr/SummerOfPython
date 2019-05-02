#This program takes user input and prints sum of all even numbers from 1 to n

userInput= int(input())  #takes user input
sum = 0                   # initialized sum to 0
counter = 2               #initalize first even number from 2
while (counter <= userInput):  # checks condition counter is less than or greater than user input
    sum = sum + counter        # sum is sum + counter
    counter+=2                 #increment counter by 2 to get even number and avoid infinite loop
print(sum)