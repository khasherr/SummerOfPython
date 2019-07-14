#Sher
#This program finds geometric sum - straighforward

def geometricSum(k):
    if k < 0:
      return 0

    else:
        return 1/(pow(2,k)) + geometricSum(k-1)


print(geometricSum(3))

print("******************************************************************")

def geometricSum(k):
    if k < 0:
      return 0

    else:
        return (1/(pow(2,k)) + geometricSum(k-1))


k = int(input())
print((format(geometricSum(k),'.5f')))