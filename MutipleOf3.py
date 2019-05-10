#This program asks for userInput and prints multiple of 3 using for loop
#Author Sher Khan


#prints multiple of 3 - first input HAS TO BE MUL  OF 3
userInput = int(input())
userInput3 = int(input())

for numbers in range(userInput, userInput3+1, 1): #includes userInput2 and increments by 1
  if (numbers % 3 == 0): # multiple of 3 or divisble by 3 to print multiple of 3 only
   print(numbers);

#Alternate way to do it
userInput1 = int(input())
userInput2 = int(input())
if (userInput1 % 3 == 0):
    startingFrom = userInput1
elif (userInput1 % 3 == 1): #case if input = 10
     startingFrom = userInput1 +2;
else:
    startingFrom = userInput1+1 # case if input = 5

for numbers in range (startingFrom, userInput2+1, 3):
    print(numbers)  # 6 - 99 - 99 being last multiple of 3


