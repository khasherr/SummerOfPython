def isPrime (userInput):
    for counter in range (2, userInput): #starts 2 : end userInput-1
        if (userInput % counter == 0):   #
            break
        else:
            return True

        return False


print(isPrime(17))

#prints prime numbers
def printFrom2ToN(userInput):
    for k in range(2, userInput+1):
        is_k_prime = isPrime(k)
        if(is_k_prime):
         print(k)
print(printFrom2ToN(10))  #print all the prime from 1 -10


#calculate NCR
