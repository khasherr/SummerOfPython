#It is easier to find K frequency of words in sentence using ddictionary

s = "hi my name is is sher sher and i am am trying trying to find frequency of each word words in this string"
k = 2
words = s.split() # turn it into a list and split by space
print(words)
d = {}
for eachwords in words: #iterate over words
    if eachwords in d: #words are in the dictionary we want to increment the occurence of that word by 1
        d[eachwords] = d[eachwords] +1
        #also do this d[eachwords] = d(eachwords, 0) = 1 if you do this you dont need else statement.
    else:
        d[eachwords] = 1  #this means that it occured once

print(d.get(2))

#here we are trying to find frequency of words that occured k times in this case 2 times.
#iterate over each words in dictionary and if words == k print it.
for eachwords in d:
    if d[eachwords] == k:
        print(eachwords,  end=" ")