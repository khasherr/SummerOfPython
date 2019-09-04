
#by default every class inherits from object class
#there are 3methods that object class gives:
#1) __init__ used to initialze object
#2) __new__ used to create object we dont use this much
#3) __str__ used to create description
class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return "this is a circle class which takes radius as an argument "

c  = Circle(3)
# print(c) #memory location if object method is not over ridden by __str__ function
print(c) # prints this is a circle class which takes radius as an argument - hence gives description bc we implemented the __str__ function