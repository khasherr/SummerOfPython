#This program asks for 3 inputs and converts the given temperature into farenheit till it reaches
#End temperature by following user input step size or increment size

userInputStartFarenheit = float (input())
userInputEndFarenheit = float (input())
userInputStepSize = float (input())

#starting temp must be less than or equal to end temp
while ( userInputStartFarenheit <= userInputEndFarenheit):
    #formula for celsius conversion
    Celsius = float ((userInputStartFarenheit - 32) * 5 / 9)
    #prints out the temp and celsius value
    print( userInputStartFarenheit,"\t", Celsius)

    #increments the starting temp: adds the user step size for the next loop
    # example 1st run = starting Temp = 0, Cel = -17
    #         2nd run = starting temp = 0+ 20 (lets say 20 is the step) = 20, cel = -17
    #         3rd run = starting temp = 20 (last temp) + 20 (step size) = 40, cel, = -6
    # Pattern continues all the way to and including end temp.
    userInputStartFarenheit = userInputStartFarenheit + userInputStepSize


