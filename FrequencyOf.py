#Sher
#Frequency

a = "my name is sherr and this is a word string that has many words"
words = a.split() #splits by white space
# print(words)  #prints out the a with splits by whitespace

d= {}
for w in words: #iterate over the words
    if w in d: #if the words in the d (dictionary)
        d[w] = d[w]+1  #if words in dictionary increase its frequency
    else:
        d[w] = 1 #else if not in dictionary make the frequency to be 1

print(d) #prints each word as key and value as frequency for exmaple 'my':1 'name":1 'is":2


#write a function that does exact same thing as above
def FrequencyKWords(s, k):
    words = s.split()
    for w in words:
      d[w] = d.get(w,0) +1 #by default get will teturn but we dont want that -instead give me zerro if the word is not there
    for w in d:
        if d[w] == k:
            print(w)


