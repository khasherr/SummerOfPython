#Sher

#lets say you want to print square of the elements in li. One way to do this is :
# 1) create empty list, 2) iterate over every element in list 3) add the elements into new list power of 2 4) print list
li = [1,2,3,4]
li_new = []
for elements in li:
    li_new.append(elements**2)
print(li_new)

#however there is a another way to do achieve same thing with one line of code !
#basic syntax [output for expression  condition]
li_new_c = [elements **2 for elements in li] # soo cool !
print(li_new_c)

#let say you want a square of even elements only do wthis with one line of code
#this simple says square the elements in the list if the element is even
li_new_even = [elements**2 for elements in li if elements %2 == 0]
print(li_new_even) #4, 16

#new list- now we want to  append only elements squared that are multiple of 2 AND 3 use online code only
lis = [1,2,3,4,5,6,7,8,9]
lis_new_c = [elements**2 for elements in lis if elements %2 ==0 if elements %3 == 0]
print(lis_new_c) #36

#new list - now we want the common of two list (aka intersection)
lis_1 = [1,2,3,4,5]
lis_2 = [2,3,5,7]
lis_intersec= []
for elements in lis_1: #iterating over every lements in list
    for elements_2 in lis_2:
        if elements == elements_2: #checking if elements from lis_1 == elements_2 from lis_2
            lis_intersec.append(elements) #appends the elements
            print(lis_intersec) #prints 2,3,5

#now do the exact same thing with one line of code
#this is simply saying that we want element in in output, interates both list and checks condition
#the point here is that you can have multiple for loops and conditions. SOO COOL ! I actually love this.
lis_new_intersection = [elements for elements in lis_1 for elements_2 in lis_2 if elements == elements_2]
print(lis_new_intersection) #prints 2,3,5


#new list now lets try it with if else . This time we want to elements squared if multiple of 2  if not then just element
#remember output for expression condtions
li_k = [1,2,3,4]
#this simply says interat over elements in li_k elements squared if element is divisble by 2 else elements if it is not divisble by 2
# just element . WOW I am truly amazed how compact this is.
li_k_new = [elements**2 if elements % 2 == 0 else elements for elements in li_k]
print(li_k_new)

#You could do same thing with string too . Now you want every character to be seperate and list
s = "appleandoranges"
s_new = [elements for elements in s] #output = elements  --- for loop interates over each elements in s
print(s_new) #['a', 'p', 'p', 'l', 'e', 'a', 'n', 'd', 'o', 'r', 'a', 'n', 'g', 'e', 's']

#new list = now we want to store each character into a list
# s h e r  - li[0]
# m i k e
# l u k e
# a      li[3]
k = ["sher", "mike","luke", "a"]
#this iterates over character in elements and elements in k string
k_new = [[character for character in elements] for elements in k]
print(k_new) #[['s', 'h', 'e', 'r'], ['m', 'i', 'k', 'e'], ['l', 'u', 'k', 'e'], ['a']]


#this is interesting example to look at
li = [[ i*j for j in range(4)] for i in range(3)]
print(li) #[[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
