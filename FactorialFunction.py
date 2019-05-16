#This program calculates factorials

def factorial(n):
     n_factorial = 1
     for counter in range (1, n+1): #inclusive userinput
        n_factorial = n_factorial * counter
     return (n_factorial)


#test
print(factorial(4)) #returns 4




