#Sher Khan
#This program replaces character in a string

def replaceChar(str, char1, char2):
    emptyStr = " "
    for letters in str:
        if (letters == char1): #checks if letter in string is equal to char you want to replace
            emptyStr+= char2  #adds the replacement char into the new string
        else:
            emptyStr+= letters  #other letters just add them to new string because we do not
                                #want to replace that letter
    return emptyStr



str = "khansherr"
strk = replaceChar(str,"k", "l")  #replace occurence of k with l in the string
print(strk)