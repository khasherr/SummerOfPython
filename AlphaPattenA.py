"""
Program asks for user input and prints the following pattern (this pattern is for user input  is 4)
A
BB
CCC
DDDD

author: Sher Khan

"""


userInput = int (input())
counter = 1
while(counter <= userInput):
    start_char = chr(ord("A")+ counter -1)
    j = 1
    while(j <= counter):
        charPrint= chr(ord(start_char))
        print(charPrint, end="")
        j= j+1
    print()
    counter = counter+1