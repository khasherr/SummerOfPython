#Sher
#Fraction class and operations with fractions
class Fraction:
    #you can have only 1 init
    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator

    def printFraction(self):
        if self.numerator == 0:
            print(0)
        elif self.denominator == 1:
            print(self.numerator)
        else:
           print(self.numerator, "/", self.denominator)

    def simplifyFraction(self):

        #case if numerator is 0, change the denominator to 1 and return
        if self.numerator == 0:
            self.denominator = 1
            return
        #finds minimum of numerator and denomintor and stores in var currentMinimum
        currentMinimum = min(self.numerator, self.denominator)
        #I want to uptil 2 and while loop will stop when currentMinimum is 1
        while currentMinimum > 1:
            #if remainder is 0 when numerator and denominator divided by currentMinimum break and decrement
            #currentMinimum by 1 (example 4 ,3, 2)
            if self.numerator % currentMinimum == 0 and self.denominator % currentMinimum == 0:
                break
            currentMinimum -= 1
        self.numerator = self.numerator// currentMinimum
        self.denominator = self.denominator // currentMinimum

    def add(self, otherFraction):
        newNumerator = self.numerator * otherFraction.denominator + self.denominator * otherFraction.numerator
        newDenominator = self.denominator * otherFraction.denominator
        self.numerator = newNumerator
        self.denominator = newDenominator
        self.simplifyFraction() #case we want to simplify 9/9 t0 1

    def multiplication(self, otherFraction):
        newNumerator = otherFraction.numerator * self.numerator
        newDenominator = otherFraction.denominator * self.denominator

        self.numerator = newNumerator
        self.denominator = newDenominator
        self.simplifyFraction()


# #no argument by default the numerator is 0 and denominator is 1
# f1 = Fraction()
# print(f1.__dict__) #{'numerator': 0, 'denominator': 1}
# f2 = Fraction(2)
# print(f2.__dict__) # now numerator is 2 - {'numerator': 2, 'denominator': 1}
# f3 = Fraction(8,2) #numerator is 8 and denominator is 2
# print(f3.__dict__) #{'numerator': 8, 'denominator': 2}

# f3 = Fraction(8,2) #numerator is 8 and denominator is 2
# f3.printFraction()
# f4 = Fraction(2,1)
# f4.printFraction() #prints 2
# f5 = Fraction(0,1)
# f5.printFraction() #prints 0
# f6 = Fraction(6,3)
# f6.simplifyFraction()
# f6.printFraction()
f1 = Fraction(2,5)
f2 = Fraction(1,3)
f1.add(f2)
f1.printFraction() #numerator = 11 and denominator = 15  11/15
f3 = Fraction(2,3)
f4 = Fraction(1,3)
f3.add(f4)
f3.printFraction() # 9/9 == 1
f6 = Fraction(2,10)
f7 = Fraction(1,5)
f6.multiplication(f7)
f6.printFraction()






