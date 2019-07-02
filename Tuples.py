#Sher Khan
#tuples to similiar lists . Tuples are used to store multiple entries in a variable.
#difference between tuple and list - tuple is immutable and list are mutable
#in python multiple things are stored as tuple.
#how to declare tuple

#string, tuple, lists are order sequence
a = (1,3) #e is referencing to tuple. By default multiple things as tuple
print(a)
print(type(a))
#a[0] = 9  #tuples are immutable meaning you can change the value inside
#how to delete tuple
del a[0] #again you can not delete single value
print(a) #error


del a
print(a) #deleted the tuple

a = ("ab","abc","def")
print(min(a)) #will print ab bc of legth