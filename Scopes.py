def function(a,b,c=1):
    return a+b-c
value = function(10,12,5)
print(value)     # will print 10+12 - 5 = 17

def function(a,b,c=1,d=5):
    return a+b+c+d
value = function(1,2,d=7)
print(value)  # will print a = 1, b = 2, c =1 , d=7  => a+b+c+d = 11


def function(a,b,c=1):
    return a+b-c
value = function(10,12)
print(value) # will print 21


#Beauty of python is that you can give a initialize a variable in function parameter
#lets say you want to return sum of 2 or 3 numbers

def sum(a, b, c=0): #if you provide 2 numbers
    return a+b+c

print(sum(2,3)) # will return sum of 2+3+0 = 5 because we did not put 3rd parameter so by default was taken as zero
print(sum(2,3,5)) # will return 2+3+5 which is 10

def f(a =0, b, c):
    return a+b+c
print(sum(2,1)) # will not work because non-default paraemter or non initialize variable goes in first and default goes second
                # this case to make it work we should do b,c, a=0



a = 14
def f():
    a = 12
    return a
a = f()
print(a) # will print 12

a = 14
def f():
    a=12
f()
print(a)   # will print 14

a=14
def f():
    global a
    a=12
f()
print(a)  #will print 12