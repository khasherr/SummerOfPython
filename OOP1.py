#Sher
#OOP1 - Object Oriented Programing
#class - template how object should look like
#object - has data, functionality  and is an instance of class

#create student class template. Can not be empty !
#if you do not have anything to write just write pass
# class Student:
#     #telling pythong that hey I want an empty class
#      pass
#     # name = " "
#     # rollNumber = 12
#
# #create objects
# s1 = Student ()
# print(type(s1)) #type is Student
# print(s1) #object with memory locations
# s1.name = "Sher"
# print(s1.name) #prints Sher
# print(s1.__dict__) #to see all the attributes of s1 - so far it has just name attribute whihc is sher
# print(hasattr(s1,"name")) #takes 2 arg - s1 and key - checks if s1 object has an name attribute - returns true
# print(getattr(s1,"name")) #gives the value of attribute name
# print(getattr(s1,"name", " ")) #checks if s1 has name attribute if so, returns the name attribute otherwise empty string
# print(getattr(s1, "course", "")) #s1 object does not have course attribute so returns emoty string
# print(delattr(s1, "name"))
# print(s1.__dict__) #empty because deleted attribute in line 24

print("**************************************************************************************************************")

# key to remember - once object is created it is then passed on to the function called __init__ function with in class
# it is called right after object is created. The init function is perfect place to assign attributes
class Student:
    # init function takes an arg. Self means that object being created is passed on to this function .
    # Self also has exact address of s1 object. S1 and Self are both references to same object
    def __init__(self,name, rollNumber):
        # self.name = "Sher"
        # self. rollNumber = 12

        #name is whatever the name is passed to me
        self.name = name
        self.rollNumber = rollNumber

     #function that prints students name and rollnumber
    def printStudent(self):
       print("my name is", self.name, "and my roll number is ", self.rollNumber )

# s1 = Student ()
# print(s1.__dict__) #s1 has attributes name and roll number
# # s2 = Student("Mike", 12)
# print(s2) #TypeError: __init__() takes 1 positional argument but 3 were given bc remember the init function takes self as arg

#now we can do something like
s2 = Student ("Sher", 12)
print(s2.__dict__)

#called printStudent function on s2 object.
#In reality the printStudent function is Student.printStudent(s2)
#but s2.printStudent() called it on object directly !
s2.printStudent()
Student.printStudent(s2) #same thing as s2.printStudent()
