#Sher
#This program aska for user input and checks if string is a palindrome
#Palidrome is a phrase that is read same backward as forward.
# Example: abcba, madam, sherresh

def palidrome(s):
    #if length of string is 0 or 1 then yes its a palindrome
    if len(s) == 0 or len(s) == 1:
        return True
    #if char at first index is not equal to char at last index then return false
    if s[0] != s[len(s)-1]:
        return False
    else:
        #strings are immuatable so i made a new string from index 1 ---n
        #and called palindrome on that
     smallStr = (s[1:len(s)-1])
    return palidrome(smallStr)


s = str(input())  #takes string from user
if palidrome(s):  #checks condition if its palindrome returns true else false
    print("true")
else:
    print("false")

    #test
# print(palidrome('abccba'))
# print(palidrome('ninja'))
# print(palidrome("abcdfaosjosdj"))

