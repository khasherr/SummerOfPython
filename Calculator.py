# This program takes user input choice of 1 - addition 2 - substraction  3- multiplication 4- division and 5- modulus
# after that it takes 2 integers from user to perform such ops.

#Author: Sher Khan

userInputChoice = int(input())

#initialize counter
counter = 1   

while(counter == 1):
 if (userInputChoice == 1):    #addition
    userInputAdd1 = int(input())
    userInputAdd2 = int(input())
    print(userInputAdd1 + userInputAdd2)
    userInputChoice = int(input())


 elif(userInputChoice == 2):    #substraction
    userInputSub1 =int(input())
    userInputSub2 = int(input())
    print(userInputSub1 - userInputSub2)
    userInputChoice = int(input())

 elif(userInputChoice == 3):     #multiplication
    userInputMul1 = int(input())
    userInputMul2 = int(input())
    print(userInputMul1 * userInputMul2)
    userInputChoice = int(input())

 elif(userInputChoice == 4):       #division
    userInputDiv1 = int(input())
    userInputDiv2 = int(input())
    print(userInputDiv1 / userInputDiv2)
    userInputChoice = int(input())

 elif(userInputChoice == 5):       #modulus
    userInputMod1 = int(input())
    userInputMod2 = int(input())
    print(userInputMod1 % userInputMod2)
    userInputChoice = int(input())

 elif (userInputChoice == 6):          #exits and counter is 0 to avoid infinite loop
     exit()
     counter =0
 else:
    print("Invalid Operation")            #input greater than 6 gives invalid ops and asks for user input again
    userInputChoice = int(input())



