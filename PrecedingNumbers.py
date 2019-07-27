#Sher Khan
#hacker rank question - input number example 10 -- print number preceeding including 10. prints 1 - 10 including 10

def preceedingNumbers(k):
    for counter in range (1,k+1):
        print(counter, end="")


k = int (input())
preceedingNumbers(k)