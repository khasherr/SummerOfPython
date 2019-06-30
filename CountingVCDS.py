#Sher Khan
#This program finds vowels, consonants, digits and special character in string
def countInString(str):
    vowels,consonants, digits,specialChar = 0,0,0,0, #initialized it to 0
    for letters in str:  #interate every character in string
        #checks if letters is a lower or upper case vowels
        if ((letters >= 'a' and letters <='z' ) or (letters >= "A" and letters <= "Z")):
            if ((letters == "a" or letters == "e" or letters =="i" or letters == "o" or letters == "u") or
                    (letters =="A" or letters == "E" or letters =="I" or letters == "O" or letters =="U")):
                vowels+=1  #increments vowels
            else:
                consonants+=1 #if not vowel then its consonant so increment consonants

        elif(letters >= "0" and letters <= "9" ):  #if letter is a digit
            digits+=1;  #increments


        else:
            specialChar+=1 #if not vowels or digit or consonant then its a specialcharacter so increment
    return vowels,consonants, digits,specialChar






str = "aisdhckscjasJSSHER123!@# aei ^&"
vowels,consonants,digits,specialChar = countInString(str)
print(vowels,consonants, digits,specialChar)
