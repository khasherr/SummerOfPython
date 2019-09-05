#Sher
#type of erros - 1) syntax error 2) zero division error 3) name error 4) type error
# try and except - just like in Java try and catch . You  try the code excecute the code, if any error it will directly
# go to exception. You can also have multuple exceptions.
# try - exception - else - finally
#you can raise own exceptiion using own class
class ZeroDenominatorException(Exception):
    pass

try:
    n = input("Enter a number ")
    numerator = int(n)
    n = input("Enter a denominator ")
    denominator = int(n)
    #you can raise your own exceptions as well example
    # this exceptions occurs when you enter denominator as zero
    #then it occurs
    if denominator == 0:
        # raise ZeroDivisionError
          raise ZeroDenominatorException("Denominator can not be zero !")
    print("Denominator can not be zero")

except ValueError: #if you input characters other than integers. If no error is given it handles all error
    print("Numerator and denominator should integers")
except ZeroDivisionError:
    print("Division by zero not allowed")
except ZeroDenominatorException:
    print ("Zero denominator exception is raised")

#else will be excecuted if no exception occurs
else:
  value = numerator/denominator
  print(value)

finally:
    print("will execute if exception if raised or not  either way")


