#sher khan
#this program removes a character from a string

def RemoveChar(strInput,character):  #takes string and character as input
   # newStr = " "    #string are immutable
    for letters in strInput:   #iterate over letters
        strInput = strInput.replace(character,"") #replace character  with emptry string

    return strInput;
    # newStr+= strInput.replace(character,"") #replace function - replaces character with empty string
    # return newStr;  #returns the new string


strInput= str(input())
character = str(input())
str1 = RemoveChar(strInput, character)
print(str1)