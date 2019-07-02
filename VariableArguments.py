#tuples

#motivation suppose we have
def sum(a,b):
    return a+b
print(sum(1,3)) #passed two arguments and prints 4
# print(sum(1,2,3,4)) #error because it only accept 2 arguments

#What if we have variable length of arguments like 6 or 7 how would you do that ?
def sum(c,d, *morearg):
    # return c+d+morearg
# print(sum(1,2,3,4,10,10)) #will not work ! error because int and tuple
      answer = c+d  #integer addtion
      for i in morearg: #iterating  through each user input args
          answer = answer + i #adding it to asnwer
      return answer
print(sum(2,4,5,6,10,11,20)) #variable length of arguments

#

def sum_diff_prod(a,b):
    return a+b, a-b, a*b
c = sum_diff_prod(1,3)
j,d,e = sum_diff_prod(1,3)
print(c)
print(j,d,e)