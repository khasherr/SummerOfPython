#Sher
#The program finds power of a number recursively
def recPower(base, power):
    if (power == 0):
        return 1
    return base ** power

base, power = [int(x) for x in input().split()]
print(recPower(base,power))
