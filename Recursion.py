#Sher
#recursion - function calling itself
#5! = 5*4 *3 *2 *1 = 120
# def factorial(n):
    #base case is important because thats the base and limit of the depth. There is limit because there is memory
    #use. You can not have infinite memory. By default nearly 1000 depth in python
#     if (n == 0): #base case
#         return 1
#     return n * factorial(n-1)
#
# n = int(input())
# print(factorial(n))

#concept PMI princple of mathematical induction used tp proved lot of things
#1) prove for small number
#2) assum f(something) is true
#3) assume f(something) + 1 is true


#sum of n natural numbers
def sum_n(n):
    if (n==0): #base case
        return 0
    return n+ sum_n(n-1) #adds n to smaller problem which is sum_n(n-1)

n = int(input())
print(sum_n(n))