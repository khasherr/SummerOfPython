"""
Asks for user input and prints the following pattern provided user input = 4

1234
123
12
1

author: Sher Khan

"""


n = int (input() )

for row in range (n, 0, -1):
    for columns in range (1, row+1):
     print(columns, end="")
    print()


