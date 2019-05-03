#This program checks if user input integer is palindrome
#Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121
#Author: Sher Khan

userInput = int(input())

#Stored userInput into variable called originalnput to use for comparison
originalInput = userInput

#Reused the code from my last program called ReverseNumber program - you can find it in this repo
reverse = 0
while(userInput != 0):
    #gives the last digit of a number
    lastDigit =  int(userInput % 10)
    #multiplication by 10 gives us unit place (unit, ten, hundred, thousand) etc.
    reverse =  int(reverse * 10 + lastDigit)
    #divide by 10 so we can shorten the number (example 4321 -> 432)
    userInput  =  int(userInput / 10)

#Added condition to check if reversed number is same as user inputted number .
#Palindrome the reverse and user inputted number must be same
if (reverse == originalInput):
      print("Yes it is a palindrome ")
else:
      print("No it is not palindrome ")