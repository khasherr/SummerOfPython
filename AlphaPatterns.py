userInput = int(input())

counter = 1
while (counter <= userInput):
    j = 1
    while (j <= userInput):
        charPrint = chr(ord("A")+ j)
        print(charPrint, end="")
        j = j+1
    print()
    counter = counter+1
