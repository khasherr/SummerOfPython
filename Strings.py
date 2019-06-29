#STRINGS -> "a" , 'a' and "'a"'  -> benefit of triple quote means that you ininitialize a string multuple lines
#You can index string as well. However, for multi line strings be aware of \n  example below:
s = "'my \
    name is sher \
    wow!'"
print(s[2]) #prints y
print(s[3]) #prints nothing because of new line at index 3
print(s[8]) #prints n

#how string are stored ?
#example s = "sher"-> somewhere sher is stored and s has reference to it.
#if you say s = "khan" -> somewhere khan will be created and s will point to khan now not sher
# if you have 3 string variable pointing to sher - > sher will be created once and string variable
#will point to sher . (python optimizes for short strings)

#convice yourself by writing code:
a = "sher"
print(id(a))  #checking mem loc
b = "sher"
print(id(b)) # same mem loc as a which mean both are stored once at specific mem loc

#IMPORTANT STRINGS ARE IMMUTABLE - MEANS IF A = "SHER" YOU  CAN ACCESS CHARACTER OF STRING S[0] BUT
# YOU  CAN NOT CHANGE THE STRING IT SELF MEANING A[0] = "K" - NOT ALLOWED.  EXAMPLE BELOW
s = "sher"
print(s[0])
s[0] = "k"  #error TypeError: 'str' object does not support item assignment
#if you want to change the character you need to create another variable k = "kher"


#CONCATENATION
a= "orange"
a = a + "pink"
print(a)  #prints orangepink
print(id(a))
a+="orange" #sinple means a = a+orange
print(a) #orangepinkorange
print(id(a)) #both mem loc are different
a = "green"
a = a*3  #will print greengreengreen
print(a)
print(id(a))

a = "red"
a = a + 3 #not allowed you can not add a word and number
print(a) #error

a ="red"
a = a + str(3) #cast it to string before you can append . If you do not cast it will give you an error !
print(a)