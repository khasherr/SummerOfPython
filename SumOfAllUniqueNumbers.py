#sher
#sum of all unique numbers avoid adding repetition

a = {1,1,2,3,5,5,6,3}
print(len(a)) #5  bc it sets disregards duplicates and counts it once

c = {}
print(type(c)) #dictionary by default

def sumUnique(li):
    s = set( )  #this will create empty set this is how you declare a set
    for i in li:
        s.add(i) #adds the element into set
    sum = 0
    for i in s:
        sum = sum+ i #one elements could be present once in a set
    return sum

print(sumUnique([1,2,2,3,4,5,6,6,10])) #prints 31 its only counnts element once ! therefore unique


#Interesting
# s = {}
# s.add(4)
# s.add(4)
# print(len(s)) #will print error because dictionary

