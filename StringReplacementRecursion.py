#Sher
#This program replaces a character in a string

#takes arg string, char you want to replace, char you want to replace with
def replaceChar(s,a,b):
   #if len of string is zero it means it empty and returns the s
    if len(s) == 0:
        return s
   #chopped string from index 1 -- n and checks to replace occurence of something with something
    smallerStr = replaceChar(s[1:a,b])

    #checks the first character of the string if is 'a' return b + the chopped string
   #return whatever the s[0] is + chopped string
    if s[0] == a:
        return b + smallerStr
    else:
       return s[0] + smallerStr


#test
#takes string, replaces occurence of e with y in that string
print(replaceChar("sheeerr","e","y"))
