#This program takes integer user input and reverses it

#Steps :
# 1- lets say user input a number 1234
# 2- 1234 mod 10 -> 4
# 3- 0 * 10 + 4 - > 4
# 4 - 1234 / 10 -> 123
# 5- Iteration 2 - 123 mod 10 - > 3
#                  4*10+ 3 = 43
#                  123 / 10 = 12
#    Iteration 3 - 12 mod 10 -> 2
#                  43*10 + 2 = 432
#                  12 / 10 = 1
#    Iteration 4 - 1 mod 10 = 1
#                 432 * 10 + 1 = 4321
#                 4321 / 10 -> 0 loop exits because of the while condition


userInput = int(input())

reverse = 0

while(userInput != 0):
    #gives the last digit of a number
    lastDigit =  int(userInput % 10)
    #multiplication by 10 gives us unit place (unit, ten, hundred, thousand) etc.
    reverse =  int(reverse * 10 + lastDigit)
    #divide by 10 so we can shorten the number (example 4321 -> 432)
    userInput  =  int(userInput / 10)
print(reverse)


