#This program takes userInput and prints 1 times according to userInput.
# Example userInput 2 - will print 1 two times

#takes user input
userInputNumber = int(input())
#initialized
counter = 1
#checks counter is less than or equal to userInput then runs
while (counter <= userInputNumber):
    print(1)
# increments counter to avoid loop running infinitely
    counter +=1