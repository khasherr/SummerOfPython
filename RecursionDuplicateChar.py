#Sher
#This program removes duplicates in a string

def removeDuplicateChar(s):
    #if length of string is empty or has one char then return the string itself
    if len(s) == 0 or len(s) == 1:
        return s
    #created new string from char index 1 to n
    newStr = removeDuplicateChar(s[1:])

    #if value at both indexes == to each other then return the chopped string from index 1 --n
    if s[0] == s[1]:
        return newStr
    else:

        #if not equal then add the value at index 1 with the chopped string
        return s[0] + newStr

#Test to see if it works
s = 'abccdd'
print(removeDuplicateChar(s))



# Main - takes userdefined input as strng and removes the repeated char in it
string = input().strip()
print(removeDuplicateChar(string))
