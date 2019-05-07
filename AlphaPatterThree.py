userInput = int(input())
counter = 1
while (counter <= userInput):
    j = 1
    while (j <= userInput):
        charPrint = chr(ord("A"))
        print(charPrint, end="")
        j = j+1
    print()
    counter = counter+1
