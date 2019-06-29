#Sher Khan
#String slicing - [start:end:step] rememeber its [start:end:step) step is exclusive not inclusive!
s = "abcdef"
print (s[4:2:-1])

#check frequency of letter l in string  - each character of string
str = 'hello sher lloljokel'
count = 0
for letter in str:
   if (letter == 'l'):
     count = count +1

print(count)


#method - via indexing
str = "hello sher lol"
counter = 0
for index in range(len(str)):
    if(str[index] == 'l'):  #indexing method
        counter+=1
print(counter)


#in and not in operations what is substring ? start from a character and continues to end of string
#quest what is substring of hello ?
#h, he, hel, hell, hello, e, el, ello, l, ll, llo, l, lo, o

#you can  use in  operator to check if substring is a string or not ! not in means oppostite

str= "hello"
if 'hel' in str: #checks if hel is a substring of hello and yes it is
    print("yes");  #will print yes
else:
    print("no");

str2 = "sherr"
if "hoo" not in str2: #not in operator is just opposite of in
    print("no is not substring")  #will print no is not substring
else:
    print("yes it is a substring")

#How to compare two strings ? ON BASIS OF ASCII VALUE 'A' - 65 - etc , 'a' =99 -etc
# comparator ops. ==, <=, >=, != etc
a = "sher"
print(a == "sher") #true because sher is equal to sher compares character by character

b = "khan"
print(b >= "khan") #true
print(b>= "KHA")  #true because of length
print(b > "khan") #fase
print(b>= "K")  #true because 1) ascii valur and length
print(b> "KHAN") #true because lower case asci valye greater
print("KHAN"> b) #false




