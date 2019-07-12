#Sher
#This program removes occourence of x in a string recursively

def removeX(s):
    if len(s) == 0: #checks if string is empty return the string if empty
        return s
    smallStr = removeX(s[1:])  #new string is chopped the original string from index 1---n and calls recursion on it
    if s[0] == "x": #checks to see if the first index of string is x
        return smallStr #returns smallerStr
    else:
        return s[0] + smallStr #else returns the value at zeroth index and concats with the new string which is the smallerStr

s = removeX("xabxxxxxcd")

print(s)

# Problem: Remove x from string (above code was used to check before implmenting it problem statement
#I know string is bad variable name
def removeX(string):
    if len(string) == 0:
        return string
    smallerStr = removeX(string[1:])
    if string[0] == "x":
        return smallerStr
    else:
        return string[0] + smallerStr

# Main
string = input() #takes input from user
print(removeX(string))
