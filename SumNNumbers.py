#This program finds and prints sum of numbers from 1 to n

userInput = int(input()) #takes input from user
sum = 0                  # initialized sum to 0
counter = 1              # initialized counter to 1
while(counter <= userInput):  #condition to check counter is less than or userinput
    sum = sum + counter       #sum is sum + counter
    counter+=1                #increment counter to avoid infinity loop
print(sum)                    #prints out sum