#Sher Khan
#This program checks if a string is premutation of each other or not
#permutation condition 1) both lengths must be same 2) must have same characters

def checkPermutation(str1,str2):
    lengthStr1 = len(str1)
    lengthStr2 = len(str2)

    #1check if both lentghs are equal
    if(lengthStr1 == lengthStr2):
     return True;

     #2 characters in both string much match
    for counter in range(0, lengthStr1):
       if str1[counter] == str2[counter] and lengthStr1 == lengthStr2:
        return True
       else:
           return False

str1 = str(input())
str2 = str(input())

# str1 = "hcrhjhfjsjirlmwlkytm"
# str2 = "hcrtmjsjirlhjhfmwlky"
str1 = sorted(str1) #sort it
# print(str1)
str2 = sorted(str2)
if (checkPermutation(str1,str2)): #compares both strings
    print("true")
else:
    print("false")
