userInput = int(input())

counter = 1
while (counter <= userInput):
    start_Char = chr(ord("A") + counter -1)
    j = 1
    while (j <= userInput):
        charPrint = chr(ord(start_Char)+ j-1)
        print(charPrint, end="")
        j = j+1
    print()
    counter = counter+1
