#Simple for loops
#Author Sher Khan


b = "abcdefghji"
for character in b:
   # print(character); #prints characters on new line
    print(character, end="") #prints characters on same line

userInput1 = int(input())
for numbers in range(1,userInput1, 1):  #range(start, stop, step), include 0 and stops at userInput-1
   print(numbers, end="");

userInput = int(input())
for numbers in range (userInput, 0, -1): #start, stop, step - userInput, 0, decrement by 1
   print(numbers);