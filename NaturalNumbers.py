#This program prints prints first n natural numbers


userInput = int(input()) #takes userinput
counter = 1              #initialized counter to 1
while(counter <= userInput):  #condition to check counter is less than or equal to userinput
    print(counter)    #prints out counter
    counter+=1        #increments counter by 1 to avoid infinite loop