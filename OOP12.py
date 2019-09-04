#OOP - Inheritance - child class inherit properties from parent class
       #polymorphism is the ability to take multiple forms related to method to over riding
       #private members double underscore ___ - ACCESS THROUGH GETTER AND SETTERS 
       #protected member same as public single underscore - DO NOT MODFIED IT

class Vehicle:
    def __init__(self, color, maxSpeed):
        # self.color = color
        # self.maxSpeed = maxSpeed
        self.color = color
        # self.__maxSpeed = maxSpeed #private member
        self._maxSpeed  = maxSpeed #protected

    #for private data members you can getters and setters
    def getmaxSpeed(self):
        # return self.__maxSpeed #private
        return self._maxSpeed #protected

    def maxSpeed(self,maxSpeed):
        # self.__maxSpeed = maxSpeed #private
        self._maxSpeed = maxSpeed


    def printVehicle(self):

     print("Color :", self.color)
     print("Max Speed :", self.__getmaxSpeed()) #__ bc it accessible in vehicle

#car is inheriting properties from vehicles
class Car(Vehicle):
    def __init__(self, color, maxSpeed, numberGears, isConvertible):

        #calls the parent constructor and its properties
        super().__init__(color,maxSpeed)
        self.numberGears = numberGears
        self.isConvertible = isConvertible

    def printCar(self):
        print("Color :", self.color)
        print("Max Speed :", self._maxSpeed)
        # super().print()  #difference between self and super ???
        print("Number of Gears :", self.numberGears)
        print("isConvertable :", self.isConvertible)

     #Same method in both class - printVehicle is in parent class and in subclass(this class)
     #if you do printVehicle which will be called ? parent or subclass ?
     # I think the interpreter first loosk the method into self class if cant be found then in parent class
     #due to inheritance.
    def printVehicle(self):
        print("Number of Gears :", self.numberGears)
        print("isConvertable :", self.isConvertible)




c = Car("black",123, 3,True)
# c.printCar()

#since I made object of car, the printVehicle method will be called from car class !
c.printVehicle()

c.maxSpeed = 10
print(c.maxSpeed)
c.printCar