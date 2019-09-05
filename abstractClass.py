#Sher
#abstract class contains abstract methods - they are declared but no
#implementation. Module -> abc -> abstract base class and abstract method as fuctionality as decorator
# You need to implmenet all the abstract methods in the child class otherwise it will give you an error

from abc import ABC, abstractmethod

class Automobile(ABC):
    def __init__(self):
        print("Automobile")

    @abstractmethod
    def start(self):
        print("Hey Automobile start !")
        #pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def drive(self):
        pass
#Sher
#prints Automobile if @abstractmethod is not specified
#but onces you specify abstractmethod then it can not create object of that class !
# c = Automobile()

class Car (Automobile):
    def __init__(self,name):
        print("car is created")
        self.name = name

    def start(self):
        # super().start() #if you want to call the parent start method
        print("hey Car start !!")

        # pass

    def stop(self):
        pass

    def drive(self):
        pass

c = Car("Toyota") #error you need to implement ALL the abstract fucntions in the child class !!
c.start() #calls the car start method


