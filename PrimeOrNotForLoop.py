#Prints out prime numbers
# author Sher Khan

userInputStart = int(input())
userInputEnd = int(input())

if(userInputStart %2 == 0):  # case prime
    startingFrom = userInputStart

else:
    startingFrom = userInputStart +1;  #case not prime example 5 - increment by 1 to make it prime

for numbers in range(startingFrom, userInputEnd+1, 2):
    print(numbers, " " , end="");
