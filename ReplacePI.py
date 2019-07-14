#Sher Khan

#This program replaces occurence of PI with 3.14 recursivelye


def replacePI(s):
    #This checks if the the string is either empty or has 1 character returns the string itself
    if len(s) == 0 or len(s) == 1:
        return s #returns the string because its empty or has 1 character
    #If the index at 0th is p char and at 1st is i char then  cho
    if ((s[0] == 'p' and s[1] == 'i')):
     smallStr = replacePI(s[2:])
     return '3.14' + smallStr

    else:
     smallStr = replacePI(s[1:])
     return s[0] + smallStr


print(replacePI("pipip"))
print(replacePI("PIPIP"))