#Sher
#adds stars between same char in a string
def pairStar(s):
    if len(s) == 0 or len(s) == 1:  #if its empty or has 1 char then then return the string
        return s
    #if char at s[0] is equal to char at s[1]
    # returns adds * in between them
    if s[0] == s[1]:
        return pairStar(s[0] + "*" + s[1:])
    else:
        #created smaller string from s[1] --n and check if s[0] == s[1] in that string
        #if not then return s[0] + the substring from s[1:]
     smallerStr = pairStar(s[1:])
     return s[0] + smallerStr

# #test
# print(pairStar('acccc'))
#print(pairstar("sheer'))

n = str(input())
print(pairStar(n))