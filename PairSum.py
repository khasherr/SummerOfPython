

def pair_sum(list, targetelement):
  for i in range (len(list)):
      for j in range (i+1, len(list)):
          for k in range (i+2, len(list)):
           if list[i]+ list[j] + list[k] == targetelement:
              print(list[i], list[j], list[k])

list = [2,1,3,4,5,6]
list.sort()
print(list)
index = pair_sum(list, 11)


#1 2 3 4 5
# temp = list [i]
#if temp