# 11111
# 0000
# 11
# 0

userInput = int(input())

for numbers in range(userInput, 0,  -1): #start from userInput number, end at zero and decrement by 1
  for columns in range (numbers, 0, -1):  #columns start from zero, end at number and increment by 1
    if (numbers % 2 == 0):               #binary pattern divisible = 1 and not divisible = 0
        print(1, end="")
    else:
        print(0, end="")
  print()